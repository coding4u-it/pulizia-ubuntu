#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pulizia Ubuntu v2.3 - i18n, icona, grafico, notifiche, cron, guida,
browser selezionabili, cestino, kernel, analisi disco."""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import subprocess, threading, os, shutil, tempfile, glob, queue
from datetime import datetime

APP_NAME = "Pulizia Ubuntu"
APP_VERSION = "2.3"
LOG_FILE = os.path.join(tempfile.gettempdir(), "pulizia_ubuntu_debug.log")

TRANSLATIONS = {
    "it": {
        "app_title": "🧹 Pulizia di Sistema",
        "subtitle": "Ubuntu 26.04 LTS - Manutenzione sicura",
        "options_title": " ⚙️  Opzioni di pulizia ",
        "opt_browser": "Pulizia cache browser (seleziona quali)",
        "opt_snap": "Rimozione vecchie revisioni Snap",
        "opt_tmp": "Pulizia file temporanei (/tmp, /var/tmp)",
        "opt_thumb": "Pulizia anteprime (thumbnails)",
        "opt_trash": "Svuotamento cestino",
        "opt_kernels": "Rimozione vecchi kernel (⚠️ pericoloso)",
        "btn_run": "▶  Esegui Pulizia",
        "btn_schedule": "⏱  Schedula",
        "btn_disk": "📊 Analisi disco",
        "btn_help": "❓  Guida",
        "btn_exit": "✖  Esci",
        "btn_save": "💾 Salva",
        "btn_copy": "📋 Copia",
        "report_label": "📋 Report:",
        "status_ready": "Pronto. Premi 'Esegui Pulizia'.",
        "status_done": "✅ Pulizia completata!",
        "status_error": "❌ Errore durante la pulizia",
        "confirm_title": "Conferma",
        "confirm_msg": "Vuoi avviare la pulizia del sistema?",
        "pwd_title": "🔒 Password amministratore",
        "pwd_msg": "La pulizia richiede privilegi di root.\nInserisci la password:",
        "pwd_key": "🔑",
        "pwd_confirm": "✔  Conferma",
        "pwd_cancel": "✖  Annulla",
        "pwd_wrong_title": "Password errata",
        "pwd_wrong_msg": "Autenticazione fallita.\n\nDettaglio: {0}",
        "pwd_timeout_title": "Timeout",
        "pwd_timeout_msg": "sudo non ha risposto in 15 secondi.",
        "pwd_expired_title": "Sessione scaduta",
        "pwd_expired_msg": "La sessione sudo è scaduta.\nRiavvia la pulizia.",
        "error_title": "Errore",
        "done_title": "Fatto",
        "done_msg": "Pulizia completata!\n\nSpazio liberato: {0}\nSpazio libero: {1}",
        "save_dialog_title": "Salva report",
        "save_ok": "Report salvato in:\n{0}",
        "copy_ok": "Report negli appunti!",
        "exit_title": "Esci",
        "exit_msg": "Chiudere l'applicazione?",
        "exit_running": "Attendi la fine della pulizia.",
        "report_header": "REPORT PULIZIA",
        "initial_free": "Spazio libero iniziale:",
        "final_summary": "RIEPILOGO FINALE",
        "final_free": "Spazio libero finale :",
        "freed_positive": "Spazio liberato      : ✅",
        "freed_zero": "Spazio liberato      : ℹ️  Nessuna variazione",
        "freed_negative": "Variazione           : ⚠️  {0} occupati",
        "completed_at": "Pulizia completata alle",
        "step_autoremove": "[1] Pulizia pacchetti orfani...",
        "step_apt_clean": "[2] Pulizia cache APT...",
        "step_apt_autoclean": "[3] Pulizia cache pacchetti vecchi...",
        "step_journal": "[4] Pulizia log systemd (ultimi 3 giorni)...",
        "step_snap": "[5] Pulizia vecchie revisioni Snap...",
        "step_tmp": "[6] Pulizia file temporanei...",
        "step_browser": "[7] Pulizia cache browser...",
        "step_thumb": "[8] Pulizia anteprime...",
        "step_trash": "[9] Svuotamento cestino...",
        "step_kernels": "[10] Rimozione vecchi kernel...",
        "ok": "✅ OK",
        "snap_none": "ℹ️  Snap non installato",
        "snap_no_rev": "✅ Nessuna revisione da rimuovere",
        "snap_found": "Trovate {0} revisioni disabilitate",
        "tmp_ok": "✅ file temporanei rimossi",
        "browser_none": "ℹ️  Nessuna cache browser trovata",
        "thumb_none": "ℹ️  Nessuna cache anteprime",
        "thumb_ok": "✅ Anteprime rimosse",
        "trash_ok": "✅ Cestino svuotato",
        "trash_empty": "ℹ️  Cestino già vuoto",
        "kernels_current": "Kernel attuale: {0}",
        "kernels_found": "Trovati {0} kernel installati",
        "kernels_remove": "Rimozione {0}...",
        "kernels_none": "ℹ️  Nessun kernel da rimuovere",
        "graph_title": "📊 Spazio disco prima/dopo",
        "graph_before": "Prima",
        "graph_after": "Dopo",
        "graph_used": "Occupato",
        "graph_free": "Libero",
        "graph_no_mpl": "matplotlib non installato.\n\nInstalla con:\nsudo apt install python3-matplotlib",
        "lang_label": "🌍 Lingua:",
        "notif_title": "🧹 Pulizia completata",
        "notif_msg": "Spazio liberato: {0}",
        "sched_title": "⏱  Schedulazione automatica",
        "sched_desc": "Configura l'esecuzione automatica\ndella pulizia via cron.",
        "sched_freq": "Frequenza",
        "sched_daily": "Ogni giorno",
        "sched_weekly": "Ogni settimana",
        "sched_monthly": "Ogni mese (1° del mese)",
        "sched_time": "Ora (0-23)",
        "sched_day": "Giorno (solo weekly)",
        "sched_sun": "Domenica",
        "sched_mon": "Lunedì",
        "sched_tue": "Martedì",
        "sched_wed": "Mercoledì",
        "sched_thu": "Giovedì",
        "sched_fri": "Venerdì",
        "sched_sat": "Sabato",
        "sched_note": "⚠️  La schedulazione richiede la password sudo.\nLo script verrà installato in:\n  /usr/local/bin/pulizia_ubuntu_cron.sh",
        "sched_save": "💾 Salva",
        "sched_remove": "🗑  Rimuovi",
        "sched_close": "Chiudi",
        "sched_ok_title": "Schedulazione attiva",
        "sched_ok_msg": "✅ Schedulazione installata!\n\nEspressione cron: {0}\n\nLog: /var/log/pulizia_ubuntu.log",
        "sched_remove_confirm_title": "Conferma",
        "sched_remove_confirm_msg": "Rimuovere la schedulazione automatica?",
        "sched_removed_title": "Rimossa",
        "sched_removed_msg": "Schedulazione rimossa con successo.",
        "sched_err_time": "Ora non valida (0-23).",
        "sched_service_title": "Stato del servizio cron",
        "sched_service_active": "✅ Servizio cron ATTIVO",
        "sched_service_inactive": "❌ Servizio cron DISATTIVATO",
        "sched_service_unknown": "⚠️  Stato servizio non rilevato",
        "sched_service_enable": "▶  Abilita cron",
        "sched_service_disable": "⏹  Disabilita cron",
        "sched_service_enabled": "Servizio cron abilitato e avviato.",
        "sched_service_disabled": "Servizio cron disabilitato e fermato.",
        "sched_service_disable_confirm": "Disabilitare il servizio cron?",
        "sched_entry_active": "✅ Schedulazione Pulizia Ubuntu ATTIVA",
        "sched_entry_inactive": "ℹ️  Nessuna schedulazione Pulizia Ubuntu",
        "sched_config_title": "Configurazione schedulazione",
        "help_title": "📖 Guida in linea",
        "help_close": "Chiudi",
        "help_index": "📑 Indice",
        "disk_title": "📊 Analisi spazio disco",
        "disk_analyzing": "Analisi in corso...",
        "disk_path": "Percorso",
        "disk_size": "Dimensione",
        "disk_total": "TOTALE",
        "disk_close": "Chiudi",
        "disk_done": "Analisi completata. Directory più grandi in cima.",
        "kernels_confirm_title": "⚠️  Rimozione kernel",
        "kernels_confirm_msg": "Verranno rimossi i kernel vecchi mantenendo solo\nquello attuale e il più recente.\n\nContinuare?",
    },
    "en": {
        "app_title": "🧹 System Cleanup",
        "subtitle": "Ubuntu 26.04 LTS - Safe maintenance",
        "options_title": " ⚙️  Cleanup options ",
        "opt_browser": "Browser cache cleanup (select which)",
        "opt_snap": "Remove old Snap revisions",
        "opt_tmp": "Temporary files cleanup (/tmp, /var/tmp)",
        "opt_thumb": "Thumbnails cleanup",
        "opt_trash": "Empty trash",
        "opt_kernels": "Remove old kernels (⚠️ dangerous)",
        "btn_run": "▶  Run Cleanup",
        "btn_schedule": "⏱  Schedule",
        "btn_disk": "📊 Disk analysis",
        "btn_help": "❓  Help",
        "btn_exit": "✖  Exit",
        "btn_save": "💾 Save",
        "btn_copy": "📋 Copy",
        "report_label": "📋 Report:",
        "status_ready": "Ready. Press 'Run Cleanup'.",
        "status_done": "✅ Cleanup completed!",
        "status_error": "❌ Error during cleanup",
        "confirm_title": "Confirm",
        "confirm_msg": "Do you want to start the system cleanup?",
        "pwd_title": "🔒 Administrator password",
        "pwd_msg": "Cleanup requires root privileges.\nEnter your password:",
        "pwd_key": "🔑",
        "pwd_confirm": "✔  Confirm",
        "pwd_cancel": "✖  Cancel",
        "pwd_wrong_title": "Wrong password",
        "pwd_wrong_msg": "Authentication failed.\n\nDetail: {0}",
        "pwd_timeout_title": "Timeout",
        "pwd_timeout_msg": "sudo didn't respond within 15 seconds.",
        "pwd_expired_title": "Session expired",
        "pwd_expired_msg": "The sudo session expired.\nRestart the cleanup.",
        "error_title": "Error",
        "done_title": "Done",
        "done_msg": "Cleanup completed!\n\nSpace freed: {0}\nFree space: {1}",
        "save_dialog_title": "Save report",
        "save_ok": "Report saved to:\n{0}",
        "copy_ok": "Report copied to clipboard!",
        "exit_title": "Exit",
        "exit_msg": "Close the application?",
        "exit_running": "Wait for the cleanup to finish.",
        "report_header": "CLEANUP REPORT",
        "initial_free": "Initial free space:",
        "final_summary": "FINAL SUMMARY",
        "final_free": "Final free space   :",
        "freed_positive": "Space freed        : ✅",
        "freed_zero": "Space freed        : ℹ️  No significant change",
        "freed_negative": "Change             : ⚠️  {0} used",
        "completed_at": "Cleanup completed at",
        "step_autoremove": "[1] Cleaning orphan packages...",
        "step_apt_clean": "[2] Cleaning APT cache...",
        "step_apt_autoclean": "[3] Cleaning old package cache...",
        "step_journal": "[4] Cleaning systemd logs (last 3 days)...",
        "step_snap": "[5] Cleaning old Snap revisions...",
        "step_tmp": "[6] Cleaning temporary files...",
        "step_browser": "[7] Cleaning browser caches...",
        "step_thumb": "[8] Cleaning thumbnails...",
        "step_trash": "[9] Emptying trash...",
        "step_kernels": "[10] Removing old kernels...",
        "ok": "✅ OK",
        "snap_none": "ℹ️  Snap not installed",
        "snap_no_rev": "✅ No revisions to remove",
        "snap_found": "Found {0} disabled revisions",
        "tmp_ok": "✅ temporary files removed",
        "browser_none": "ℹ️  No browser cache found",
        "thumb_none": "ℹ️  No thumbnail cache",
        "thumb_ok": "✅ Thumbnails removed",
        "trash_ok": "✅ Trash emptied",
        "trash_empty": "ℹ️  Trash already empty",
        "kernels_current": "Current kernel: {0}",
        "kernels_found": "Found {0} installed kernels",
        "kernels_remove": "Removing {0}...",
        "kernels_none": "ℹ️  No kernels to remove",
        "graph_title": "📊 Disk space before/after",
        "graph_before": "Before",
        "graph_after": "After",
        "graph_used": "Used",
        "graph_free": "Free",
        "graph_no_mpl": "matplotlib not installed.\n\nInstall with:\nsudo apt install python3-matplotlib",
        "lang_label": "🌍 Language:",
        "notif_title": "🧹 Cleanup completed",
        "notif_msg": "Space freed: {0}",
        "sched_title": "⏱  Automatic scheduling",
        "sched_desc": "Configure automatic cleanup\nvia cron.",
        "sched_freq": "Frequency",
        "sched_daily": "Daily",
        "sched_weekly": "Weekly",
        "sched_monthly": "Monthly (1st of month)",
        "sched_time": "Time (0-23)",
        "sched_day": "Day (weekly only)",
        "sched_sun": "Sunday",
        "sched_mon": "Monday",
        "sched_tue": "Tuesday",
        "sched_wed": "Wednesday",
        "sched_thu": "Thursday",
        "sched_fri": "Friday",
        "sched_sat": "Saturday",
        "sched_note": "⚠️  Scheduling requires sudo password.\nScript will be installed at:\n  /usr/local/bin/pulizia_ubuntu_cron.sh",
        "sched_save": "💾 Save",
        "sched_remove": "🗑  Remove",
        "sched_close": "Close",
        "sched_ok_title": "Schedule active",
        "sched_ok_msg": "✅ Schedule installed!\n\nCron expression: {0}\n\nLog: /var/log/pulizia_ubuntu.log",
        "sched_remove_confirm_title": "Confirm",
        "sched_remove_confirm_msg": "Remove the automatic schedule?",
        "sched_removed_title": "Removed",
        "sched_removed_msg": "Schedule removed successfully.",
        "sched_err_time": "Invalid hour (0-23).",
        "sched_service_title": "Cron service status",
        "sched_service_active": "✅ Cron service ACTIVE",
        "sched_service_inactive": "❌ Cron service DISABLED",
        "sched_service_unknown": "⚠️  Service status unknown",
        "sched_service_enable": "▶  Enable cron",
        "sched_service_disable": "⏹  Disable cron",
        "sched_service_enabled": "Cron service enabled and started.",
        "sched_service_disabled": "Cron service disabled and stopped.",
        "sched_service_disable_confirm": "Disable the cron service?",
        "sched_entry_active": "✅ Pulizia Ubuntu schedule ACTIVE",
        "sched_entry_inactive": "ℹ️  No Pulizia Ubuntu schedule",
        "sched_config_title": "Schedule configuration",
        "help_title": "📖 Online help",
        "help_close": "Close",
        "help_index": "📑 Index",
        "disk_title": "📊 Disk space analysis",
        "disk_analyzing": "Analyzing...",
        "disk_path": "Path",
        "disk_size": "Size",
        "disk_total": "TOTAL",
        "disk_close": "Close",
        "disk_done": "Analysis complete. Largest directories on top.",
        "kernels_confirm_title": "⚠️  Kernel removal",
        "kernels_confirm_msg": "Old kernels will be removed, keeping only\nthe current and the most recent one.\n\nContinue?",
    },
}


GUIDE_CONTENT = {
    "it": [
        ("Introduzione", """Benvenuto in Pulizia Ubuntu!

