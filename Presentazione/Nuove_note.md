# Tuning Ledger — Presentazione

## Slide 1 — Tuning Ledger

Buongiorno professore. Io sono Gabriele Hamil e insieme a Matteo Stricagnolo le presentiamo il progetto sviluppato per il corso di Sistemi Informativi, dal titolo **Tuning Ledger**.

L'idea nasce da un problema molto concreto: quando un veicolo viene modificato dopo l'immatricolazione, oggi non esiste un sistema unico e affidabile che permetta di ricostruirne la storia.

La nostra proposta è un **Digital Modified Vehicle Passport**, o DMVP: un passaporto digitale registrato su blockchain e legato al veicolo per tutta la sua vita.

In questi venti minuti vedremo il problema, la soluzione, il funzionamento del sistema e infine la sua fattibilità tecnica ed economica.

---

## Slide 2 — Agenda

La presentazione segue la struttura del progetto.

Partiremo dal problema e dal contesto, passeremo poi alla soluzione e al funzionamento attraverso attori, ruoli e processi, e concluderemo con le tre valutazioni principali: **SWOT, Project Plan e Business Plan**.

---

## Slide 3 — Il problema

Partiamo dal problema.

Oggi la storia delle modifiche di un veicolo è distribuita tra fatture, dichiarazioni, certificazioni e documentazione prodotta da soggetti diversi.

Manca quindi una fonte informativa unica che garantisca che queste informazioni siano complete e non alterate.

Le conseguenze riguardano tutta la filiera: il cliente non riesce a verificare facilmente la storia del veicolo, gli enti devono ricostruirla manualmente, i componenti non sono sempre tracciabili e anche assicurazioni e rivenditori hanno informazioni incomplete.

Il problema comune è quindi la **mancanza di un registro condiviso e affidabile**.

---

## Slide 4 — Digital Modified Vehicle Passport

La nostra risposta è il **Digital Modified Vehicle Passport**.

Il DMVP è un passaporto digitale associato al numero di telaio, che accompagna il veicolo per tutta la sua vita.

Contiene sia la documentazione relativa alle lavorazioni e ai componenti installati, sia gli esiti dei controlli effettuati dal centro di certificazione.

Il principio fondamentale è che ogni attore inserisce solo le informazioni di propria competenza, mentre i permessi determinano chi può visualizzare i diversi dati.

Una volta registrata un'informazione, questa non può essere modificata e il passaporto segue il veicolo anche in caso di vendita.

---

## Slide 5 — Le scelte tecnologiche

Per realizzare il sistema abbiamo fatto tre scelte principali.

La blockchain è **permissioned**, quindi possono partecipare soltanto soggetti verificati.

L'architettura è **ibrida**: sulla blockchain registriamo gli hash, mentre documenti, fotografie e schede tecniche rimangono in un database esterno.

Infine utilizziamo gli **smart contract** per automatizzare i controlli sulle condizioni previste dal sistema.

Abbiamo escluso una blockchain pubblica per motivi di costi e scalabilità, mentre una blockchain completamente privata non garantirebbe lo stesso livello di condivisione tra gli attori.

Come riferimento tecnologico abbiamo considerato **Hyperledger Fabric**, già utilizzata in ambito automotive.

---

## Slide 6 — Contesto e scenario

Per analizzare il contesto abbiamo utilizzato **GOREM** in due fasi.

Prima abbiamo considerato in maniera ampia tutti i soggetti coinvolti nel mondo del tuning; successivamente abbiamo ristretto l'analisi agli attori che interagiscono direttamente con la piattaforma.

---

## Slide 7 — Stakeholder Diagram

Da questa analisi emerge una filiera composta da diverse categorie di stakeholder.

Abbiamo utenti finali, operatori tecnici, soggetti commerciali, assicurazioni, enti di certificazione e autorità pubbliche.

In totale abbiamo individuato sedici attori concreti.

A questi si aggiunge l'**Intermediario**, che gestisce la piattaforma e costituisce l'elemento trasversale dell'intero sistema.

Questa prima analisi è volutamente ampia: non tutti gli stakeholder individuati devono necessariamente scrivere sulla piattaforma.

---

## Slide 8 — Softgoal Diagram

Passiamo agli obiettivi non funzionali, cioè alle qualità che il sistema deve garantire.

L'obiettivo generale è ottenere una **certificazione digitale affidabile delle modifiche ai veicoli**.

