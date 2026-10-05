# 🧹 Pulizia Ubuntu

<div align="center">

![Anteprima](https://raw.githubusercontent.com/coding4u-it/pulizia-ubuntu/main/screenshot.png)

[![Version](https://img.shields.io/badge/version-5.0-blue)](https://github.com/coding4u-it/pulizia-ubuntu/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/coding4u-it/pulizia-ubuntu/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-Ubuntu-orange)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)

**Applicazione grafica per la manutenzione e la pulizia di Ubuntu**

*22 operazioni di pulizia, 5 temi, multilingua IT/EN, schedulazione automatica*

</div>

---

## ✨ Funzionalità

### 🌐 Browser
- Pulizia cache di **Chrome, Chromium, Edge, Firefox, Brave, Opera** (selezionabili singolarmente)

### ⚙️ Sistema
- Rimozione pacchetti orfani (`apt autoremove`)
- Pulizia cache APT
- Pulizia log systemd (mantiene ultimi 3 giorni)
- Rimozione vecchie revisioni Snap
- Pulizia file temporanei (`/tmp`, `/var/tmp`)
- Pulizia anteprime (thumbnails)
- Svuotamento cestino
- Pulizia config orfane (`apt purge rc`)
- Pulizia file recenti (`recently-used`)

### 💻 Sviluppatori
- Pulizia cache **pip, npm, yarn, cargo, gem, composer, go**

### 🎬 Multimedia
- Pulizia cache **Thunderbird, Spotify, VLC, MPV, Rhythmbox, digiKam, Shotwell, gThumb, Cheese**

### 🎮 Gaming
- Pulizia cache **Steam** (shader, download, log)

### 🚀 Avanzate
- Rimozione librerie orfane (`deborphan`)
- Rigenerazione liste APT
- Pulizia runtime **Flatpak**
- Pulizia **Docker** (container, immagini, volumi, reti)
- Esecuzione **TRIM SSD**
- Rimozione **vecchi kernel**
- Rimozione **link simbolici rotti**
- Rimozione **cartelle vuote**

### 🛠 Strumenti integrati
- 📊 **Analisi spazio disco** interattiva
- 📈 **Statistiche storiche** con grafico dell'andamento
- ⏱ **Schedulazione cron** con controllo servizio
- 🔐 **Shred** per cancellazione sicura (1-35 passaggi)
- 📖 **Guida in linea** (F1)
- 🎨 **5 temi**: dark, light, nord, dracula, solarized

### 🌍 Multilingua
- Italiano 🇮🇹
- English 🇬🇧

### 📊 Report e notifiche
- Report dettagliato nella finestra finale
- Notifica desktop al termine
- Grafico spazio disco prima/dopo
- Salvataggio/copia report

---

## 🚀 Installazione

### Da pacchetto `.deb` (consigliato)

```bash
# Scarica l'ultima release
wget https://github.com/coding4u-it/pulizia-ubuntu/releases/latest/download/pulizia-ubuntu-5.0.deb

# Installa (con gdebi per risolvere dipendenze)
sudo apt install gdebi -y
sudo gdebi pulizia-ubuntu-5.0.deb

# Avvia dal menu applicazioni o da terminale
pulizia-ubuntu
```

### Da sorgente

```bash
# Clona il repository
git clone https://github.com/coding4u-it/pulizia-ubuntu.git
cd pulizia-ubuntu

# Installa le dipendenze
sudo apt install python3-tk python3-pil python3-matplotlib libnotify-bin -y

# Avvia l'applicazione
python3 usr/share/pulizia-ubuntu/pulizia_gui.py
```

---

## 📸 Screenshot

### Tema scuro (default)
![Screenshot tema scuro](screenshot.png)

### Temi disponibili
- 🎨 **dark** — Default, elegante
- ☀️ **light** — Chiaro, per ambienti luminosi
- ❄️ **nord** — Blu notte, riposante
- 🧛 **dracula** — Contrastato, vivace
- 🌅 **solarized** — Classico, basso contrasto

---

## 🛠 Requisiti

- **Ubuntu** 22.04 LTS o superiore (testato su 26.04)
- **Python** 3.10+
- **Dipendenze**:
  - `python3-tk` — interfaccia grafica
  - `python3-pil` — gestione icone
  - `python3-matplotlib` — grafico spazio disco
  - `libnotify-bin` — notifiche desktop

### Dipendenze opzionali

```bash
# Per abilitare funzionalità extra:
sudo apt install deborphan -y      # Rimozione librerie orfane
sudo apt install cron -y            # Schedulazione automatica
sudo apt install docker.io -y       # Pulizia Docker
sudo apt install flatpak -y         # Pulizia runtime Flatpak
sudo apt install fdupes -y          # (futuro) Ricerca duplicati
```

---

## 📖 Utilizzo

### 1. Avvia l'app

Dal menu applicazioni cerca **"Pulizia Ubuntu"** oppure:

```bash
pulizia-ubuntu
```

### 2. Seleziona le opzioni

Le opzioni sono organizzate in 3 gruppi collassabili:
- 🌐 **Browser** — quali browser pulire
- ⚙️ **Sistema** — operazioni di base
- 🚀 **Avanzate** — operazioni rischiose

### 3. Esegui pulizia

Clicca **▶ Esegui Pulizia** e inserisci la password sudo quando richiesto.

### 4. Visualizza il report

Al termine si apre una finestra con:
- Grafico spazio liberato
- Report completo
- Pulsanti Salva/Copia

---

## 🎯 Menu Strumenti

Dal menu **🔧 Strumenti ▼** puoi accedere a:

| Strumento | Descrizione |
|-----------|-------------|
| ⏱ **Schedulazione** | Programma pulizie automatiche via cron |
| 📊 **Analisi disco** | Mostra directory più pesanti |
| 📈 **Statistiche** | Storico pulizie con grafico |
| 🔐 **Shred** | Cancellazione sicura irreversibile |

---

## 🎨 Cambio tema

In alto a destra c'è il selettore tema. La scelta viene salvata e ricordata al prossimo avvio.

**File di preferenze**: `~/.config/pulizia-ubuntu/settings.json`

```json
{
  "lang": "it",
  "theme": "dark"
}
```

---

## ⏱ Schedulazione automatica

Il pulsante **Schedulazione** permette di:

- 🟢 **Abilitare/disabilitare** il servizio cron
- 📅 **Configurare** frequenza (giornaliera/settimanale/mensile)
- 🕐 **Scegliere ora e giorno**
- 🗑 **Rimuovere** la schedulazione

**File installati**:
- `/usr/local/bin/pulizia_ubuntu_cron.sh` — script
- `/etc/cron.d/pulizia-ubuntu` — voce cron
- `/var/log/pulizia_ubuntu.log` — log esecuzioni

---

## 📊 Statistiche

Le statistiche sono salvate in:
```
~/.local/share/pulizia-ubuntu/stats.json
```

Il grafico mostra l'andamento dello spazio liberato nel tempo (ultime 20 pulizie).

---

## 🔐 Shred (cancellazione sicura)

Lo strumento Shred permette di cancellare **irreversibilmente** file o directory:

- **Passaggi configurabili**: 1-35 (default 3)
- **Passaggio zero**: aggiunge zeri finali per nascondere shred
- **Rimozione automatica**: elimina i file dopo sovrascrittura
- **Conferma esplicita**: richiede conferma prima di procedere

> ⚠️ **Attenzione**: operazione **irreversibile**.
> 
> Non garantito al 100% su SSD (usare cifratura disco LUKS per sicurezza massima).

---

## 🌍 Lingue

Cambia lingua dal menu in alto a destra. Supportate:
- 🇮🇹 Italiano
- 🇬🇧 English

La lingua viene anche rilevata automaticamente dall'ambiente (`LANG`).

---

## 🤝 Contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida.

---

## 📝 Changelog

Vedi [CHANGELOG.md](CHANGELOG.md) per la storia delle versioni.

### v5.0 (2026-10-05)
- 💻 Pulizia cache sviluppatori (pip, npm, yarn, cargo, gem, composer, go)
- 🎬 Pulizia cache multimedia (Thunderbird, Spotify, VLC, ...)
- 🎮 Pulizia cache Steam
- 🔗 Rimozione link simbolici rotti
- 🗂 Rimozione cartelle vuote

### v4.2 (2026-10-01)
- GUI compatta, report solo nella finestra finale
- Menu Strumenti a tendina
- Gruppi opzioni collassabili

### v4.0 (2026-10-01)
- Riorganizzazione GUI
- 5 temi (dark, light, nord, dracula, solarized)

### v3.0 (2026-10-01)
- Flatpak, Docker, TRIM SSD
- Shred (v3.1)

### v2.0 (2026-09-25)
- i18n IT/EN, grafico disco, icona personalizzata

### v1.0 (2026-09-20)
- Prima versione con pulizia base

---

## 📄 Licenza

Distribuito sotto licenza **MIT**. Vedi [LICENSE](LICENSE) per i dettagli.

---

## 👤 Autore

**coding4u-it**

- 🐙 GitHub: [@coding4u-it](https://github.com/coding4u-it)
- 📦 Repository: [pulizia-ubuntu](https://github.com/coding4u-it/pulizia-ubuntu)

---

<div align="center">

**⭐ Se ti piace questo progetto, lascia una stella su GitHub! ⭐**

[🐛 Segnala un bug](https://github.com/coding4u-it/pulizia-ubuntu/issues/new)
·
[💡 Proponi una funzionalità](https://github.com/coding4u-it/pulizia-ubuntu/issues/new)
·
[📥 Scarica l'ultima release](https://github.com/coding4u-it/pulizia-ubuntu/releases/latest)

</div>
