#!/usr/bin/env python3
"""Ritaglia il bianco in eccesso dalle immagini PNG (di default quelle in imgs/gantt).

Per ogni immagine individua il rettangolo minimo che contiene il contenuto
(tutto cio' che non e' bianco/trasparente), aggiunge un margine configurabile
e ritaglia. Di default sovrascrive i file, tenendo una copia degli originali.

Esempi:
    python3 ritaglia_bianco.py --dry-run          # mostra cosa farebbe
    python3 ritaglia_bianco.py                    # ritaglia in place (con backup)
    python3 ritaglia_bianco.py --margine 40       # margine piu' generoso
    python3 ritaglia_bianco.py --uniforme         # stesso ritaglio per cartella
    python3 ritaglia_bianco.py imgs/gantt --out imgs/gantt_ritagliati
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def maschera_contenuto(img: Image.Image, soglia: int) -> np.ndarray:
    """Maschera booleana: True dove il pixel NON e' bianco.

    Le immagini con canale alfa vengono prima composte su fondo bianco, cosi'
    il trasparente e il semi-trasparente sono valutati come apparirebbero
    stampati sulla pagina.
    """
    if "A" in img.getbands() or (img.mode == "P" and "transparency" in img.info):
        rgba = img.convert("RGBA")
        fondo = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        img = Image.alpha_composite(fondo, rgba)
    arr = np.asarray(img.convert("RGB"), dtype=np.uint8)
    return (arr < soglia).any(axis=-1)


def bbox_contenuto(maschera: np.ndarray, min_pixel: int) -> tuple[int, int, int, int] | None:
    """Bounding box (sinistra, alto, destra, basso) del contenuto.

    Una riga/colonna e' considerata vuota se contiene meno di `min_pixel`
    pixel non bianchi: serve a ignorare puntini isolati o bordi sporchi
    dovuti alla compressione dell'export.
    """
    righe = np.flatnonzero(maschera.sum(axis=1) >= min_pixel)
    colonne = np.flatnonzero(maschera.sum(axis=0) >= min_pixel)
    if righe.size == 0 or colonne.size == 0:
        return None
    return int(colonne[0]), int(righe[0]), int(colonne[-1]) + 1, int(righe[-1]) + 1


def espandi(box: tuple[int, int, int, int], margine: int, dim: tuple[int, int]):
    """Allarga il box di `margine` pixel restando dentro l'immagine."""
    larghezza, altezza = dim
    sinistra, alto, destra, basso = box
    return (
        max(0, sinistra - margine),
        max(0, alto - margine),
        min(larghezza, destra + margine),
        min(altezza, basso + margine),
    )


def unione(boxes: list[tuple[int, int, int, int]]) -> tuple[int, int, int, int]:
    return (
        min(b[0] for b in boxes),
        min(b[1] for b in boxes),
        max(b[2] for b in boxes),
        max(b[3] for b in boxes),
    )