Da questo derivano esigenze diverse per i vari stakeholder: trasparenza e autenticità per il cliente, sicurezza e sostenibilità dei costi per l'Intermediario, integrità dei dati per il centro di certificazione e rapidità dei controlli per le autorità.

Sono softgoal, quindi non rappresentano condizioni semplicemente raggiunte o non raggiunte, ma qualità che il sistema deve perseguire.

---

## Slide 9 — Softgoal Dependency Diagram

Analizzando le relazioni tra questi obiettivi emerge un quadro prevalentemente positivo: la maggior parte dei softgoal si rafforza reciprocamente.

I principali conflitti riguardano invece la **trasparenza rispetto alla riservatezza**: rendere disponibile più storico può significare esporre più informazioni sensibili.

La soluzione è una gestione dei permessi differenziata in base al ruolo.

Un secondo equilibrio riguarda l'Intermediario, che deve garantire affidabilità e sicurezza mantenendo però sotto controllo i costi dell'infrastruttura.

---

## Slide 10 — Attori della piattaforma

A questo punto restringiamo il perimetro.

Dei numerosi stakeholder individuati, **cinque interagiscono direttamente con la piattaforma**: Intermediario, concessionaria, azienda di tuning, centro di certificazione e cliente finale.

Accanto a questi abbiamo quattro partner esterni, tra cui Motorizzazione e fornitori, che possono essere integrati con il sistema ma non scrivono direttamente sul registro.

L'Intermediario è il nostro **cliente primario**, perché è il soggetto che acquista e gestisce la piattaforma.

---

## Slide 11 — Role Diagram

Ogni attore può assumere uno o più ruoli.

L'Intermediario, per esempio, amministra la rete, gestisce le identità e fornisce assistenza.

Concessionaria e centro di certificazione hanno invece ruoli specifici legati alla registrazione e alla verifica del veicolo.

In totale abbiamo individuato dieci ruoli, ciascuno associato a uno specifico obiettivo.

---

## Slide 12 — Goal Diagram

Collegando ogni ruolo al proprio obiettivo possiamo già ricostruire il ciclo di vita del passaporto.

Si parte dalla creazione del DMVP, si registrano le modifiche, si effettua il collaudo, viene emessa la certificazione e infine il passaporto viene trasferito insieme al veicolo.

A differenza dei softgoal, qui parliamo di **goal verificabili**: l'obiettivo è raggiunto oppure non è raggiunto.

---

## Slide 13 — Goal Dependency Diagram

Le dipendenze tra i goal descrivono sostanzialmente il flusso operativo del sistema.

Ogni obiettivo abilita quello successivo.

Emergono però anche alcuni punti di attenzione: aumentando l'utilizzo cresce il carico sull'infrastruttura, aumentando gli attori cresce il lavoro di assistenza e controlli più rigorosi possono aumentare i tempi necessari per la consegna del veicolo.

---

## Slide 14 — Business Model Canvas

Passiamo al modello di business.

La scelta centrale è identificare l'**Intermediario come cliente primario**.

È lui ad acquistare la piattaforma e a renderla disponibile agli altri soggetti della filiera.

Il valore offerto cambia invece in base al segmento: per il cliente è soprattutto trasparenza, per le aziende tracciabilità e per gli enti una gestione più affidabile delle informazioni.

Per i ricavi abbiamo considerato principalmente **abbonamenti e verticalizzazioni**, mantenendo una stima prudenziale ed escludendo altre possibili fonti.

---

## Slide 15 — Use case e processi

A questo punto passiamo dal modello concettuale al funzionamento vero e proprio.

Prima abbiamo descritto i **casi d'uso**, cioè chi svolge ciascuna attività.

Successivamente li abbiamo trasformati in processi BPMN, per mostrare come le attività si susseguono nel tempo.

---

## Slide 16 — Concessionaria e Azienda di Tuning

La concessionaria registra il veicolo iniziale e questa operazione porta alla creazione del passaporto.

L'azienda di tuning gestisce invece la modifica del veicolo e registra le informazioni necessarie: specifiche tecniche, seriali dei componenti e documentazione.

Ogni operazione che modifica il registro passa dall'Intermediario, che è l'unico soggetto autorizzato a effettuare la scrittura sulla blockchain.

---

## Slide 17 — Centro di Certificazione e Cliente

