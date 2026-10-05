# Changelog

Tutte le modifiche importanti di questo progetto sono documentate qui.
Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.0.0/).

## [5.0] - 2026-10-05

### Aggiunto
- 💻 Pulizia cache sviluppatori (pip, npm, yarn, cargo, gem, composer, go)
- 🎬 Pulizia cache multimedia (Thunderbird, Spotify, VLC, MPV, ...)
- 🎮 Pulizia cache Steam (shader, download, log)
- 🔗 Rimozione link simbolici rotti
- 🗂 Rimozione cartelle vuote (escluse quelle di sistema)
- 22 operazioni di pulizia totali

### Sicurezza
- Steam e cartelle vuote disattivati di default
- Cartelle vuote escludono directory di sistema

## [4.2] - 2026-10-01

### Modificato
- GUI principale compatta (rimosso report interno)
- Report spostato solo nella finestra finale unificata
- Menu "Strumenti" a tendina (Schedula, Analisi, Statistiche, Shred)
- Opzioni organizzate in 3 gruppi collassabili (Browser, Sistema, Avanzate)

### Rimosso
- Popup separato di fine pulizia
- Grafico in finestra separata
- Report dalla finestra principale
- Finestra finale unificata con grafico + report

## [4.0] - 2026-10-01

### Modificato
- Riorganizzazione GUI: toolbar compatta e gruppi di opzioni

## [3.1] - 2026-10-01

### Aggiunto
- 🔐 Strumento Shred per cancellazione sicura
  - Supporto file singolo e directory complete
  - Configurabile (1-35 passaggi, zero, rimozione)
  - Log dettagliato in tempo reale
  - Notifica desktop al termine
- 17 operazioni di pulizia + Shred

### Note
- Shred è IRREVERSIBILE (conferma esplicita richiesta)
- Non garantito su SSD (usare LUKS per sicurezza massima)

## [3.0] - 2026-10-01

### Aggiunto
- 📦 Pulizia runtime Flatpak inutilizzati
- 🐳 Pulizia Docker (container, immagini, volumi, reti)
- ⚡ Esecuzione TRIM su SSD
- 🗑 Pulizia file recently-used
- 17 operazioni di pulizia totali

### Sicurezza
- Docker e TRIM disattivati di default
- Ogni operazione controlla la disponibilità della dipendenza

## [2.7] - 2026-10-01

### Aggiunto
- 🎨 3 nuovi temi: Nord, Dracula, Solarized
- Selettore tema esteso a 5 opzioni
- 🎨 Selettore tema chiaro/scuro
- 💾 Persistenza preferenze in `~/.config/pulizia-ubuntu/settings.json`
- 🔄 Cambio tema istantaneo senza riavviare l'app

### Modificato
- Refactoring colori: uso di `T("chiave")` per temi
- Lingua e tema ora vengono ricordati tra sessioni

## [2.4] - 2026-09-30

### Aggiunto
- 🧹 Pulizia config orfane (`apt purge rc`) — attiva di default
- 📚 Rimozione librerie orfane (`deborphan`) — disattiva di default
- 📥 Rigenerazione liste APT (`/var/lib/apt/lists`) — disattiva di default
- 13 opzioni di pulizia totali

### Modificato
- Report numerato da [1] a [13]
- Ordinamento ottimale: prima libera spazio, poi pulisce residui

## [2.3] - 2026-09-25

### Aggiunto
- 📊 Analisi spazio disco interattiva
- 🗑 Svuotamento cestino
- 🔧 Rimozione vecchi kernel
- 📖 Guida in linea (F1 / Ctrl+H)
- 🌐 Browser selezionabili singolarmente (6 browser)
- ⏱ Schedulazione cron con controllo stato servizio
- 📢 Notifiche desktop
- 📈 Grafico spazio disco prima/dopo
- 🌍 Supporto multilingua IT/EN

## [2.0] - 2026-09-20

### Aggiunto
- 🎨 Icona personalizzata generata con PIL
- 📊 Grafico spazio disco

## [1.3] - 2026-09-18

### Risolto
- 🐛 GUI bloccata durante la pulizia (coda thread-safe)
- 🐛 Autenticazione sudo da GUI senza terminale
- 🐛 Finestra fuori schermo all'avvio

## [1.0] - 2026-09-15

### Aggiunto
- Prima versione con pulizia base (APT, Snap, log, tmp)
- Interfaccia Tkinter
- Report dettagliato
