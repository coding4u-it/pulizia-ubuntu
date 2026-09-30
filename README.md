# 🧹 Pulizia Ubuntu

<div align="center">

![Version](https://img.shields.io/badge/version-2.3-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Ubuntu-orange)

**Applicazione grafica per la manutenzione e la pulizia di Ubuntu**

</div>

## ✨ Funzionalità

| Funzione | Descrizione |
|----------|-------------|
| 🧹 Pulizia APT | Rimuove pacchetti orfani e cache |
| 🌐 Cache Browser | Chrome, Chromium, Edge, Firefox, Brave, Opera |
| 🗑 Cestino | Svuota il cestino dell'utente e di root |
| 🔧 Kernel | Rimuove i vecchi kernel in sicurezza |
| 📊 Analisi Disco | Mostra le directory più pesanti |
| ⏱ Schedulazione | Pulizia automatica via cron |
| 🌍 Lingua | Supporto Italiano / Inglese |

## 🚀 Installazione

```bash
# Clona il repository
git clone https://github.com/coding4u-it/pulizia-ubuntu.git
cd pulizia-ubuntu

# Installa le dipendenze
sudo apt install python3-tk python3-pil python3-matplotlib libnotify-bin

# Avvia l'applicazione
python3 pulizia_gui.py