Questa applicazione ti aiuta a mantenere il tuo sistema
pulito e veloce rimuovendo file temporanei, cache e
pacchetti non più necessari.

Ogni operazione viene eseguita in modo sicuro: l'app
usa solo comandi standard di Ubuntu e mostra sempre
un report dettagliato di ciò che è stato fatto."""),
        ("Esegui Pulizia", """Clicca il pulsante "Esegui Pulizia" per avviare la
manutenzione del sistema.

L'app ti chiederà la password di amministratore (sudo)
perché alcune operazioni richiedono privilegi di root.

Una volta inserita la password, la pulizia partirà
automaticamente e vedrai:

  • Il report aggiornarsi in tempo reale
  • La barra di progresso avanzare
  • Una notifica desktop al termine
  • Un grafico con lo spazio liberato

Al termine puoi salvare o copiare il report."""),
        ("Opzioni di pulizia", """Puoi scegliere quali operazioni eseguire tramite le
caselle di controllo:

✓ Pulizia cache browser (Chrome, Chromium, Edge,
  Firefox, Brave, Opera). Non tocca segnalibri
  o password.

✓ Rimozione vecchie revisioni Snap
✓ Pulizia file temporanei
✓ Pulizia anteprime
✓ Svuotamento cestino
✓ Rimozione vecchi kernel (⚠️ pericoloso)

Sempre attive:
  • Pulizia pacchetti orfani (apt autoremove)
  • Pulizia cache APT
  • Pulizia log di systemd (mantiene ultimi 3 giorni)"""),
        ("Report", """Ogni operazione viene registrata in un report
dettagliato visibile in fondo alla finestra.

📋 Copia
  Copia tutto il report negli appunti.

💾 Salva
  Salva il report in un file di testo con data e ora
  nel nome (es. report_pulizia_20260930_143045.txt)."""),
        ("Schedulazione", """Puoi programmare la pulizia automatica aprendo la
finestra "⏱ Schedula".

SEZIONE 1 - Stato del servizio cron
  Mostra se cron è attivo e se esiste già una
  schedulazione. Puoi abilitare/disabilitare cron.

SEZIONE 2 - Configurazione
  Frequenza: ogni giorno, settimana o mese
  Ora: da 0 a 23
  Giorno: solo per settimanale

Salvando, l'app installa:
  • /usr/local/bin/pulizia_ubuntu_cron.sh
  • /etc/cron.d/pulizia-ubuntu

Log in /var/log/pulizia_ubuntu.log"""),
        ("Notifiche", """Al termine di ogni pulizia ricevi una notifica
desktop in alto a destra.

Funziona sia per pulizia manuale sia per cron.

Se non vedi le notifiche:
  sudo apt install libnotify-bin"""),
        ("Lingua", """L'app supporta Italiano e Inglese.

Usa il menu a tendina in alto a destra per cambiare
lingua in qualsiasi momento.

La lingua viene anche rilevata dall'ambiente di
sistema (variabile LANG)."""),
        ("Analisi disco", """Il pulsante "📊 Analisi disco" apre una finestra
che mostra le directory più grandi del sistema.

Vengono analizzate:
  • /var/log, /var/cache, /var/lib/snapd
  • /usr/lib, /usr/share
  • ~/.cache, ~/.local/share/Trash
  • Browser (Chrome, Firefox, Brave)
  • E altre...

È solo lettura: non cancella nulla."""),
        ("Domande frequenti", """D: Serve sudo?
R: Sì, per apt, journalctl, snap, cron.

D: La cache del browser cancella le password?
R: No. Solo cache temporanea.

D: Dove trovo il log dell'app?
R: /tmp/pulizia_ubuntu_debug.log

D: Come disinstallo tutto?
R: sudo dpkg -r pulizia-ubuntu
   sudo rm -rf /usr/share/pulizia-ubuntu
   sudo rm -f /etc/cron.d/pulizia-ubuntu"""),
    ],
    "en": [
        ("Introduction", """Welcome to Ubuntu Cleanup!

