# 🧹 Ubuntu Cleanup

> 🇮🇹 [Leggi in italiano](README.md)

<div align="center">

![Preview](https://raw.githubusercontent.com/coding4u-it/pulizia-ubuntu/main/screenshot.png)

[![Version](https://img.shields.io/badge/version-5.0-blue)](https://github.com/coding4u-it/pulizia-ubuntu/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/coding4u-it/pulizia-ubuntu/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-Ubuntu-orange)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)

**Graphical application for Ubuntu maintenance and cleanup**

*22 cleanup operations, 5 themes, IT/EN multilingual, automatic scheduling*

</div>

---

## ✨ Features

### 🌐 Browsers
- Cache cleanup for **Chrome, Chromium, Edge, Firefox, Brave, Opera** (individually selectable)

### ⚙️ System
- Remove orphan packages (`apt autoremove`)
- APT cache cleanup
- systemd log cleanup (keeps last 3 days)
- Remove old Snap revisions
- Temporary file cleanup (`/tmp`, `/var/tmp`)
- Thumbnail cleanup
- Empty trash
- Orphan config cleanup (`apt purge rc`)
- Recently-used files cleanup

### 💻 Developers
- Cache cleanup for **pip, npm, yarn, cargo, gem, composer, go**

### 🎬 Multimedia
- Cache cleanup for **Thunderbird, Spotify, VLC, MPV, Rhythmbox, digiKam, Shotwell, gThumb, Cheese**

### 🎮 Gaming
- **Steam** cache cleanup (shader, download, logs)

### 🚀 Advanced
- Remove orphan libraries (`deborphan`)
- Regenerate APT lists
- **Flatpak** runtime cleanup
- **Docker** cleanup (containers, images, volumes, networks)
- **SSD TRIM** execution
- Remove **old kernels**
- Remove **broken symlinks**
- Remove **empty directories**

### 🛠 Built-in tools
- 📊 Interactive **disk space analysis**
- 📈 **Historical statistics** with trend chart
- ⏱ **Cron scheduling** with service status control
- 🔐 **Shred** for secure deletion (1-35 passes)
- 📖 **Online help** (F1)
- 🎨 **5 themes**: dark, light, nord, dracula, solarized

### 🌍 Multilingual
- Italian 🇮🇹
- English 🇬🇧

### 📊 Report and notifications
- Detailed report in the final window
- Desktop notification when done
- Disk space chart before/after
- Save/copy report

---

## 🚀 Installation

### From `.deb` package (recommended)

```bash
# Download the latest release
wget https://github.com/coding4u-it/pulizia-ubuntu/releases/latest/download/pulizia-ubuntu-5.0.deb

# Install (with gdebi to resolve dependencies)
sudo apt install gdebi -y
sudo gdebi pulizia-ubuntu-5.0.deb

# Launch from applications menu or terminal
pulizia-ubuntu
```

### From source

```bash
# Clone the repository
git clone https://github.com/coding4u-it/pulizia-ubuntu.git
cd pulizia-ubuntu

# Install dependencies
sudo apt install python3-tk python3-pil python3-matplotlib libnotify-bin -y

# Launch the application
python3 usr/share/pulizia-ubuntu/pulizia_gui.py
```

---

## 📸 Screenshot

![Screenshot](screenshot.png)

---

## 🛠 Requirements

- **Ubuntu** 22.04 LTS or newer (tested on 26.04)
- **Python** 3.10+
- **Dependencies**:
  - `python3-tk` — graphical interface
  - `python3-pil` — icon management
  - `python3-matplotlib` — disk space chart
  - `libnotify-bin` — desktop notifications

### Optional dependencies

```bash
# To enable extra features:
sudo apt install deborphan -y      # Orphan library removal
sudo apt install cron -y            # Automatic scheduling
sudo apt install docker.io -y       # Docker cleanup
sudo apt install flatpak -y         # Flatpak runtime cleanup
```

---

## 📖 Usage

### 1. Launch the app

Search for **"Ubuntu Cleanup"** in your applications menu or run:

```bash
pulizia-ubuntu
```

### 2. Select options

Options are organized into 3 collapsible groups:
- 🌐 **Browsers** — which browsers to clean
- ⚙️ **System** — basic operations
- 🚀 **Advanced** — risky operations

### 3. Run cleanup

Click **▶ Run Cleanup** and enter the sudo password when prompted.

### 4. View the report

When done, a window opens with:
- Freed space chart
- Complete report
- Save/Copy buttons

---

## 🎯 Tools Menu

From the **🔧 Tools ▼** menu you can access:

| Tool | Description |
|------|-------------|
| ⏱ **Scheduling** | Schedule automatic cleanups via cron |
| 📊 **Disk analysis** | Show heaviest directories |
| 📈 **Statistics** | Cleanup history with chart |
| 🔐 **Shred** | Irreversible secure deletion |

---

## 🎨 Theme switching

The theme selector is in the top-right corner. Available themes:
- 🎨 **dark** — Default, elegant
- ☀️ **light** — Light, for bright environments
- ❄️ **nord** — Night blue, restful
- 🧛 **dracula** — Contrasted, vibrant
- 🌅 **solarized** — Classic, low contrast

Your choice is saved in `~/.config/pulizia-ubuntu/settings.json`:

```json
{
  "lang": "en",
  "theme": "dark"
}
```

---

## ⏱ Automatic scheduling

The **Scheduling** button allows you to:

- 🟢 **Enable/disable** the cron service
- 📅 **Configure** frequency (daily/weekly/monthly)
- 🕐 **Choose hour and day**
- 🗑 **Remove** the schedule

**Installed files**:
- `/usr/local/bin/pulizia_ubuntu_cron.sh` — script
- `/etc/cron.d/pulizia-ubuntu` — cron entry
- `/var/log/pulizia_ubuntu.log` — execution log

---

## 📊 Statistics

Statistics are saved in:
```
~/.local/share/pulizia-ubuntu/stats.json
```

The chart shows the trend of freed space over time (last 20 cleanups).

---

## 🔐 Shred (secure deletion)

The Shred tool allows you to **irreversibly** delete files or directories:

- **Configurable passes**: 1-35 (default 3)
- **Zero pass**: adds final zeros to hide shred
- **Automatic removal**: deletes files after overwrite
- **Explicit confirmation**: requires confirmation before proceeding

> ⚠️ **Warning**: **irreversible** operation.
> 
> Not guaranteed on SSD (use LUKS disk encryption for maximum security).

---

## 🌍 Languages

Change language from the top-right menu. Supported:
- 🇮🇹 Italian
- 🇬🇧 English

Language is also auto-detected from the environment (`LANG`).

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

### v5.0 (2026-10-05)
- 💻 Developer cache cleanup (pip, npm, yarn, cargo, gem, composer, go)
- 🎬 Multimedia cache cleanup (Thunderbird, Spotify, VLC, ...)
- 🎮 Steam cache cleanup
- 🔗 Remove broken symlinks
- 🗂 Remove empty directories

### v4.2 (2026-10-01)
- Compact GUI, report only in final window
- Tools dropdown menu
- Collapsible option groups

### v4.0 (2026-10-01)
- GUI reorganization
- 5 themes (dark, light, nord, dracula, solarized)

### v3.0 (2026-10-01)
- Flatpak, Docker, SSD TRIM
- Shred (v3.1)

### v2.0 (2026-09-25)
- IT/EN i18n, disk chart, custom icon

### v1.0 (2026-09-20)
- First version with basic cleanup

---

## 📄 License

Distributed under **MIT** license. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**coding4u-it**

- 🐙 GitHub: [@coding4u-it](https://github.com/coding4u-it)
- 📦 Repository: [pulizia-ubuntu](https://github.com/coding4u-it/pulizia-ubuntu)

---

<div align="center">

**⭐ If you like this project, leave a star on GitHub! ⭐**

[🐛 Report a bug](https://github.com/coding4u-it/pulizia-ubuntu/issues/new)
·
[💡 Request a feature](https://github.com/coding4u-it/pulizia-ubuntu/issues/new)
·
[📥 Download the latest release](https://github.com/coding4u-it/pulizia-ubuntu/releases/latest)

</div>
