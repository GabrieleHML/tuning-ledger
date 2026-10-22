# Tuning Ledger — Note del relatore

## Slide 1 - Tuning Ledger

Buongiorno professore. Io sono Gabriele Hamil, insieme a me ha lavorato Matteo Stricagnolo, e le presentiamo il progetto che abbiamo sviluppato per il corso di Sistemi Informativi. Si chiama Tuning Ledger. L'idea di partenza è semplice: quando un'auto viene modificata dopo l'immatricolazione, oggi non esiste un modo affidabile per sapere che cosa sia stato fatto davvero. Noi proponiamo un passaporto digitale, che abbiamo chiamato DMVP, registrato su blockchain, che resta legato al veicolo per tutta la sua vita. Nei prossimi venti minuti ripercorriamo il lavoro, dall'analisi del contesto fino alla valutazione economica.

## Slide 2 - Agenda

Questa è la struttura del documento, ed è anche la struttura della presentazione: otto capitoli. I primi due inquadrano il problema e il contesto. Il terzo e il quarto descrivono la soluzione, con gli attori, i ruoli e i processi. Gli ultimi tre valutano l'idea da tre punti di vista diversi: strategico con la SWOT, realizzativo con il Project Plan, economico con il Business Plan.

## Slide 3 - Il problema: una filiera senza un registro condiviso

Partiamo dal problema. Oggi le modifiche a un veicolo vengono documentate con fatture, dichiarazioni di conformità e annotazioni sul libretto. Sono documenti prodotti da soggetti diversi, su supporti diversi, e non c'è niente che ne garantisca l'integrità nel tempo. Nelle sei caselle abbiamo raccolto le conseguenze. Chi compra non può verificare che cosa sia stato fatto. I documenti si possono alterare o retrodatare. Gli enti devono ricostruire la storia a mano. I ricambi non sono tracciati. Le assicurazioni non sanno con precisione che cosa stanno assicurando. E chi ha speso bene non riesce a dimostrarlo alla rivendita. In fondo alla slide abbiamo messo la causa comune: manca una fonte informativa unica e non alterabile.

## Slide 4 - La risposta: il Digital Modified Vehicle Passport

La risposta è il Digital Modified Vehicle Passport, il DMVP. È un passaporto digitale legato al numero di telaio, che accompagna il veicolo per tutta la vita. Nei due riquadri in alto a destra ci sono le informazioni che contiene: da una parte le lavorazioni eseguite, con i codici seriali dei componenti installati; dall'altra l'esito dei controlli del centro di certificazione. Sotto abbiamo elencato che cosa cambia rispetto a oggi: ogni attore scrive solo per la parte che gli compete, gli altri leggono in base ai permessi che hanno, nessuno può modificare quello che è già stato registrato, e il passaporto si trasferisce insieme al veicolo.

## Slide 5 - Le tre scelte tecnologiche

Le scelte tecnologiche sono tre, quelle nei riquadri in alto. La blockchain è permissioned: entrano solo soggetti che sono stati verificati. L'architettura è ibrida: sulla catena registriamo soltanto l'hash, mentre foto, PDF e schede tecniche restano in un database esterno. E gli smart contract validano in automatico le condizioni. Nella riga sotto abbiamo messo il perché delle alternative scartate. Una blockchain pubblica è tecnicamente possibile, ci sono proposte che tokenizzano il veicolo come NFT, ma i costi e la scalabilità non reggono. Una privata toglie proprio la garanzia che ci serve. Nel riquadro in oro, invece, i riferimenti esistenti: Hyperledger Fabric è già usata nell'automotive.

## Slide 6 - Contesto e scenario specifico

Passiamo all'analisi del contesto. Abbiamo usato GOREM in due passaggi: prima uno sguardo largo, su tutti i soggetti che ruotano attorno al tuning, poi la restrizione ai soli attori che useranno davvero la piattaforma.

## Slide 7 - Stakeholder Diagram