Il centro di certificazione, prima di eseguire il collaudo, consulta lo storico del passaporto.

Se il collaudo non viene superato, viene generato un report di anomalia e la pratica torna all'azienda di tuning.

Se invece il veicolo è conforme, viene emesso il certificato e il relativo hash viene registrato.

Il cliente finale può consultare lo storico in sola lettura e, al momento dell'acquisto, il DMVP viene trasferito insieme alla proprietà del veicolo.

---

## Slide 18 — Intermediario

L'Intermediario svolge tre funzioni fondamentali: **gestione dell'infrastruttura, gestione delle identità e assistenza**.

La gestione delle identità è particolarmente importante perché determina chi può scrivere sul registro.

Questo permette di distinguere due concetti: la blockchain garantisce che il dato registrato non venga modificato, mentre il processo di onboarding garantisce che quel dato provenga effettivamente da un soggetto autorizzato.

---

## Slide 19 — Processo complessivo

Qui vediamo il processo completo, dalla richiesta iniziale fino al passaggio di proprietà.

Il processo attraversa quattro fasi principali: registrazione del veicolo, esecuzione del tuning, certificazione e consegna.

Un elemento importante è la separazione tra **database off-chain e blockchain**: i documenti rimangono esternamente, mentre sulla blockchain viene registrato il relativo hash.

Il collaudo costituisce il punto decisionale principale: se l'esito è negativo, la pratica torna all'officina; se è positivo, può proseguire.

---

## Slide 20 — Esecuzione del tuning

Nel processo di tuning abbiamo due attività che procedono in parallelo.

Da una parte viene effettuata fisicamente la modifica del veicolo; dall'altra vengono registrate nel sistema le specifiche, i seriali e la documentazione.

La documentazione viene salvata nel database off-chain, mentre il suo hash viene registrato sulla blockchain.

In questo modo possiamo mantenere i dati pesanti fuori dalla blockchain, conservando comunque una prova della loro integrità.

---

## Slide 21 — Ispezione e certificazione

L'ultimo sotto-processo riguarda la certificazione.

Il centro consulta innanzitutto lo storico, esegue le verifiche e poi si arriva a uno dei due possibili esiti.

In caso di non conformità viene generato un report e la pratica torna all'officina.

In caso positivo viene registrato il certificato e il DMVP passa allo stato **“Certificato e conforme”**.

---

## Slide 22 — Fattibilità

A questo punto passiamo alla valutazione complessiva dell'iniziativa.

Abbiamo cercato di rispondere a tre domande: **ha senso strategicamente? È realizzabile? È sostenibile economicamente?**

Per farlo abbiamo utilizzato rispettivamente SWOT, Project Plan e Business Plan.

---

## Slide 23 — SWOT

Dalla SWOT emergono quattro aspetti principali.

Il punto di forza è l'**immutabilità** del registro.

La principale debolezza è invece la necessità di raggiungere una massa critica: senza la partecipazione degli enti di certificazione il passaporto rimane incompleto.

L'opportunità è rappresentata dalla crescente esigenza di trasparenza nella filiera, mentre la principale minaccia è il mancato riconoscimento da parte degli enti.

Per questo la collaborazione tra gli attori è una condizione fondamentale.

---

## Slide 24 — Piano temporale

Il Project Plan copre **sei anni, dal 2026 al 2031**.

Il primo anno è dedicato allo sviluppo della piattaforma, mentre i cinque successivi riguardano esercizio e mantenimento.

Complessivamente abbiamo stimato circa **47 Anni-Persona**, con una squadra più numerosa durante lo sviluppo e più contenuta durante l'esercizio.

Abbiamo utilizzato Scrum con sprint di due settimane.

---

## Slide 25 — Architettura a microservizi

Dal punto di vista architetturale abbiamo scelto un approccio a **microservizi**.

In alto abbiamo un front-end unificato e multi-ruolo.

Al centro ci sono i sottosistemi specifici per gli attori e, sotto, il Back-Office, che rappresenta il motore del sistema ed è l'unico componente autorizzato a interagire direttamente con il chaincode.

Infine abbiamo i due livelli di persistenza: blockchain e storage/database off-chain.

---

## Slide 26 — Distribuzione e tecnologie

La piattaforma viene distribuita su cloud.

Gli utenti accedono al sistema attraverso i propri dispositivi, mentre il cluster applicativo comunica con la rete Hyperledger Fabric.