This app helps you keep your system clean and fast
by removing temporary files, caches and unnecessary
packages.

Every operation is safe: the app uses only standard
Ubuntu commands and always shows a detailed report."""),
        ("Run Cleanup", """Click "Run Cleanup" to start maintenance.

The app will ask for your sudo password because some
operations require root privileges.

You will see:

  • Report updating in real time
  • Progress bar
  • Desktop notification when done
  • Chart with freed space"""),
        ("Cleanup Options", """Choose which operations to run:

✓ Browser cache cleanup (Chrome, Chromium, Edge,
  Firefox, Brave, Opera). Doesn't touch bookmarks
  or passwords.

✓ Remove old Snap revisions
✓ Temporary files cleanup
✓ Thumbnails cleanup
✓ Empty trash
✓ Remove old kernels (⚠️ dangerous)

Always active:
  • Orphan packages (apt autoremove)
  • APT cache
  • systemd logs (keeps last 3 days)"""),
        ("Report", """Every operation is logged in a detailed report.

📋 Copy
  Copies report to clipboard.

💾 Save
  Saves report with date/time in filename."""),
        ("Scheduling", """Open the "⏱ Schedule" window.

SECTION 1 - Cron service status
  Shows if cron is active and if a schedule exists.

SECTION 2 - Configuration
  Frequency: daily, weekly, monthly
  Hour: 0-23
  Day: weekly only

Saves:
  • /usr/local/bin/pulizia_ubuntu_cron.sh
  • /etc/cron.d/pulizia-ubuntu

Log at /var/log/pulizia_ubuntu.log"""),
        ("Notifications", """At the end of every cleanup you get a desktop
notification in the top right corner.

Works for both manual and cron cleanup.

If missing:
  sudo apt install libnotify-bin"""),
        ("Language", """Supports Italian and English.

Use the dropdown at the top right to switch language
at any time.

Auto-detected from LANG variable."""),
        ("Disk analysis", """The "📊 Disk analysis" button opens a window with
the largest directories.

Analyzed:
  • /var/log, /var/cache, /var/lib/snapd
  • /usr/lib, /usr/share
  • ~/.cache, ~/.local/share/Trash
  • Browsers
  • And more...

Read-only: nothing is deleted."""),
        ("FAQ", """Q: Is sudo required?
A: Yes, for apt, journalctl, snap, cron.

Q: Does browser cleanup remove passwords?
A: No. Only temporary cache.

Q: Where's the app log?
A: /tmp/pulizia_ubuntu_debug.log

