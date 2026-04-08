# Changelog

All notable changes to WiFuX are documented in this file.

---

## v2.0 — 2026

### Core Engine

- Rewrote the main engine (`main.py`) from scratch with improved architecture
- Replaced the monolithic v1 script with a structured, modular codebase
- Added `NetworkAddress` class for clean MAC address handling
- Improved WPS handshake handling and socket timeout management
- Fixed zombie process accumulation during long attack sessions
- Fixed session resume logic that caused incorrect PIN offset on restart
- Improved wpa_supplicant lifecycle management to prevent crashes

### Global Command System

- Added `wifux` as a globally registered Termux command via `$PREFIX/bin`
- `wifux` — run with default settings (wlan0 + Pixie Dust)
- `wifux menu` — open interactive menu without triggering auto-attack
- `wifux old` — run the legacy v1 engine (w1.py) for compatibility
- `wifux update` — pull latest updates from GitHub and re-apply setup
- `wifux help` — open the built-in interactive help guide
- `wifux fix` — launch the root/superuser repair script
- `wifux contact` — open the developer contact menu

### Installer

- Added `installer.sh` — one-command fresh install from GitHub
- Added `install.sh` — local setup script for manual installs and updates
- Both installers display a post-install command reference panel
- `wifux update` internally re-runs `install.sh` to keep the command fresh

### Built-in Help Guide (`help.py`)

- Added `help.py` — a full interactive help guide with 9 sections
- Section 1: What is WiFuX — introduction and overview
- Section 2: Installation steps
- Section 3: How to find your WiFi interface
- Section 4: All attack modes explained (Pixie Dust, Bruteforce, PBC)
- Section 5: Full command argument reference (A-Z)
- Section 6: Copy-paste usage examples
- Section 7: Troubleshooting common errors
- Section 8: Warnings and legal notice
- Section 9: Quick reference for all `wifux` commands

### Contact (`contact.py`)

- Added `contact.py` — interactive menu to open social media links in browser
- Supports: Facebook, Instagram, Telegram, GitHub, Telegram Group
- Uses `termux-open-url` with fallback to `xdg-open`

### Root Fix (`fix.sh`)

- Added `fix.sh` — automated root/superuser repair for Termux
- Removes conflicting `tsu` binaries
- Installs `sudo` framework
- Scans known root binary paths (Magisk, KernelSU, system xbin, etc.)
- Offers to launch a root shell if a valid binary is found

### Attack Features (new in v2)

- Added session save and resume (`--list-sessions`, `--resume-session`)
- Added HTML, CSV, and JSON report generation
- Added MAC address changing per attempt (`-M`)
- Added recurring delay support (`--recurring-delay X:Y`)
- Added signal analysis before attack (`--signal-analysis`)
- Added vulnerability check before attack (`--check-vuln`)
- Added Pixie Dust vulnerable router list (`--pixie-list`)
- Added full router model database viewer (`--list-all-models`)
- Added auto vulnerable device tracking (`--auto-vuln-list`)
- Added rfkill auto-unblock (`--handle-rfkill`)
- Added MediaTek WiFi driver support (`--mtk-wifi`)
- Added weak WPS algorithm detection (`--detect-weak-algo`)

### UI and Output

- Redesigned banner and startup output
- Added color-coded status indicators throughout
- Cleaner scan table layout for network listing
- Consistent progress display during attacks

---

## v1.0 — 2025

- Initial release
- Basic Pixie Dust and Bruteforce attack support
- Single-file script (`w1.py`) based on the OneShot WPS framework
- Termux / Android compatible
- No global command — required manual `python w1.py` invocation
- No session management
- No reporting
- No built-in help system