Questo è lo Stakeholder Diagram. In alto la radice. Collegato direttamente a essa c'è l'Intermediario, che fornisce e gestisce la piattaforma e per questo opera trasversalmente rispetto alla filiera. Accanto ci sono le sei categorie, che abbiamo riportato anche nella riga in fondo, e all'ultimo livello i sedici attori concreti. Le categorie raggruppano i soggetti per la funzione che svolgono nella filiera: gli utenti finali, privati e aziende con flotte; gli operatori tecnici, cioè aziende di tuning e officine; gli attori commerciali, dalla casa automobilistica alla concessionaria fino alle aziende di spedizione; le assicurazioni con i periti; gli enti di certificazione accreditati, che eseguono le verifiche tecniche; e le autorità pubbliche, che fissano le regole e vigilano sulla circolazione. In questa fase l'analisi è volutamente larga: ci sono anche soggetti che sulla piattaforma non entreranno mai.

## Slide 8 - Softgoal Diagram

Qui ci sono i softgoal, cioè gli obiettivi non funzionali: le qualità che il sistema deve avere. In cima la radice, la certificazione digitale affidabile delle modifiche ai veicoli. Sotto, cinque softgoal per ciascuno stakeholder, trentacinque in totale. Per esempio l'utente finale si aspetta trasparenza, autenticità e protezione dei dati; l'Intermediario affidabilità, sicurezza degli accessi e costi sostenibili; l'ente di certificazione integrità dei dati e verifiche ripetibili; l'autorità pubblica controlli rapidi e sicurezza della circolazione. Come scritto nel riquadro a destra, un softgoal non è mai raggiunto o non raggiunto: si persegue quanto basta.

## Slide 9 - Softgoal Dependency Diagram

In questo diagramma le frecce tratteggiate indicano come i softgoal si influenzano tra loro: il più è un rinforzo, il meno un ostacolo. Il risultato è riassunto nei due riquadri a destra. In alto: trenta relazioni su trentatré sono positive, quindi gli interessi dei vari attori vanno quasi tutti nella stessa direzione. In basso i tre conflitti. Due esprimono la stessa tensione: più lo storico è aperto, più si espongono dati riservati. Non la risolviamo scegliendo un lato, la gestiamo con permessi diversi a seconda del ruolo. Il terzo riguarda l'Intermediario, che deve bilanciare l'affidabilità della piattaforma con il costo dell'infrastruttura che la sostiene.

## Slide 10 - Cinque attori sulla piattaforma, quattro partner al contorno

Adesso stringiamo il campo. Di tutti quegli stakeholder, solo cinque interagiscono direttamente con la piattaforma, e accanto a ognuno abbiamo scritto il motivo per cui dovrebbe aderire. Il primo è l'Intermediario: è chi sviluppa e gestisce il sistema, ed è il nostro cliente primario, quello che lo acquista. Poi ci sono concessionaria, azienda di tuning, centro di certificazione e cliente finale. Nella colonna a destra i quattro partner, dalla Motorizzazione ai fornitori: il sistema si interfaccia con loro, ma non scrivono sul registro.

## Slide 11 - Role Diagram

Il Role Diagram scompone ogni attore nei ruoli che assume: sono le frecce «plays» che si vedono nel disegno. L'elenco a destra le riassume. L'Intermediario ne ha tre: amministra la rete, gestisce le identità e fa assistenza. Concessionaria e centro di certificazione ne hanno due ciascuno, e nel caso del centro la divisione è voluta: chi ispeziona e chi firma il certificato sono due momenti distinti. In tutto dieci ruoli, e a ognuno corrisponde un goal.

## Slide 12 - Goal Diagram

Stesso impianto della slide precedente, ma qui a ogni ruolo abbiamo agganciato il suo obiettivo, nei riquadri esterni. Un ruolo, un goal. Se li leggiamo in sequenza otteniamo già il ciclo di vita del passaporto: creazione, registrazione delle modifiche, collaudo, certificazione, consegna. La differenza rispetto ai softgoal è che qui la verifica è binaria: il goal o è raggiunto o non lo è.

## Slide 13 - Goal Dependency Diagram