Q: How to uninstall?
A: sudo dpkg -r pulizia-ubuntu
   sudo rm -rf /usr/share/pulizia-ubuntu
   sudo rm -f /etc/cron.d/pulizia-ubuntu"""),
    ],
}


def _rileva_lingua():
    for var in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        val = os.environ.get(var, "")
        if val:
            code = val.split(":")[0].split(".")[0].split("_")[0].lower()
            if code in TRANSLATIONS:
                return code
    return "en"


CURRENT_LANG = _rileva_lingua()


def _(key, *args):
    testo = TRANSLATIONS.get(CURRENT_LANG, TRANSLATIONS["en"]).get(key, key)
    if args:
        try:
            return testo.format(*args)
        except Exception:
            return testo
    return testo


def debug_log(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    except Exception:
        pass


class PuliziaApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} {APP_VERSION}")
        self.root.geometry("820x760+80+40")
        self.root.minsize(760, 640)
        self.root.configure(bg="#2c3e50")

        self.report_lines = []
        self.spazio_prima = 0
        self.spazio_dopo = 0
        self.totale_disco = 0
        self.in_esecuzione = False
        self.password_sudo = None
        self.ui_queue = queue.Queue()

        # Variabili
        self.var_browser_all = tk.BooleanVar(value=True)
        self.var_chrome = tk.BooleanVar(value=True)
        self.var_chromium = tk.BooleanVar(value=True)
        self.var_edge = tk.BooleanVar(value=True)
        self.var_firefox = tk.BooleanVar(value=True)
        self.var_brave = tk.BooleanVar(value=True)
        self.var_opera = tk.BooleanVar(value=True)
        self.var_snap = tk.BooleanVar(value=True)
        self.var_tmp = tk.BooleanVar(value=True)
        self.var_thumbnails = tk.BooleanVar(value=True)
        self.var_trash = tk.BooleanVar(value=True)
        self.var_kernels = tk.BooleanVar(value=False)

        debug_log("=" * 50)
        debug_log(f"=== App avviata - {APP_NAME} {APP_VERSION} ===")
        debug_log(f"Lingua: {CURRENT_LANG}")

        self._set_icona()
        self._build_ui()
        self._calcola_spazio_iniziale()
        self._avvia_poller_coda()

        self.root.bind("<F1>", lambda e: self.apri_guida())
        self.root.bind("<Control-h>", lambda e: self.apri_guida())

        self.root.attributes("-topmost", True)
        self.root.after(300, lambda: (
            self.root.lift(),
            self.root.focus_force(),
            self.root.attributes("-topmost", False)
        ))

    def _set_icona(self):
        percorsi = [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "icona.png"),
            "/usr/share/icons/hicolor/256x256/apps/pulizia-ubuntu.png",
            "/usr/share/icons/hicolor/128x128/apps/pulizia-ubuntu.png",
            "/usr/share/pulizia-ubuntu/icona.png",
        ]
        for p in percorsi:
            if os.path.exists(p):
                try:
                    img = tk.PhotoImage(file=p)
                    self.root.iconphoto(True, img)
                    self._icona_ref = img
                    return
                except Exception:
                    continue

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#2c3e50")
        header.pack(fill=tk.X, pady=(10, 0))

        frame_lang = tk.Frame(header, bg="#2c3e50")
        frame_lang.pack(side=tk.RIGHT, padx=15)
        tk.Label(frame_lang, text=_("lang_label"), font=("Ubuntu", 9),
                 bg="#2c3e50", fg="#95a5a6").pack(side=tk.LEFT)
        self.lang_var = tk.StringVar(value=CURRENT_LANG)
        lang_combo = ttk.Combobox(frame_lang, textvariable=self.lang_var,
                                  state="readonly", width=4,
                                  values=["it", "en"], font=("Ubuntu", 9))
        lang_combo.pack(side=tk.LEFT, padx=4)
        lang_combo.bind("<<ComboboxSelected>>", self._cambia_lingua)

        self.lbl_titolo = tk.Label(header, text=_("app_title"),
                                   font=("Ubuntu", 20, "bold"),
                                   bg="#2c3e50", fg="#ecf0f1")
        self.lbl_titolo.pack()
        self.lbl_sottotitolo = tk.Label(
            self.root, text=f"{_('subtitle')}  |  v{APP_VERSION}",
            font=("Ubuntu", 10, "italic"),
            bg="#2c3e50", fg="#95a5a6")
        self.lbl_sottotitolo.pack(pady=(2, 6))

        # Opzioni
        self.frame_opt = tk.LabelFrame(
            self.root, text=_("options_title"),
            font=("Ubuntu", 10, "bold"),
            bg="#34495e", fg="#ecf0f1", bd=2, relief="groove")
        self.frame_opt.pack(fill=tk.X, padx=20, pady=6)

        self.checkbuttons = {}

        # Browser master
        frame_browsers = tk.Frame(self.frame_opt, bg="#34495e")
        frame_browsers.pack(fill=tk.X, padx=10, pady=2)
        cb_all = tk.Checkbutton(
            frame_browsers, text=_("opt_browser"),
            variable=self.var_browser_all,
            font=("Ubuntu", 10, "bold"),
            bg="#34495e", fg="#ecf0f1", selectcolor="#2c3e50",
            activebackground="#34495e", activeforeground="#1abc9c",
            anchor="w", command=self._toggle_all_browsers)
        cb_all.pack(fill=tk.X)
        self.checkbuttons["opt_browser"] = cb_all

        # Browser individuali
        frame_sub = tk.Frame(self.frame_opt, bg="#34495e")
        frame_sub.pack(fill=tk.X, padx=10, pady=(0, 4))
        self.browser_vars = {
            "chrome": self.var_chrome,
            "chromium": self.var_chromium,
            "edge": self.var_edge,
            "firefox": self.var_firefox,
            "brave": self.var_brave,
            "opera": self.var_opera,
        }
        for i, (nome, var) in enumerate(self.browser_vars.items()):
            r, c = i // 3, i % 3
            cb = tk.Checkbutton(
                frame_sub, text=nome.capitalize(),
                variable=var, font=("Ubuntu", 9),
                bg="#34495e", fg="#ecf0f1", selectcolor="#2c3e50",
                activebackground="#34495e", activeforeground="#1abc9c",
                anchor="w", command=self._sync_master_browser)
            cb.grid(row=r, column=c, sticky="w", padx=15, pady=1)

        # Altre opzioni
        for key, var in [("opt_snap", self.var_snap),
                         ("opt_tmp", self.var_tmp),
                         ("opt_thumb", self.var_thumbnails),
                         ("opt_trash", self.var_trash),
                         ("opt_kernels", self.var_kernels)]:
            cb = tk.Checkbutton(self.frame_opt, text=_(key), variable=var,
                                font=("Ubuntu", 10),
                                bg="#34495e", fg="#ecf0f1",
                                selectcolor="#2c3e50",
                                activebackground="#34495e",
                                activeforeground="#1abc9c", anchor="w")
            cb.pack(fill=tk.X, padx=10, pady=2)
            self.checkbuttons[key] = cb

        # Pulsanti
        frame_btn = tk.Frame(self.root, bg="#2c3e50")
        frame_btn.pack(pady=6)

        self.btn_esegui = self._crea_pulsante(frame_btn, _("btn_run"),
                                              "#27ae60", "#2ecc71",
                                              self.avvia_pulizia, 18)
        self.btn_esegui.pack(side=tk.LEFT, padx=4)

        self.btn_schedula = self._crea_pulsante(frame_btn, _("btn_schedule"),
                                                "#2980b9", "#3498db",
                                                self.apri_schedulazione, 12)
        self.btn_schedula.pack(side=tk.LEFT, padx=4)

        self.btn_disco = self._crea_pulsante(frame_btn, _("btn_disk"),
                                             "#16a085", "#1abc9c",
                                             self.analizza_disco, 13)
        self.btn_disco.pack(side=tk.LEFT, padx=4)

        self.btn_guida = self._crea_pulsante(frame_btn, _("btn_help"),
                                             "#8e44ad", "#9b59b6",
                                             self.apri_guida, 10)
        self.btn_guida.pack(side=tk.LEFT, padx=4)

        self.btn_esci = self._crea_pulsante(frame_btn, _("btn_exit"),
                                            "#c0392b", "#e74c3c",
                                            self.esci, 8)
        self.btn_esci.pack(side=tk.LEFT, padx=4)

        # Progress
        self.progress = ttk.Progressbar(self.root, orient="horizontal",
                                        length=740, mode="determinate")
        self.progress.pack(pady=6, padx=20, fill=tk.X)

        self.lbl_stato = tk.Label(self.root, text=_("status_ready"),
                                  font=("Ubuntu", 10),
                                  bg="#2c3e50", fg="#f39c12")
        self.lbl_stato.pack(pady=4)

        # Report header
        frame_head = tk.Frame(self.root, bg="#2c3e50")
        frame_head.pack(fill=tk.X, padx=20, pady=(6, 0))

        self.lbl_report = tk.Label(frame_head, text=_("report_label"),
                                   font=("Ubuntu", 11, "bold"),
                                   bg="#2c3e50", fg="#ecf0f1")
        self.lbl_report.pack(side=tk.LEFT)

        self.btn_salva = tk.Button(frame_head, text=_("btn_save"),
                                   font=("Ubuntu", 9), bg="#16a085", fg="white",
                                   relief="flat", cursor="hand2",
                                   command=self.salva_report, state=tk.DISABLED)
        self.btn_salva.pack(side=tk.RIGHT, padx=4)

        self.btn_copia = tk.Button(frame_head, text=_("btn_copy"),
                                   font=("Ubuntu", 9), bg="#8e44ad", fg="white",
                                   relief="flat", cursor="hand2",
                                   command=self.copia_report, state=tk.DISABLED)
        self.btn_copia.pack(side=tk.RIGHT, padx=4)

        self.txt_report = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=90, height=13,
            font=("Ubuntu Mono", 9), bg="#1c2833", fg="#ecf0f1",
            insertbackground="white", relief="flat", state=tk.DISABLED)
        self.txt_report.pack(padx=20, pady=(5, 12), fill=tk.BOTH, expand=True)

    def _crea_pulsante(self, parent, testo, bg, active_bg, comando, width=15):
        return tk.Button(parent, text=testo, font=("Ubuntu", 11, "bold"),
                         bg=bg, fg="white", activebackground=active_bg,
                         activeforeground="white", width=width, height=2,
                         cursor="hand2", relief="flat", command=comando)

    def _toggle_all_browsers(self):
        val = self.var_browser_all.get()
        for v in self.browser_vars.values():
            v.set(val)

    def _sync_master_browser(self):
        tutti_attivi = all(v.get() for v in self.browser_vars.values())
        self.var_browser_all.set(tutti_attivi)

    def _cambia_lingua(self, event=None):
        global CURRENT_LANG
        CURRENT_LANG = self.lang_var.get()
        self.lbl_titolo.config(text=_("app_title"))
        self.lbl_sottotitolo.config(text=f"{_('subtitle')}  |  v{APP_VERSION}")
        self.frame_opt.config(text=_("options_title"))
        for key, cb in self.checkbuttons.items():
            cb.config(text=_(key))
        self.btn_esegui.config(text=_("btn_run"))
        self.btn_schedula.config(text=_("btn_schedule"))
        self.btn_disco.config(text=_("btn_disk"))
        self.btn_guida.config(text=_("btn_help"))
        self.btn_esci.config(text=_("btn_exit"))
        self.btn_salva.config(text=_("btn_save"))
        self.btn_copia.config(text=_("btn_copy"))
        self.lbl_report.config(text=_("report_label"))
        self.lbl_stato.config(text=_("status_ready"))

    def _avvia_poller_coda(self):
        try:
            while True:
                tipo, payload = self.ui_queue.get_nowait()
                if tipo == "log":
                    self.txt_report.config(state=tk.NORMAL)
                    self.txt_report.insert(tk.END, payload + "\n")
                    self.txt_report.see(tk.END)
                    self.txt_report.config(state=tk.DISABLED)
                elif tipo == "stato":
                    self.lbl_stato.config(text=payload)
                elif tipo == "progress":
                    self.progress["value"] = payload
                elif tipo == "abilita_pulsanti":
                    self._set_pulsanti(payload)
                elif tipo == "abilita_report":
                    self.btn_salva.config(state=tk.NORMAL)
                    self.btn_copia.config(state=tk.NORMAL)
                elif tipo == "info":
                    messagebox.showinfo(*payload)
                elif tipo == "error":
                    messagebox.showerror(*payload)
                elif tipo == "warning":
                    messagebox.showwarning(*payload)
                elif tipo == "grafico":
                    self._mostra_grafico(*payload)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self._avvia_poller_coda)

    def _mostra_grafico(self, prima, dopo, totale):
        try:
            import matplotlib
            matplotlib.use("TkAgg")
            from matplotlib.figure import Figure
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        except ImportError:
            messagebox.showwarning(_("graph_title"), _("graph_no_mpl"))
            return

        win = tk.Toplevel(self.root)
        win.title(_("graph_title"))
        win.geometry("700x500")
        win.configure(bg="#2c3e50")
        win.transient(self.root)

        usato_prima = totale - prima
        usato_dopo = totale - dopo

        fig = Figure(figsize=(7, 4.5), dpi=100, facecolor="#2c3e50")
        ax = fig.add_subplot(111, facecolor="#1c2833")
        labels = [_("graph_before"), _("graph_after")]
        usati_gb = [usato_prima / (1024**3), usato_dopo / (1024**3)]
        liberi_gb = [prima / (1024**3), dopo / (1024**3)]

        x = [0, 1]
        ax.bar(x, usati_gb, 0.5, label=_("graph_used"),
               color="#e74c3c", edgecolor="white", linewidth=0.5)
        ax.bar(x, liberi_gb, 0.5, bottom=usati_gb,
               label=_("graph_free"), color="#27ae60",
               edgecolor="white", linewidth=0.5)

        for i, (u, f) in enumerate(zip(usati_gb, liberi_gb)):
            if u > 0.5:
                ax.text(i, u / 2, f"{u:.1f} GB", ha="center", va="center",
                        color="white", fontweight="bold", fontsize=10)
            if f > 0.5:
                ax.text(i, u + f / 2, f"{f:.1f} GB", ha="center", va="center",
                        color="white", fontweight="bold", fontsize=10)

        ax.set_xticks(x)
        ax.set_xticklabels(labels, color="#ecf0f1", fontsize=11)
        ax.set_ylabel("GB", color="#ecf0f1")
        ax.tick_params(axis="y", colors="#ecf0f1")
        ax.spines["bottom"].set_color("#7f8c8d")
        ax.spines["left"].set_color("#7f8c8d")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", linestyle="--", alpha=0.3, color="#7f8c8d")
        ax.legend(loc="upper right", facecolor="#34495e",
                  edgecolor="white", labelcolor="#ecf0f1")

        delta = dopo - prima
        if delta > 0:
            titolo = f"{_('graph_title')}  (+{delta / (1024**3):.2f} GB)"
            fig.suptitle(titolo, color="#2ecc71",
                         fontsize=13, fontweight="bold")
        else:
            fig.suptitle(_("graph_title"), color="#ecf0f1",
                         fontsize=13, fontweight="bold")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True,
                                    padx=10, pady=10)
        tk.Button(win, text="OK", font=("Ubuntu", 10, "bold"),
                  bg="#27ae60", fg="white", relief="flat",
                  width=12, cursor="hand2",
                  command=win.destroy).pack(pady=8)

    def _calcola_spazio_iniziale(self):
        try:
            u = shutil.disk_usage("/")
            self.spazio_prima = u.free
            self.totale_disco = u.total
        except Exception:
            self.spazio_prima = 0
            self.totale_disco = 0

    def _log(self, testo):
        self.report_lines.append(testo)
        self.ui_queue.put(("log", testo))

    def _set_stato(self, testo):
        self.ui_queue.put(("stato", testo))

    def _set_progress(self, valore):
        self.ui_queue.put(("progress", valore))

    def _bytes_a_human(self, b):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if b < 1024:
                return f"{b:.2f} {unit}"
            b /= 1024
        return f"{b:.2f} PB"

    def _esegui_comando(self, cmd, timeout=300):
        if any(op in cmd for op in ["|", ">", "<", "&&", ";", "*"]):
            args = ["bash", "-c", cmd]
            usa_sudo = "sudo " in cmd
        else:
            args = cmd.split()
            usa_sudo = args and args[0] == "sudo"
            if usa_sudo:
                args = ["sudo", "-S", "-p", ""] + args[1:]
        try:
            if usa_sudo and args[0] == "sudo":
                r = subprocess.run(args,
                                   input=(self.password_sudo or "") + "\n",
                                   capture_output=True, text=True,
                                   timeout=timeout)
            elif usa_sudo:
                r = subprocess.run(args,
                                   input=((self.password_sudo or "") + "\n") * 10,
                                   capture_output=True, text=True,
                                   timeout=timeout)
            else:
                r = subprocess.run(args, capture_output=True, text=True,
                                   timeout=timeout)
            sl = (r.stderr or "").lower()
            if ("incorrect password" in sl or
                    "password incorretta" in sl or
                    "autenticazione non riuscita" in sl or
                    "sorry, try again" in sl):
                return False, "ERRORE_PASSWORD"
            return r.returncode == 0, (r.stdout or "").strip() or (r.stderr or "").strip()
        except subprocess.TimeoutExpired:
            return False, "Timeout comando"
        except Exception as e:
            return False, str(e)

    def _sudo_in_cache(self):
        try:
            r = subprocess.run(["sudo", "-n", "true"],
                               capture_output=True, text=True, timeout=5)
            return r.returncode == 0
        except Exception:
            return False

    def _chiedi_password(self):
        dialog = tk.Toplevel(self.root)
        dialog.title(_("pwd_title"))
        dialog.geometry("440x230")
        dialog.configure(bg="#2c3e50")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - 220
        y = (dialog.winfo_screenheight() // 2) - 115
        dialog.geometry(f"+{x}+{y}")

        tk.Label(dialog, text=_("pwd_title"), font=("Ubuntu", 13, "bold"),
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=(15, 5))
        tk.Label(dialog, text=_("pwd_msg"), font=("Ubuntu", 9),
                 bg="#2c3e50", fg="#95a5a6",
                 justify="center").pack(pady=(0, 10))

        fi = tk.Frame(dialog, bg="#2c3e50")
        fi.pack(pady=5)
        tk.Label(fi, text=_("pwd_key"), font=("Ubuntu", 14),
                 bg="#2c3e50", fg="#f39c12").pack(side=tk.LEFT, padx=(0, 5))
        entry = tk.Entry(fi, show="●", font=("Ubuntu", 12), width=25,
                         bg="#1c2833", fg="#ecf0f1", insertbackground="white",
                         relief="flat", bd=5)
        entry.pack(side=tk.LEFT)
        entry.focus_set()
        ris = {"pwd": None}

        def ok(event=None):
            p = entry.get()
            if p:
                ris["pwd"] = p
                dialog.destroy()

        entry.bind("<Return>", ok)

        fb = tk.Frame(dialog, bg="#2c3e50")
        fb.pack(pady=15)
        tk.Button(fb, text=_("pwd_confirm"), font=("Ubuntu", 10, "bold"),
                  bg="#27ae60", fg="white", relief="flat", width=12,
                  cursor="hand2", command=ok).pack(side=tk.LEFT, padx=5)
        tk.Button(fb, text=_("pwd_cancel"), font=("Ubuntu", 10, "bold"),
                  bg="#c0392b", fg="white", relief="flat", width=12,
                  cursor="hand2", command=dialog.destroy).pack(side=tk.LEFT, padx=5)
        dialog.wait_window()
        return ris["pwd"]

    def _assicura_sudo(self):
        if self._sudo_in_cache():
            return True
        pwd = self._chiedi_password()
        if pwd is None:
            return False
        try:
            r = subprocess.run(["sudo", "-S", "-p", "", "-v"],
                               input=pwd + "\n", capture_output=True,
                               text=True, timeout=15)
            if r.returncode != 0:
                messagebox.showerror(_("pwd_wrong_title"),
                                     _("pwd_wrong_msg", r.stderr.strip() or "?"))
                return False
            self.password_sudo = pwd
            return True
        except subprocess.TimeoutExpired:
            messagebox.showerror(_("pwd_timeout_title"), _("pwd_timeout_msg"))
            return False
        except Exception as e:
            messagebox.showerror(_("error_title"), str(e))
            return False

    def avvia_pulizia(self):
        if self.in_esecuzione:
            return
        if not messagebox.askyesno(_("confirm_title"), _("confirm_msg")):
            return
        if not self._assicura_sudo():
            return
        self.in_esecuzione = True
        self._set_pulsanti(False)
        self.txt_report.config(state=tk.NORMAL)
        self.txt_report.delete("1.0", tk.END)
        self.txt_report.config(state=tk.DISABLED)
        self.report_lines = []
        self._set_progress(0)
        threading.Thread(target=self._esegui_pulizia, daemon=True).start()

    def _esegui_pulizia(self):
        try:
            self._calcola_spazio_iniziale()
            self._log("=" * 70)
            self._log(f"  {_('report_header')} - "
                      f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            self._log("=" * 70)
            self._log(f"{_('initial_free')} "
                      f"{self._bytes_a_human(self.spazio_prima)}")
            self._log("")

            passi = [
                (_("step_autoremove"), "sudo apt-get autoremove --purge -y"),
                (_("step_apt_clean"), "sudo apt-get clean"),
                (_("step_apt_autoclean"), "sudo apt-get autoclean"),
                (_("step_journal"), "sudo journalctl --vacuum-time=3d"),
            ]
            if self.var_snap.get():
                passi.append((_("step_snap"), "SNAP"))
            if self.var_tmp.get():
                passi.append((_("step_tmp"), "TMP"))
            browser_attivi = [n for n, v in self.browser_vars.items() if v.get()]
            if browser_attivi:
                passi.append((_("step_browser"),
                              "BROWSER:" + ",".join(browser_attivi)))
            if self.var_thumbnails.get():
                passi.append((_("step_thumb"), "THUMB"))
            if self.var_trash.get():
                passi.append((_("step_trash"), "TRASH"))
            if self.var_kernels.get():
                passi.append((_("step_kernels"), "KERNELS"))

            totale = len(passi)
            completati = 0

            for stato, cmd in passi:
                self._set_stato(stato)
                self._log(f"▶ {stato}")

                if cmd == "SNAP":
                    self._pulisci_snap()
                elif cmd == "TMP":
                    self._pulisci_tmp()
                elif cmd.startswith("BROWSER:"):
                    self._pulisci_browser(cmd.split(":", 1)[1].split(","))
                elif cmd == "THUMB":
                    self._pulisci_thumbnails()
                elif cmd == "TRASH":
                    self._svuota_cestino()
                elif cmd == "KERNELS":
                    self._gestisci_kernel()
                else:
                    ok, out = self._esegui_comando(cmd)
                    if ok:
                        self._log(f"   {_('ok')}")
                        if out:
                            for r in out.split("\n")[-5:]:
                                if r.strip():
                                    self._log(f"      {r}")
                    elif out == "ERRORE_PASSWORD":
                        self._log("   ❌ " + _("pwd_expired_msg"))
                        self.password_sudo = None
                        self.ui_queue.put(("error", (_("pwd_expired_title"),
                                                     _("pwd_expired_msg"))))
                        return
                    else:
                        self._log(f"   ⚠️  {out}")

                self._log("")
                completati += 1
                self._set_progress((completati / totale) * 100)

            self.spazio_dopo = shutil.disk_usage("/").free
            liberato = self.spazio_dopo - self.spazio_prima

            self._log("=" * 70)
            self._log(f"  📊 {_('final_summary')}")
            self._log("=" * 70)
            self._log(f"{_('final_free')} "
                      f"{self._bytes_a_human(self.spazio_dopo)}")
            if liberato > 0:
                self._log(f"{_('freed_positive')} "
                          f"{self._bytes_a_human(liberato)}")
            elif liberato == 0:
                self._log(_("freed_zero"))
            else:
                self._log(_("freed_negative",
                            self._bytes_a_human(abs(liberato))))
            self._log("")
            self._log(f"{_('completed_at')} "
                      f"{datetime.now().strftime('%H:%M:%S')}")

            self._set_stato(_("status_done"))
            self._set_progress(100)
            self.ui_queue.put(("abilita_report", True))

            self._invia_notifica(
                _("notif_title"),
                _("notif_msg", self._bytes_a_human(max(liberato, 0))))
            self.ui_queue.put(("grafico",
                               (self.spazio_prima, self.spazio_dopo,
                                self.totale_disco)))
            self.ui_queue.put(("info", (
                _("done_title"),
                _("done_msg",
                  self._bytes_a_human(max(liberato, 0)),
                  self._bytes_a_human(self.spazio_dopo)))))
        except Exception as e:
            debug_log(f"_esegui_pulizia: {e}")
            self._log(f"\n❌ {e}")
            self._set_stato(_("status_error"))
            self.ui_queue.put(("error", (_("error_title"), str(e))))
        finally:
            self.in_esecuzione = False
            self.ui_queue.put(("abilita_pulsanti", True))

    def _pulisci_snap(self):
        if not shutil.which("snap"):
            self._log(f"   {_('snap_none')}")
            return
        ok, out = self._esegui_comando(
            "snap list --all | awk '/disabled/{print $1, $3}'")
        if ok and out.strip():
            righe = [r for r in out.strip().split("\n") if r.strip()]
            self._log(f"   {_('snap_found', len(righe))}")
            for riga in righe:
                p = riga.split()
                if len(p) >= 2:
                    self._log(f"      - {p[0]} (rev {p[1]})...")
                    self._esegui_comando(
                        f"sudo snap remove {p[0]} --revision={p[1]}")
        else:
            self._log(f"   {_('snap_no_rev')}")

    def _pulisci_tmp(self):
        self._esegui_comando(
            "sudo find /tmp -type f -atime +7 -delete 2>/dev/null")
        self._esegui_comando(
            "sudo find /var/tmp -type f -atime +30 -delete 2>/dev/null")
        self._log(f"   {_('tmp_ok')}")

    def _pulisci_browser(self, attivi=None):
        if attivi is None:
            attivi = list(self.browser_vars.keys())
        home = os.path.expanduser("~")
        percorsi = {
            "chrome": [f"{home}/.cache/google-chrome",
                       f"{home}/.config/google-chrome/Default/Cache",
                       f"{home}/.config/google-chrome/Default/Code Cache",
                       f"{home}/.config/google-chrome/Default/GPUCache"],
            "chromium": [f"{home}/.cache/chromium",
                         f"{home}/.config/chromium/Default/Cache",
                         f"{home}/.config/chromium/Default/Code Cache",
                         f"{home}/.config/chromium/Default/GPUCache"],
            "edge": [f"{home}/.cache/microsoft-edge",
                     f"{home}/.config/microsoft-edge/Default/Cache",
                     f"{home}/.config/microsoft-edge/Default/Code Cache",
                     f"{home}/.config/microsoft-edge/Default/GPUCache"],
            "firefox": [f"{home}/.cache/mozilla/firefox",
                        f"{home}/.mozilla/firefox/*/cache2",
                        f"{home}/.mozilla/firefox/*/startupCache"],
            "brave": [f"{home}/.cache/BraveSoftware",
                      f"{home}/.config/BraveSoftware/Brave-Browser/Default/Cache",
                      f"{home}/.config/BraveSoftware/Brave-Browser/Default/Code Cache",
                      f"{home}/.config/BraveSoftware/Brave-Browser/Default/GPUCache"],
            "opera": [f"{home}/.cache/opera",
                      f"{home}/.config/opera/Cache",
                      f"{home}/.config/opera/Code Cache"],
        }
        totale = 0
        for nome in attivi:
            lista = percorsi.get(nome, [])
            rimossi = 0
            for pat in lista:
                for p in glob.glob(pat):
                    if os.path.exists(p):
                        try:
                            if os.path.isdir(p):
                                shutil.rmtree(p, ignore_errors=True)
                                if "cache" in p.lower():
                                    try:
                                        os.makedirs(p, exist_ok=True)
                                    except Exception:
                                        pass
                            else:
                                os.remove(p)
                            rimossi += 1
                        except Exception:
                            pass
            if rimossi:
                self._log(f"   ✅ {nome.capitalize()}: {rimossi}")
                totale += rimossi
            else:
                self._log(f"   -- {nome.capitalize()}: nessuna cache")
        if totale == 0:
            self._log(f"   {_('browser_none')}")

    def _pulisci_thumbnails(self):
        home = os.path.expanduser("~")
        p = os.path.join(home, ".cache", "thumbnails")
        if os.path.exists(p):
            try:
                shutil.rmtree(p)
                os.makedirs(p, exist_ok=True)
                self._log(f"   {_('thumb_ok')}")
            except Exception as e:
                self._log(f"   ⚠️  {e}")
        else:
            self._log(f"   {_('thumb_none')}")

    def _svuota_cestino(self):
        home = os.path.expanduser("~")
        percorsi = [
            f"{home}/.local/share/Trash/files",
            f"{home}/.local/share/Trash/info",
            f"{home}/.local/share/Trash/expunged",
            "/root/.local/share/Trash/files",
            "/root/.local/share/Trash/info",
        ]
        dimensione = 0
        for p in percorsi:
            if os.path.exists(p):
                for root, dirs, files in os.walk(p):
                    for f in files:
                        try:
                            dimensione += os.path.getsize(
                                os.path.join(root, f))
                        except Exception:
                            pass
        rimossi = 0
        for p in percorsi:
            if os.path.exists(p):
                try:
                    if p.startswith("/root/"):
                        self._esegui_comando(f"sudo rm -rf {p}/* 2>/dev/null")
                    else:
                        for el in os.listdir(p):
                            full = os.path.join(p, el)
                            try:
                                if os.path.isdir(full):
                                    shutil.rmtree(full, ignore_errors=True)
                                else:
                                    os.remove(full)
                                rimossi += 1
                            except Exception:
                                pass
                except Exception:
                    pass
        if dimensione > 0:
            self._log(f"   {_('trash_ok')} "
                      f"({self._bytes_a_human(dimensione)})")
        elif rimossi > 0:
            self._log(f"   {_('trash_ok')} ({rimossi} elementi)")
        else:
            self._log(f"   {_('trash_empty')}")

    def _gestisci_kernel(self):
        try:
            r = subprocess.run(["uname", "-r"],
                               capture_output=True, text=True, timeout=5)
            kernel_attuale = r.stdout.strip()
        except Exception:
            self._log("   ⚠️  Impossibile rilevare kernel attuale")
            return
        self._log(f"   {_('kernels_current', kernel_attuale)}")
        r = subprocess.run(
            "dpkg --list | grep -E '^ii  linux-(image|headers|modules)' "
            "| awk '{print $2}'",
            shell=True, capture_output=True, text=True, timeout=15)
        tutti = [k.strip() for k in (r.stdout or "").split("\n") if k.strip()]
        self._log(f"   {_('kernels_found', len(tutti))}")
        da_rimuovere = []
        for pkg in tutti:
            if kernel_attuale in pkg or kernel_attuale.replace("-generic", "") in pkg:
                continue
            da_rimuovere.append(pkg)
        if da_rimuovere:
            da_rimuovere = sorted(da_rimuovere)[:-1]
        if not da_rimuovere:
            self._log(f"   {_('kernels_none')}")
            return
        versioni = {}
        for pkg in da_rimuovere:
            for pref in ["linux-image-", "linux-headers-", "linux-modules-"]:
                if pkg.startswith(pref):
                    ver = pkg[len(pref):]
                    versioni.setdefault(ver, []).append(pkg)
                    break
        for ver, pkgs in sorted(versioni.items()):
            self._log(f"   {_('kernels_remove', ver)}")
            cmd = "sudo apt-get purge -y " + " ".join(pkgs)
            ok, out = self._esegui_comando(cmd, timeout=300)
            if ok:
                self._log(f"      ✅ OK")
            else:
                self._log(f"      ⚠️  {out[:200]}")

    def analizza_disco(self):
        win = tk.Toplevel(self.root)
        win.title(_("disk_title"))
        win.geometry("660x580")
        win.configure(bg="#2c3e50")
        win.transient(self.root)

        tk.Label(win, text=_("disk_title"), font=("Ubuntu", 15, "bold"),
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=(12, 5))
        lbl_stato = tk.Label(win, text=_("disk_analyzing"),
                             font=("Ubuntu", 10, "italic"),
                             bg="#2c3e50", fg="#f39c12")
        lbl_stato.pack(pady=4)

        frame_txt = tk.Frame(win, bg="#2c3e50")
        frame_txt.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        txt = tk.Text(frame_txt, wrap=tk.NONE, font=("Ubuntu Mono", 9),
                      bg="#1c2833", fg="#ecf0f1", relief="flat")
        txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb = tk.Scrollbar(frame_txt, command=txt.yview, width=12,
                          relief="flat", bd=0)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        txt.config(yscrollcommand=sb.set)

        txt.insert(tk.END, f"{_('disk_path'):<45} {_('disk_size'):>12}\n")
        txt.insert(tk.END, "─" * 60 + "\n")

        def analizza():
            home = os.path.expanduser("~")
            percorsi = [
                ("/var/log", "/var/log"),
                ("/var/cache/apt", "/var/cache/apt"),
                ("/var/cache", "/var/cache"),
                ("/var/lib/snapd", "/var/lib/snapd"),
                ("/var/lib/docker", "/var/lib/docker"),
                ("/usr/lib", "/usr/lib"),
                ("/usr/share", "/usr/share"),
                ("/opt", "/opt"),
                (f"{home}/.cache", "~/.cache"),
                (f"{home}/.local/share/Trash", "~/.local/share/Trash"),
                (f"{home}/Downloads", "~/Downloads"),
                (f"{home}/.mozilla", "~/.mozilla"),
                (f"{home}/.config/google-chrome", "~/.config/google-chrome"),
                (f"{home}/.config/BraveSoftware", "~/.config/BraveSoftware"),
                ("/tmp", "/tmp"),
                ("/snap", "/snap"),
            ]
            risultati = []
            for percorso, etichetta in percorsi:
                if not os.path.exists(percorso):
                    continue
                try:
                    r = subprocess.run(["du", "-sb", percorso],
                                       capture_output=True, text=True,
                                       timeout=60)
                    if r.returncode == 0:
                        size = int(r.stdout.split()[0])
                        risultati.append((etichetta, size))
                except Exception:
                    pass
            risultati.sort(key=lambda x: x[1], reverse=True)
            for etichetta, size in risultati:
                txt.insert(tk.END, f"{etichetta:<45} "
                                   f"{self._bytes_a_human(size):>12}\n")
            totale = sum(r[1] for r in risultati)
            txt.insert(tk.END, "─" * 60 + "\n")
            txt.insert(tk.END, f"{_('disk_total'):<45} "
                               f"{self._bytes_a_human(totale):>12}\n")
            lbl_stato.config(text=_("disk_done"), fg="#2ecc71")

        threading.Thread(target=analizza, daemon=True).start()
        tk.Button(win, text=_("disk_close"), font=("Ubuntu", 10, "bold"),
                  bg="#7f8c8d", fg="white", relief="flat", width=14,
                  cursor="hand2", command=win.destroy).pack(pady=10)

    def salva_report(self):
        if not self.report_lines:
            return
        nome = f"report_pulizia_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        percorso = filedialog.asksaveasfilename(
            title=_("save_dialog_title"), initialfile=nome,
            defaultextension=".txt",
            filetypes=[("Testo", "*.txt"), ("Tutti", "*.*")])
        if not percorso:
            return
        try:
            with open(percorso, "w", encoding="utf-8") as f:
                f.write("\n".join(self.report_lines))
            messagebox.showinfo("OK", _("save_ok", percorso))
        except Exception as e:
            messagebox.showerror(_("error_title"), str(e))

    def copia_report(self):
        if not self.report_lines:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append("\n".join(self.report_lines))
        messagebox.showinfo("OK", _("copy_ok"))

    # --- GUIDA ---
    def apri_guida(self):
        win = tk.Toplevel(self.root)
        win.title(_("help_title"))
        win.configure(bg="#2c3e50")
        win.transient(self.root)
        win.minsize(800, 560)

        tk.Label(win, text=_("help_title"), font=("Ubuntu", 15, "bold"),
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=(12, 6))

        frame_main = tk.Frame(win, bg="#2c3e50")
        frame_main.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        frame_index = tk.Frame(frame_main, bg="#34495e", width=210)
        frame_index.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 8))
        frame_index.pack_propagate(False)
        tk.Label(frame_index, text=_("help_index"),
                 font=("Ubuntu", 10, "bold"),
                 bg="#34495e", fg="#ecf0f1").pack(pady=6)

        listbox = tk.Listbox(frame_index, font=("Ubuntu", 10),
                             bg="#1c2833", fg="#ecf0f1",
                             selectbackground="#27ae60",
                             selectforeground="white",
                             relief="flat", bd=0, highlightthickness=0,
                             activestyle="none", cursor="hand2")
        listbox.pack(fill=tk.BOTH, expand=True, padx=6, pady=(0, 6))

        frame_content = tk.Frame(frame_main, bg="#2c3e50")
        frame_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        txt = tk.Text(frame_content, wrap=tk.WORD, font=("Ubuntu", 10),
                      bg="#1c2833", fg="#ecf0f1",
                      insertbackground="white", relief="flat",
                      padx=15, pady=12, cursor="arrow")
        txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb = tk.Scrollbar(frame_content, command=txt.yview, width=12,
                          relief="flat", bd=0)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        txt.config(yscrollcommand=sb.set)

        txt.tag_configure("section", font=("Ubuntu", 14, "bold"),
                          foreground="#2ecc71", spacing1=15, spacing3=8)
        txt.tag_configure("body", font=("Ubuntu", 10),
                          foreground="#ecf0f1",
                          lmargin1=10, lmargin2=10, spacing1=3, spacing3=3)
        txt.tag_configure("bullet", font=("Ubuntu", 10),
                          foreground="#f39c12",
                          lmargin1=25, lmargin2=40, spacing1=2, spacing3=2)
        txt.tag_configure("code", font=("Ubuntu Mono", 9),
                          foreground="#1abc9c", background="#2c3e50",
                          lmargin1=40, lmargin2=40, spacing1=1, spacing3=1)

        sezioni = GUIDE_CONTENT.get(CURRENT_LANG, GUIDE_CONTENT["en"])
        markers = []
        for titolo, contenuto in sezioni:
            marker = f"sec_{len(markers)}"
            txt.mark_set(marker, tk.END)
            markers.append(marker)
            txt.insert(tk.END, f"▶ {titolo}\n", "section")
            for riga in contenuto.strip().split("\n"):
                if not riga.strip():
                    txt.insert(tk.END, "\n")
                elif riga.strip()[:1] in "•✓❌📋💾⚠️" or \
                        riga.strip()[:2] in ("D:", "R:", "Q:", "A:"):
                    txt.insert(tk.END, "  " + riga + "\n", "bullet")
                elif riga.strip().startswith(("sudo", "systemctl", "cat ",
                                              "/usr", "groups", "apt-",
                                              "/etc", "/var", "rm ",
                                              "notify-", "grep", "python3",
                                              "du ")):
                    txt.insert(tk.END, "      " + riga.strip() + "\n", "code")
                else:
                    txt.insert(tk.END, riga + "\n", "body")
            txt.insert(tk.END, "\n")
            listbox.insert(tk.END, f"  {titolo}")

        def vai(event=None):
            sel = listbox.curselection()
            if sel and 0 <= sel[0] < len(markers):
                txt.see(markers[sel[0]])
        listbox.bind("<<ListboxSelect>>", vai)
        listbox.bind("<Return>", vai)
        listbox.selection_set(0)

        tk.Button(win, text=_("help_close"), font=("Ubuntu", 10, "bold"),
                  bg="#7f8c8d", fg="white", relief="flat", width=14,
                  height=2, cursor="hand2",
                  command=win.destroy).pack(pady=10)
        win.bind("<Escape>", lambda e: win.destroy())

        win.update_idletasks()
        win.geometry("")
        win.update_idletasks()
        larg = max(win.winfo_reqwidth(), 820)
        alt = max(win.winfo_reqheight(), 620)
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        win.geometry(f"{larg}x{alt}+{(sw-larg)//2}+{(sh-alt)//2}")
        win.focus_set()

    # --- CRON ---
    def _cron_service_attivo(self):
        try:
            r = subprocess.run(["systemctl", "is-active", "cron"],
                               capture_output=True, text=True, timeout=5)
            s = (r.stdout or "").strip().lower()
            if s == "active":
                return True
            if s in ("inactive", "failed", "deactivating"):
                return False
            r2 = subprocess.run(["systemctl", "is-enabled", "cron"],
                                capture_output=True, text=True, timeout=5)
            e = (r2.stdout or "").strip().lower()
            if e == "enabled":
                return True
            if e in ("disabled", "masked"):
                return False
            return None
        except Exception:
            return None

    def apri_schedulazione(self):
        cron_file = "/etc/cron.d/pulizia-ubuntu"
        win = tk.Toplevel(self.root)
        win.title(_("sched_title"))
        win.configure(bg="#2c3e50")
        win.transient(self.root)
        win.grab_set()
        win.resizable(False, False)
        win.minsize(560, 600)

        tk.Label(win, text=_("sched_title"), font=("Ubuntu", 15, "bold"),
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=(15, 5))
        tk.Label(win, text=_("sched_desc"), font=("Ubuntu", 9, "italic"),
                 bg="#2c3e50", fg="#95a5a6",
                 justify="center").pack(pady=(0, 10))

        # Stato servizio
        fs = tk.LabelFrame(win, text=" " + _("sched_service_title") + " ",
                           font=("Ubuntu", 10, "bold"),
                           bg="#34495e", fg="#ecf0f1", bd=2, relief="groove")
        fs.pack(fill=tk.X, padx=20, pady=6)

        cron_attivo = self._cron_service_attivo()
        if cron_attivo is None:
            t_serv, c_serv = _("sched_service_unknown"), "#e67e22"
        elif cron_attivo:
            t_serv, c_serv = _("sched_service_active"), "#2ecc71"
        else:
            t_serv, c_serv = _("sched_service_inactive"), "#e74c3c"

        lbl_serv = tk.Label(fs, text=t_serv, font=("Ubuntu", 10, "bold"),
                            bg="#34495e", fg=c_serv, anchor="w")
        lbl_serv.pack(fill=tk.X, padx=10, pady=(8, 2))

        voce = os.path.exists(cron_file)
        t_voce = _("sched_entry_active") if voce else _("sched_entry_inactive")
        c_voce = "#2ecc71" if voce else "#95a5a6"
        lbl_voce = tk.Label(fs, text=t_voce, font=("Ubuntu", 10, "bold"),
                            bg="#34495e", fg=c_voce, anchor="w")
        lbl_voce.pack(fill=tk.X, padx=10, pady=(2, 8))

        fb = tk.Frame(fs, bg="#34495e")
        fb.pack(pady=(0, 10), padx=10, fill=tk.X)

        def agg_stato():
            a = self._cron_service_attivo()
            if a is None:
                lbl_serv.config(text=_("sched_service_unknown"), fg="#e67e22")
            elif a:
                lbl_serv.config(text=_("sched_service_active"), fg="#2ecc71")
            else:
                lbl_serv.config(text=_("sched_service_inactive"), fg="#e74c3c")
            if os.path.exists(cron_file):
                lbl_voce.config(text=_("sched_entry_active"), fg="#2ecc71")
            else:
                lbl_voce.config(text=_("sched_entry_inactive"), fg="#95a5a6")
            btn_en.config(state=tk.NORMAL if a is False else tk.DISABLED)
            btn_di.config(state=tk.NORMAL if a is True else tk.DISABLED)

        def abilita():
            if not self._assicura_sudo():
                return
            ok, out = self._esegui_comando("sudo systemctl enable --now cron")
            if ok:
                messagebox.showinfo(_("sched_service_title"),
                                    _("sched_service_enabled"))
                agg_stato()
            else:
                messagebox.showerror(_("error_title"), out)

        def disabilita():
            if not messagebox.askyesno(_("confirm_title"),
                                       _("sched_service_disable_confirm")):
                return
            if not self._assicura_sudo():
                return
            ok, out = self._esegui_comando(
                "sudo systemctl stop cron && sudo systemctl disable cron")
            if ok:
                messagebox.showinfo(_("sched_service_title"),
                                    _("sched_service_disabled"))
                agg_stato()
            else:
                messagebox.showerror(_("error_title"), out)

        btn_en = tk.Button(fb, text=_("sched_service_enable"),
                           font=("Ubuntu", 9, "bold"),
                           bg="#27ae60", fg="white", relief="flat",
                           cursor="hand2", width=18, command=abilita)
        btn_di = tk.Button(fb, text=_("sched_service_disable"),
                           font=("Ubuntu", 9, "bold"),
                           bg="#c0392b", fg="white", relief="flat",
                           cursor="hand2", width=18, command=disabilita)
        btn_en.pack(side=tk.LEFT, padx=5)
        btn_di.pack(side=tk.LEFT, padx=5)
        if cron_attivo is True:
            btn_en.config(state=tk.DISABLED)
        elif cron_attivo is False:
            btn_di.config(state=tk.DISABLED)

        # Configurazione
        fc = tk.LabelFrame(win, text=" " + _("sched_config_title") + " ",
                           font=("Ubuntu", 10, "bold"),
                           bg="#34495e", fg="#ecf0f1", bd=2, relief="groove")
        fc.pack(fill=tk.X, padx=20, pady=6)
        inner = tk.Frame(fc, bg="#34495e")
        inner.pack(padx=15, pady=10, fill=tk.X)

        tk.Label(inner, text=_("sched_freq") + ":",
                 font=("Ubuntu", 10, "bold"),
                 bg="#34495e", fg="#ecf0f1").grid(
            row=0, column=0, sticky="w", pady=(4, 2))
        freq_var = tk.StringVar(value="weekly")
        ffr = tk.Frame(inner, bg="#34495e")
        ffr.grid(row=1, column=0, columnspan=2, sticky="w", padx=20,
                 pady=(0, 8))
        for val, key in [("daily", "sched_daily"),
                         ("weekly", "sched_weekly"),
                         ("monthly", "sched_monthly")]:
            tk.Radiobutton(ffr, text=_(key), variable=freq_var, value=val,
                           font=("Ubuntu", 10),
                           bg="#34495e", fg="#ecf0f1",
                           selectcolor="#34495e",
                           activebackground="#34495e",
                           activeforeground="#1abc9c",
                           anchor="w", cursor="hand2").pack(fill=tk.X, pady=1)

        tk.Label(inner, text=_("sched_time") + ":",
                 font=("Ubuntu", 10, "bold"),
                 bg="#34495e", fg="#ecf0f1").grid(
            row=2, column=0, sticky="w", pady=(4, 2))
        ora_var = tk.StringVar(value="3")
        tk.Spinbox(inner, from_=0, to=23, textvariable=ora_var, width=5,
                   font=("Ubuntu", 10), bg="#1c2833", fg="#ecf0f1",
                   buttonbackground="#2c3e50", relief="flat",
                   insertbackground="white").grid(
            row=2, column=1, sticky="w", padx=8, pady=(4, 2))

        tk.Label(inner, text=_("sched_day") + ":",
                 font=("Ubuntu", 10, "bold"),
                 bg="#34495e", fg="#ecf0f1").grid(
            row=3, column=0, sticky="w", pady=(4, 2))
        giorni = [("0", "sched_sun"), ("1", "sched_mon"), ("2", "sched_tue"),
                  ("3", "sched_wed"), ("4", "sched_thu"), ("5", "sched_fri"),
                  ("6", "sched_sat")]
        combo = ttk.Combobox(inner, state="readonly", width=20,
                             font=("Ubuntu", 10),
                             values=[f"{g[0]} - {_(g[1])}" for g in giorni])
        combo.current(1)
        combo.grid(row=3, column=1, sticky="w", padx=8, pady=(4, 2))

        tk.Label(win, text=_("sched_note"), font=("Ubuntu", 8, "italic"),
                 bg="#2c3e50", fg="#95a5a6", wraplength=520,
                 justify="left").pack(pady=6, padx=20)

        def salva():
            freq = freq_var.get()
            try:
                ora = int(ora_var.get())
                if not 0 <= ora <= 23:
                    raise ValueError()
            except ValueError:
                messagebox.showerror(_("error_title"), _("sched_err_time"))
                return
            gt = combo.get()
            g = gt.split(" - ")[0] if " - " in gt else "0"
            if freq == "daily":
                expr = f"0 {ora} * * *"
            elif freq == "weekly":
                expr = f"0 {ora} * * {g}"
            else:
                expr = f"0 {ora} 1 * *"
            if not self._assicura_sudo():
                return
            self._installa_cron(expr, win)

        def rimuovi():
            if not os.path.exists(cron_file):
                messagebox.showinfo(_("sched_title"),
                                    _("sched_entry_inactive"))
                return
            if not messagebox.askyesno(_("sched_remove_confirm_title"),
                                       _("sched_remove_confirm_msg")):
                return
            if not self._assicura_sudo():
                return
            self._rimuovi_cron(win)

        fbt = tk.Frame(win, bg="#2c3e50")
        fbt.pack(pady=10)
        tk.Button(fbt, text=_("sched_save"), font=("Ubuntu", 10, "bold"),
                  bg="#27ae60", fg="white", relief="flat", width=14,
                  height=2, cursor="hand2", command=salva).pack(
            side=tk.LEFT, padx=4)
        tk.Button(fbt, text=_("sched_remove"), font=("Ubuntu", 10, "bold"),
                  bg="#c0392b", fg="white", relief="flat", width=14,
                  height=2, cursor="hand2", command=rimuovi).pack(
            side=tk.LEFT, padx=4)
        tk.Button(fbt, text=_("sched_close"), font=("Ubuntu", 10),
                  bg="#7f8c8d", fg="white", relief="flat", width=10,
                  height=2, cursor="hand2", command=win.destroy).pack(
            side=tk.LEFT, padx=4)

        win.update_idletasks()
        win.geometry("")
        win.update_idletasks()
        larg = max(win.winfo_reqwidth(), 560)
        alt = max(win.winfo_reqheight(), 600)
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        win.geometry(f"{larg}x{alt}+{(sw-larg)//2}+{(sh-alt)//2}")

    def _installa_cron(self, espressione, finestra):
        script_content = r'''#!/bin/bash
LOG=/var/log/pulizia_ubuntu.log
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === Inizio pulizia ===" >> "$LOG"
PRIMA=$(df -B1 / | tail -1 | awk '{print $4}')
apt-get autoremove --purge -y >> "$LOG" 2>&1
apt-get clean >> "$LOG" 2>&1
apt-get autoclean >> "$LOG" 2>&1
journalctl --vacuum-time=3d >> "$LOG" 2>&1
if command -v snap &>/dev/null; then
    snap list --all 2>/dev/null | awk '/disabled/{print $1, $3}' | \
    while read nome rev; do
        [ -n "$nome" ] && [ -n "$rev" ] && \
            snap remove "$nome" --revision="$rev" >> "$LOG" 2>&1
    done
fi
find /tmp -type f -atime +7 -delete 2>/dev/null
find /var/tmp -type f -atime +30 -delete 2>/dev/null
DOPO=$(df -B1 / | tail -1 | awk '{print $4}')
LIBERATO=$(( DOPO - PRIMA ))
if [ "$LIBERATO" -gt 0 ]; then
    LIB=$(numfmt --to=iec --suffix=B "$LIBERATO" 2>/dev/null || echo "${LIBERATO}B")
else
    LIB="0B"
fi
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Completata. Liberati: $LIB" >> "$LOG"
UTENTE=$(who | grep -v root | head -1 | awk '{print $1}')
if [ -n "$UTENTE" ]; then
    UID_U=$(id -u "$UTENTE" 2>/dev/null)
    DISP=$(who | grep "^$UTENTE " | grep -o ':[0-9.]*' | head -1)
    [ -z "$DISP" ] && DISP=":0"
    [ -n "$UID_U" ] && runuser -u "$UTENTE" -- env DISPLAY="$DISP" \
        DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$UID_U/bus" \
        notify-send -i pulizia-ubuntu -a "Pulizia Ubuntu" -t 10000 \
        "Pulizia automatica completata" "Spazio liberato: $LIB" 2>/dev/null
fi
echo "" >> "$LOG"
'''
        try:
            tmp = "/tmp/pulizia_cron_tmp.sh"
            with open(tmp, "w") as f:
                f.write(script_content)
            os.chmod(tmp, 0o755)
        except Exception as e:
            messagebox.showerror(_("error_title"), str(e))
            return
        ok, out = self._esegui_comando(
            f"sudo mv {tmp} /usr/local/bin/pulizia_ubuntu_cron.sh && "
            f"sudo chmod 755 /usr/local/bin/pulizia_ubuntu_cron.sh")
        if not ok:
            messagebox.showerror(_("error_title"), out)
            return
        cron_content = ("# Pulizia automatica Ubuntu\n"
                        "SHELL=/bin/bash\n"
                        "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:"
                        "/usr/sbin:/usr/bin\n"
                        f"{espressione} root "
                        "/usr/local/bin/pulizia_ubuntu_cron.sh\n")
        try:
            tmp_c = "/tmp/pulizia_cron_tmp.cron"
            with open(tmp_c, "w") as f:
                f.write(cron_content)
        except Exception as e:
            messagebox.showerror(_("error_title"), str(e))
            return
        ok, out = self._esegui_comando(
            f"sudo mv {tmp_c} /etc/cron.d/pulizia-ubuntu && "
            f"sudo chmod 644 /etc/cron.d/pulizia-ubuntu")
        if not ok:
            messagebox.showerror(_("error_title"), out)
            return
        messagebox.showinfo(_("sched_ok_title"),
                            _("sched_ok_msg", espressione))
        finestra.destroy()

    def _rimuovi_cron(self, finestra):
        ok, out = self._esegui_comando(
            "sudo rm -f /etc/cron.d/pulizia-ubuntu "
            "/usr/local/bin/pulizia_ubuntu_cron.sh")
        if ok:
            messagebox.showinfo(_("sched_removed_title"),
                                _("sched_removed_msg"))
            finestra.destroy()
        else:
            messagebox.showerror(_("error_title"), out)

    def _invia_notifica(self, titolo, messaggio):
        try:
            subprocess.Popen(
                ["notify-send", "-i", "pulizia-ubuntu", "-a", APP_NAME,
                 "-t", "8000", titolo, messaggio],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            debug_log(f"notify err: {e}")

    def _set_pulsanti(self, abilitato):
        stato = tk.NORMAL if abilitato else tk.DISABLED
        self.btn_esegui.config(state=stato)
        self.btn_esci.config(state=stato)
        self.btn_schedula.config(state=stato)
        self.btn_disco.config(state=stato)
        self.btn_guida.config(state=stato)

    def esci(self):
        if self.in_esecuzione:
            messagebox.showwarning("⏳", _("exit_running"))
            return
        if messagebox.askyesno(_("exit_title"), _("exit_msg")):
            self.password_sudo = None
            self.root.destroy()


if __name__ == "__main__":
    debug_log("--- Avvio main ---")
    root = tk.Tk()
    app = PuliziaApp(root)
    root.mainloop()
    debug_log("--- Chiusura app ---")