def trova_png(radice: Path, ricorsivo: bool) -> list[Path]:
    pattern = "**/*.png" if ricorsivo else "*.png"
    return sorted(p for p in radice.glob(pattern) if p.is_file())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Individua e ritaglia il bianco in eccesso nelle immagini PNG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "cartella",
        nargs="?",
        default="imgs/gantt",
        type=Path,
        help="cartella con i PNG da ritagliare (default: imgs/gantt)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="scrive i risultati in questa cartella (struttura replicata) invece di sovrascrivere",
    )
    parser.add_argument(
        "--margine",
        type=int,
        default=16,
        help="pixel di bianco da lasciare attorno al contenuto (default: 16)",
    )
    parser.add_argument(
        "--soglia",
        type=int,
        default=250,
        help="un pixel e' 'bianco' se tutti i canali sono >= soglia (0-255, default: 250)",
    )
    parser.add_argument(
        "--min-pixel",
        type=int,
        default=3,
        help="pixel non bianchi minimi perche' una riga/colonna conti come contenuto (default: 3)",
    )
    parser.add_argument(
        "--uniforme",
        action="store_true",
        help="usa lo stesso ritaglio per tutte le immagini della stessa cartella "
             "(utile per mantenere la scala coerente tra i gantt di una fase)",
    )
    parser.add_argument(
        "--no-ricorsivo",
        action="store_true",
        help="non scendere nelle sottocartelle",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="non salvare una copia degli originali (solo con sovrascrittura in place)",
    )
    parser.add_argument(
        "--backup-dir",
        type=Path,
        help="cartella dei backup (default: <cartella>/../<nome>_originali)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="mostra solo cosa verrebbe ritagliato, senza scrivere nulla",
    )
    args = parser.parse_args(argv)

    radice: Path = args.cartella
    if not radice.is_dir():
        print(f"Errore: '{radice}' non e' una cartella.", file=sys.stderr)
        return 1

    immagini = trova_png(radice, ricorsivo=not args.no_ricorsivo)
    if not immagini:
        print(f"Nessun PNG trovato in '{radice}'.")
        return 0

    # Passata 1: calcola il bounding box del contenuto di ogni immagine.
    box_per_file: dict[Path, tuple[int, int, int, int]] = {}
    dim_per_file: dict[Path, tuple[int, int]] = {}
    for percorso in immagini:
        with Image.open(percorso) as img:
            dim_per_file[percorso] = img.size
            box = bbox_contenuto(maschera_contenuto(img, args.soglia), args.min_pixel)
        if box is None:
            print(f"  saltata (tutta bianca): {percorso}")
            continue
        box_per_file[percorso] = espandi(box, args.margine, dim_per_file[percorso])

    if args.uniforme:
        # Unisce i box delle immagini della stessa cartella e stessa dimensione.
        gruppi: dict[tuple[Path, tuple[int, int]], list[Path]] = {}
        for percorso in box_per_file:
            gruppi.setdefault((percorso.parent, dim_per_file[percorso]), []).append(percorso)
        for membri in gruppi.values():
            comune = unione([box_per_file[p] for p in membri])
            for p in membri:
                box_per_file[p] = comune

    # Passata 2: ritaglia e scrive.
    backup_dir = None
    if args.out is None and not args.no_backup and not args.dry_run:
        backup_dir = args.backup_dir or radice.parent / f"{radice.name}_originali"

    ritagliate = 0
    for percorso in immagini:
        box = box_per_file.get(percorso)
        if box is None:
            continue
        larghezza, altezza = dim_per_file[percorso]
        nuova_l, nuova_a = box[2] - box[0], box[3] - box[1]
        relativo = percorso.relative_to(radice)
        risparmio = 100 * (1 - (nuova_l * nuova_a) / (larghezza * altezza))

        if box == (0, 0, larghezza, altezza):
            print(f"  {relativo}: gia' senza bianco in eccesso, invariata")
            continue

        print(
            f"  {relativo}: {larghezza}x{altezza} -> {nuova_l}x{nuova_a} "
            f"(offset {box[0]},{box[1]}; -{risparmio:.0f}% area)"
        )
        if args.dry_run:
            continue

        if args.out is not None:
            destinazione = args.out / relativo
        else:
            destinazione = percorso
            if backup_dir is not None:
                copia = backup_dir / relativo
                copia.parent.mkdir(parents=True, exist_ok=True)
                if not copia.exists():
                    shutil.copy2(percorso, copia)

        destinazione.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(percorso) as img:
            ritaglio = img.crop(box)
            ritaglio.save(destinazione, format="PNG", optimize=True, dpi=img.info.get("dpi", (96, 96)))
        ritagliate += 1

    if args.dry_run:
        print("\n(dry-run: nessun file modificato)")
    else:
        print(f"\n{ritagliate} immagini ritagliate su {len(immagini)}.")
        if backup_dir is not None and ritagliate:
            print(f"Originali salvati in: {backup_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
