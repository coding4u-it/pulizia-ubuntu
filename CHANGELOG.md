# Changelog

Tutte le modifiche importanti di questo progetto sono documentate qui.
Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.0.0/).

## [2.6] - 2026-10-01

### Aggiunto
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