Qui vediamo come i goal si condizionano a vicenda. A sinistra le otto relazioni positive: lette in fila descrivono esattamente il flusso, ogni obiettivo abilita il successivo. A destra i tre punti di attrito, che sono quelli da tenere presenti in esercizio: più il sistema viene usato, più pesa l'infrastruttura; più attori entrano, più cresce il lavoro di assistenza; e un collaudo fatto con rigore allunga i tempi di consegna.

## Slide 14 - Business Model Canvas

Questo è il Business Model Canvas. La scelta di fondo è nel primo riquadro a destra: il cliente primario è l'Intermediario, non l'officina e non il cliente finale. È lui che acquista la piattaforma e la porta agli altri. Nel riquadro centrale del canvas il valore offerto è diviso per segmento, così ogni attore ha il suo motivo per entrare. Sotto ci sono i flussi di ricavo: nel Business Plan abbiamo contabilizzato solo abbonamento e verticalizzazioni, gli altri li abbiamo lasciati fuori per prudenza.

## Slide 15 - Use-case e processi

Con il capitolo quattro entriamo nel funzionamento: prima i casi d'uso, che dicono chi fa che cosa, poi i processi in BPMN, che mostrano come le attività si concatenano nel tempo.

## Slide 16 - Concessionaria e Azienda di Tuning

Prima una convenzione che vale per tutti i diagrammi, quella nel riquadro in alto: ogni operazione che scrive sul registro è modellata come «include» e coinvolge l'Intermediario come attore secondario, perché è l'unico che può operare sulla blockchain. A sinistra la concessionaria: registra il veicolo base, e questa operazione crea il passaporto; poi avvia la consegna. A destra l'azienda di tuning, un solo ruolo ma tre azioni incluse: la scheda tecnica con i seriali, le prove multimediali e l'ancoraggio dell'hash.

## Slide 17 - Centro di Certificazione e Cliente Privato

A sinistra il centro di certificazione. L'ispettore, prima di collaudare, consulta lo storico del passaporto per verificare che le fasi precedenti siano in regola. Da qui parte l'unico «extend» di tutta la modellazione: il ramo della non conformità, che scatta se il collaudo va male. L'emittente invece rilascia il certificato e lo registra. A destra il cliente privato: consulta lo storico in sola lettura, e quando accetta il veicolo l'operazione include il passaggio di proprietà del DMVP.

## Slide 18 - Intermediario, gestore della piattaforma

L'Intermediario gioca tre ruoli, elencati a destra: amministra l'infrastruttura, gestisce le identità e fornisce assistenza. Il secondo è quello su cui vale la pena fermarsi, perché è lì che si decide chi può scrivere sul registro. L'immutabilità garantisce che il dato non cambi, non che sia vero; è l'onboarding a garantirne la provenienza. Il terzo ruolo, l'assistenza, nel diagramma ha quattro frecce in entrata, una per ogni altro attore.

## Slide 19 - Processo complessivo di gestione del DMVP

Questo è il processo completo, dalla richiesta del cliente fino al passaggio di proprietà. È una coreografia: ogni attività appartiene a un partecipante e si rivolge agli altri. La fascia centrale si legge da sinistra a destra ed è divisa nelle quattro fasi che abbiamo riassunto in basso. Sotto ogni blocco c'è una banda grigia con scritto Intermediario: è lui che effettua la scrittura. Al centro i due archivi separati, il database off-chain sopra e la blockchain sotto. E poi il rombo con la X, il gateway che valuta l'esito del collaudo: se è negativo la pratica torna all'azienda di tuning.

## Slide 20 - Esecuzione del tuning e registrazione delle modifiche

Questo è il sotto-processo del tuning vero e proprio. Subito dopo l'evento di inizio c'è il rombo con il più: è un gateway parallelo, apre due rami che procedono insieme. Nel ramo in alto l'officina lavora fisicamente sull'auto; nel ramo in basso registra sul sistema le specifiche, i seriali dei componenti e la documentazione. Seguendo il ramo basso si vede che i dati vanno nel database off-chain e in parallelo l'hash finisce sulla blockchain. I due rami si richiudono nel secondo rombo, e parte la notifica al centro di certificazione.

## Slide 21 - Ispezione e certificazione

