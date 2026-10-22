# Tuning Ledger

Piattaforma basata su blockchain *permissioned* per la registrazione, la certificazione e la
consultazione delle modifiche apportate a un veicolo dopo l'immatricolazione, attraverso il
**DMVP** (*Digital Modified Vehicle Passport*): un passaporto digitale immutabile associato
univocamente al numero di telaio.

Progetto per il corso di **Sistemi Informativi**, A.A. 2025/26 — Prof. Domenico Saccà
Dipartimento di Ingegneria Informatica, Modellistica, Elettronica e Sistemistica

Gabriele Hamil (mat. 256747) · Matteo Stricagnolo (mat. 252309)

## Struttura del repository

Il lavoro segue la metodologia **GOREM** e procede dall'analisi del contesto fino alla
valutazione economica. Ogni cartella di modellazione contiene i sorgenti `.drawio` e una
sottocartella con i PNG esportati.

| Cartella | Contenuto | Export |
|---|---|---|
| `Context Modeling/` | Stakeholder, Softgoal e Softgoal Dependency Diagram; Business Model Canvas (`.tex`) | `exports/` |
| `Scenario Modeling/` | Role, Goal e Goal Dependency Diagram | `exports/` |
| `Use Case Modeling/Use Case Diagram/` | Use Case Diagram dei cinque attori | `exports/` |
| `Use Case Modeling/Process Diagram/` | Processi in notazione BPMN | `exports/` |
| `Project Plan/` | Architettura a componenti, deployment e gruppi di lavoro; `dati_project_plan.xlsx` | `export/` |
| `Project Plan/gantt/` | Diagrammi di GANTT e prospetti di impegno per ruolo (`.xlsx`) | `gantt_exports/` |
| `Relazione/` | Sorgenti LaTeX della relazione e PDF finale | — |

## Relazione

I sorgenti stanno in `Relazione/`, un file per capitolo sotto `capitoli/`:

1. Sommario e Introduzione
2. Analisi del Contesto — modellazione GOREM del contesto
3. Descrizione dello Scenario Specifico — modellazione GOREM, Business Model Canvas
4. Idea Progettuale — Use Case in GOREM e Processi in BPMN
5. Analisi SWOT e valutazione dell'idea progettuale
6. Project Plan — architettura, tecnologie, pianificazione delle due fasi
7. Business Plan — costi, ricavi, Break Even Point e ROI
8. Conclusioni

seguiti da `bibliografia.tex`. Gli articoli citati sono archiviati in `Relazione/riferimenti/`.

### Compilazione

```sh
cd Relazione
latexmk -pdf main.tex     # produce main.pdf
latexmk -C                # ripulisce gli artefatti di compilazione
```

Servono due passate perché indice, elenchi di figure e tabelle e riferimenti incrociati si
stabilizzino: `latexmk` le esegue da solo. Gli artefatti (`.aux`, `.log`, `.toc`, …) sono
ignorati da git; `main.pdf` invece è versionato in quanto elaborato finale.

### Immagini

`Relazione/imgs/` non è generata automaticamente: i PNG vengono esportati da draw.io o dai
fogli di calcolo nella cartella `export/` della rispettiva area e poi copiati sotto
`Relazione/imgs/<categoria>/` (`context`, `scenario`, `usecase`, `bpmn`, `projectplan`,
`gantt`). **Dopo aver modificato un diagramma occorre riesportarlo e ricopiarlo**, altrimenti
la relazione continua a mostrare la versione precedente.

Due immagini non hanno un sorgente versionato e vanno rigenerate a mano se servono modifiche:
`imgs/swot.png` (matrice SWOT) e `imgs/evoluzione.png` (grafico del Business Plan).

`Relazione/ritaglia_bianco.py` ritaglia il bianco in eccesso dai PNG esportati, utile per i
GANTT che escono dai fogli di calcolo con ampi margini vuoti:

```sh
python3 ritaglia_bianco.py --dry-run        # mostra cosa farebbe
python3 ritaglia_bianco.py imgs/gantt       # ritaglia (tiene una copia degli originali)
```

Richiede `Pillow` e `numpy`.