Un elemento fondamentale è che ogni organizzazione mantiene un proprio **peer con una copia del ledger**.

In questo modo nessun singolo attore può modificare autonomamente lo storico condiviso.

---

## Slide 27 — Fase 1: sviluppo

La prima fase comprende le 48 settimane dell'anno di sviluppo.

I diversi gruppi lavorano in parallelo sui sottosistemi, mentre le fasi finali sono dedicate a integrazione, testing e deployment.

Il componente più impegnativo in termini di risorse è il Back-Office.

L'organizzazione del lavoro segue Scrum con sprint di due settimane.

---

## Slide 28 — Fase 2: esercizio

La seconda fase comprende i cinque anni successivi.

Il team si riduce progressivamente rispetto alla fase di sviluppo e si concentra soprattutto su gestione della piattaforma, manutenzione, assistenza e analisi dei dati.

La manutenzione evolutiva aumenta solo dopo i primi anni, quando il sistema è stato stabilizzato e la base clienti è cresciuta.

---

## Slide 29 — Risorse umane

Questa tabella riassume le risorse necessarie nei sei anni.

Durante lo sviluppo è necessario un numero maggiore di persone perché le attività procedono in parallelo.

Durante l'esercizio, invece, il fabbisogno si riduce e si stabilizza.

La stima complessiva è di **46,75 Anni-Persona**, ed è proprio questo dato che utilizziamo come base per il calcolo dei costi.

---

## Slide 30 — Costi iniziali

L'investimento iniziale è concentrato nell'anno di sviluppo.

La componente principale è il personale, a cui aggiungiamo le spese generali e gli oneri finanziari.

Il costo complessivo dello sviluppo è di circa **599 mila euro**, mentre considerando gli oneri finanziari il capitale investito raggiunge circa **671 mila euro**.

Questo investimento viene poi ammortizzato nei cinque anni di esercizio.

---

## Slide 31 — Ricavi

Per i ricavi abbiamo formulato tre ipotesi principali.

Un abbonamento annuale di **30 mila euro per intermediario**, un prezzo per le verticalizzazioni che diminuisce nel tempo e una crescita della base clienti da dieci a quaranta intermediari nel corso dei cinque anni.

Con queste ipotesi il ricavo complessivo annuo passa da circa **400 mila a 1,5 milioni di euro**.

Abbiamo inoltre escluso, per prudenza, altre possibili entrate come le fee sui singoli passaporti e il marketplace.

---

## Slide 32 — Costi e risultato

Confrontando ricavi e costi, il risultato cumulato rimane negativo nei primi anni.

Il disavanzo viene progressivamente recuperato grazie alla crescita dei ricavi.

Il risultato cumulato diventa positivo durante il **terzo anno di esercizio**, che rappresenta quindi il momento in cui l'investimento iniziale viene recuperato.

---

## Slide 33 — Break Even e ROI

Il grafico riassume questo andamento.

Ricavi e costi si incontrano tra il secondo e il terzo anno e il risultato cumulato supera lo zero nel terzo anno.

Alla fine dei cinque anni il risultato cumulato stimato è di circa **1,074 milioni di euro**, a fronte di un capitale investito di circa 671 mila euro.

Il Business Plan porta quindi a un **ROI complessivo del 160%** sul quinquennio.

---

## Slide 34 — Risultati e sviluppi futuri

Possiamo quindi riassumere il contributo del progetto in tre aspetti.

Primo, una storia delle modifiche che non può essere alterata.

Secondo, una prova documentale condivisa per tutti gli attori coinvolti.

Terzo, un processo di certificazione più strutturato e facilmente verificabile.

Il modello potrebbe inoltre essere esteso ad altri scenari, come retrofit elettrico, auto storiche e flotte.

La principale condizione per la sua realizzazione non è quindi soltanto tecnologica: è riuscire a coinvolgere un numero sufficiente di attori della filiera.

---

## Slide 35 — Conclusione

Concludiamo con tre numeri che sintetizzano il progetto:

**46,75 Anni-Persona** di lavoro stimati nell'arco di sei anni,

**break even al terzo anno** di esercizio,

e **ROI del 160%** sul quinquennio.

Il punto centrale di Tuning Ledger è quindi utilizzare la blockchain non semplicemente per conservare dati, ma per creare una **fonte condivisa e verificabile della storia delle modifiche di un veicolo**.

Grazie per l'attenzione.