Ultimo processo. Il centro di certificazione riceve il veicolo e come prima attività consulta lo storico del passaporto. Poi esegue le verifiche. Al centro il rombo con la X apre i due esiti descritti in basso. Il ramo che scende è quello negativo: si genera un report di anomalia e si chiude con un messaggio che rimanda la pratica all'officina. Il ramo che prosegue a destra è quello positivo: il certificato viene archiviato, il suo hash registrato, e lo stato del DMVP passa a «Certificato e conforme».

## Slide 22 - Fattibilità strategica, realizzativa ed economica

L'ultima parte risponde a tre domande: la SWOT se l'idea ha senso, il Project Plan se è realizzabile e con quali risorse, il Business Plan se l'investimento rientra.

## Slide 23 - Valutazione strategica dell'iniziativa

A sinistra la SWOT completa: quattro punti di forza, quattro debolezze, tre opportunità e tre minacce. A destra abbiamo estratto il fattore che pesa di più in ogni quadrante. La forza è l'immutabilità, che elimina tecnicamente la falsificazione. La debolezza è la massa critica: se il centro di certificazione non partecipa, il passaporto resta incompleto. L'opportunità è la domanda crescente di trasparenza. La minaccia è il mancato riconoscimento da parte degli enti. Come si legge in fondo, debolezza e minaccia si affrontano con la stessa leva: le collaborazioni.

## Slide 24 - Sei anni, due fasi

Il piano copre sei anni, dal 2026 al 2031. Nel GANTT la prima barra è l'anno di sviluppo, le cinque sotto sono gli anni di esercizio. In totale sono quasi quarantasette Anni-Persona, con un organico di dodici persone durante lo sviluppo che scende a otto in esercizio. Un parametro che usiamo in tutto il piano: un Anno-Persona corrisponde a 1752 ore, cioè 219 giornate da otto ore; uno sprint di due settimane sono 73 ore a persona.

## Slide 25 - Architettura a micro-servizi

L'architettura è a micro-servizi. Il diagramma si legge a fasce. In alto il front-end unificato: una sola applicazione multi-ruolo, dove la differenza tra utente business e cliente finale la fa il profilo di autenticazione. Nella fascia centrale i tre sottosistemi verticali, uno per attore. Sotto, in verde, il Back-Office: è il motore del sistema ed è l'unico livello autorizzato a invocare il chaincode. In fondo la persistenza, con la rete Fabric da un lato e database e object storage dall'altro. A destra il riepilogo dei cinque sottosistemi.

## Slide 26 - Distribuzione e tecnologie

Qui vediamo dove i componenti vengono collocati fisicamente. In alto i dispositivi degli utenti, al centro a sinistra il cluster applicativo sul cloud, a destra la rete Hyperledger Fabric. Il punto più importante è il secondo riquadro a destra: ogni organizzazione mantiene un proprio peer con la sua copia del ledger, ed è questo che rende impossibile a un singolo attore modificare i dati. In fondo, su una riga sola, lo stack di sviluppo che abbiamo scelto.

## Slide 27 - Fase 1 — Sviluppo della piattaforma

Il GANTT della prima fase copre le quarantotto settimane dell'Anno 0: le colonne sono i dodici mesi, ognuno diviso in due sprint da due settimane. Le prime righe in alto sono l'organizzazione del progetto. Al centro si vedono tre blocchi di colore che corrono in parallelo: sono i tre gruppi che lavorano contemporaneamente sui rispettivi sottosistemi. In fondo le ultime due righe, integrazione, testing e deployment. Il sottosistema più pesante è il Back-Office, con oltre cinquemila ore. Abbiamo adottato Scrum con sprint di due settimane: il project manager fa da Product Owner, l'architetto da Scrum Master.

## Slide 28 - Fase 2 — Esercizio e mantenimento

La seconda fase copre cinque anni, venti trimestri, e la squadra scende da dodici a otto persone. Le attività sono cinque, descritte in basso. Guardando la terza riga del GANTT, la manutenzione evolutiva è vuota per i primi due anni e parte solo dall'anno tre: all'inizio le risorse servono a stabilizzare la rete e ad acquisire i primi clienti. L'ultima riga invece è costante, perché l'analisi dei dati gira sempre allo stesso ritmo.

## Slide 29 - Risorse umane sui sei anni

Questa tabella chiude il Project Plan. Le colonne sono i sei anni, le righe le quattro figure professionali. Seguendo la riga del totale si vede il salto tra l'anno zero e gli anni successivi: da 11,75 Anni-Persona si passa a 7 all'anno, per un totale di 46,75. Il motivo è nei due riquadri sotto: in sviluppo serve gente per lavorare in parallelo, in esercizio il lavoro cambia natura. Questi numeri sono la base di calcolo del Business Plan.

## Slide 30 - Costi della Fase 1 e capitale investito

Passiamo ai costi. La tabella a sinistra riguarda l'anno zero. La voce principale è il personale, 456 mila euro: l'abbiamo ottenuta moltiplicando gli Anni-Persona per il costo aziendale di ogni figura, cioè la RAL su tredici mensilità più TFR e contributi a carico dell'azienda. Le spese generali sono stimate forfettariamente al venti per cento. Il totale è 599 mila euro; aggiungendo il dodici per cento di oneri finanziari, il capitale investito arriva a 671 mila, il riquadro in oro. Lo ammortizziamo in cinque rate da 134 mila euro.

## Slide 31 - Ricavi della Fase 2

I ricavi si basano sulle tre ipotesi in basso: un abbonamento fisso di trentamila euro l'anno per intermediario, un prezzo per verticalizzazione che scende nel tempo, e una crescita da dieci clienti nel primo anno a quaranta nel quinto. La riga in oro è il ricavo totale: si parte da quattrocentomila euro e si arriva a un milione e mezzo. Nella nota in fondo abbiamo precisato che la fee per ogni passaporto registrato e il marketplace non sono conteggiati, quindi la stima è prudenziale.

## Slide 32 - Costi, imposte e risultato netto della Fase 2

Qui costi e ricavi si incontrano. Nella parte alta i costi di esercizio, circa 482 mila euro l'anno, che comprendono anche la rata di ammortamento. Poi due tipi di oneri finanziari: quelli sul finanziamento iniziale, che calano ogni anno, e quelli sul disavanzo, che compaiono solo negli anni due e tre, quando la cassa è ancora negativa. Sotto si tolgono IRES e IRAP. La riga che conta è l'ultima, il risultato cumulato: parte da meno 172 mila, resta negativo il secondo anno e diventa positivo al terzo.

## Slide 33 - Break Even Point e ROI

Il grafico riassume i cinque anni. Le barre blu sono i ricavi, quelle in oro i costi: si incrociano tra il secondo e il terzo anno. La linea scura è il risultato cumulato ed è quella da seguire: parte sotto lo zero e taglia l'asse all'anno tre. Quello è il Break Even Point. A fine quinquennio il cumulato è di un milione e 74 mila euro su 671 mila investiti: un ROI del 160 per cento, cioè un rendimento medio del dodici per cento l'anno. Nella nota in fondo segnaliamo che al terzo anno il pareggio si raggiunge per circa sedicimila euro, quindi con un margine stretto.

## Slide 34 - Che cosa abbiamo ottenuto e dove può andare

Chiudiamo con due colonne. A sinistra quello che il sistema porta: informazioni che non si possono alterare, una prova documentale per chi esegue le lavorazioni, collaudi più rapidi e un veicolo che alla rivendita mantiene il suo valore. A destra le direzioni di sviluppo: il modello si applica al retrofit elettrico, alle auto storiche e alle flotte; poi c'è il riconoscimento formale da parte degli enti e l'aggancio ai passaporti digitali di prodotto europei. In fondo abbiamo messo la condizione di successo: non è tecnica, è la capacità di portare abbastanza attori dentro al registro.

## Slide 35 - Grazie per l'attenzione

Questo è quanto. Tre numeri per riassumere: quasi quarantasette Anni-Persona di lavoro su sei anni, pareggio al terzo anno di esercizio, e un ROI del centosessanta per cento sul quinquennio. Grazie per l'attenzione, restiamo a disposizione per le domande.
