#!/usr/bin/env python3
# ─────────────────────────────────────────────
#  WiFuX Help Guide — by MSR
#  Run: wifux help
# ─────────────────────────────────────────────

import sys
import os
import time

# ── Colors ──────────────────────────────────
R  = '\033[1;31m'   # red
G  = '\033[1;32m'   # green
Y  = '\033[1;33m'   # yellow
B  = '\033[1;34m'   # blue
M  = '\033[1;35m'   # magenta
C  = '\033[1;36m'   # cyan
W  = '\033[1;37m'   # white
RS = '\033[0m'       # reset

# ── Symbols ─────────────────────────────────
OK   = f'{G}[{W}+{G}]{RS}'
INFO = f'{B}[{W}i{B}]{RS}'
WARN = f'{Y}[{W}!{Y}]{RS}'
TIP  = f'{M}[{W}★{M}]{RS}'
CMD  = f'{C}[{W}>{C}]{RS}'

LINE  = f'{C}{"━"*52}{RS}'
LINE2 = f'{B}{"─"*52}{RS}'

# ────────────────────────────────────────────
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def pause():
    input(f'\n{INFO} {W}Press Enter to go back to menu...{RS}')

def banner():
    print(f'''\033[1;32m
██╗    ██╗██╗███████╗██╗   ██╗██╗  ██╗
██║    ██║██║██╔════╝██║   ██║╚██╗██╔╝
██║ █╗ ██║██║█████╗  ██║   ██║ ╚███╔╝
██║███╗██║██║██╔══╝  ██║   ██║ ██╔██╗
╚███╔███╔╝██║██║     ╚██████╔╝██╔╝ ██╗
 ╚══╝╚══╝ ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝\033[0m
{C}         Help Guide — v2.0{RS}
{M}         ★ Stay With MSR{RS}
''')

# ────────────────────────────────────────────
def show_menu():
    clear()
    banner()
    print(f'''{LINE}
{Y}  What do you want to know? Pick a number:{RS}
{LINE}

  {G}1{RS}  →  {W}What is WiFuX? Introduction{RS}
  {G}2{RS}  →  {W}How to Install / Setup{RS}
  {G}3{RS}  →  {W}What is an Interface & how to find it{RS}
  {G}4{RS}  →  {W}All Attack Modes explained{RS}
  {G}5{RS}  →  {W}Full Command List (A-Z){RS}
  {G}6{RS}  →  {W}Usage Examples (Copy-Paste ready){RS}
  {G}7{RS}  →  {W}Troubleshooting common errors{RS}
  {G}8{RS}  →  {W}Important warnings & rules{RS}
  {G}9{RS}  →  {W}Available wifux commands (quick reference){RS}

  {R}0{RS}  →  {W}Exit{RS}

{LINE}''')
    return input(f'  {C}Your choice: {RS}').strip()

# ────────────────────────────────────────────
def section_intro():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  1. What is WiFuX — Introduction{RS}
{LINE}

{INFO} {W}WiFuX{RS} is a WPS (Wi-Fi Protected Setup)
   security testing tool that runs in Termux.

{INFO} It lets you test WPS vulnerabilities
   on your own router.

{LINE2}
{Y}  What is WPS?{RS}
{LINE2}

  WPS is a router feature that allows
  connecting to WiFi using an 8-digit PIN.
  Many older routers have PINs that can be
  easily extracted — that's what WiFuX tests.

{LINE2}
{Y}  What can WiFuX do?{RS}
{LINE2}

  {G}✔{RS} Pixie Dust Attack    — fast PIN extraction
  {G}✔{RS} Bruteforce Attack    — try all PINs step by step
  {G}✔{RS} Network Scanner      — scan nearby WiFi networks
  {G}✔{RS} Session Save/Resume  — pause & resume attacks
  {G}✔{RS} HTML/CSV/JSON Report — save results to file

{TIP} {M}Only test your own network — never others'.{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_install():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  2. How to Install / Setup{RS}
{LINE}

{INFO} Run these commands one by one in Termux:

{LINE2}
{Y}  Step 1 — Update Termux packages{RS}
{LINE2}

{CMD} {C}pkg update && pkg upgrade{RS}

{LINE2}
{Y}  Step 2 — Install required packages{RS}
{LINE2}

{CMD} {C}pkg install python root-repo{RS}
{CMD} {C}pkg install wpa-supplicant pixiewps{RS}
{CMD} {C}pkg install wireless-tools iw{RS}

{LINE2}
{Y}  Step 3 — Run WiFuX{RS}
{LINE2}

{CMD} {C}cd /path/to/wifux/folder{RS}
{CMD} {C}python main.py -i wlan0{RS}

{LINE2}
{Y}  Step 4 — Make sure you have root access{RS}
{LINE2}

  WiFuX requires root to run.
  In Termux:

{CMD} {C}su{RS}        ← get root
{CMD} {C}python main.py -i wlan0{RS}

{TIP} {M}Without root you will see: "Run it as root" error.{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_interface():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  3. What is an Interface & how to find it{RS}
{LINE}

{INFO} Interface is the name of your WiFi card.
   Usually it is: {G}wlan0{RS}, {G}wlan1{RS}, or {G}wlan2{RS}

{LINE2}
{Y}  Commands to find your interface:{RS}
{LINE2}

{CMD} {C}ip link show{RS}
   ↳ Shows all network interfaces

{CMD} {C}iwconfig{RS}
   ↳ Shows only WiFi interfaces

{CMD} {C}iw dev{RS}
   ↳ Detailed WiFi info

{LINE2}
{Y}  Output will look like this:{RS}
{LINE2}

  {W}2: wlan0: <BROADCAST,MULTICAST,UP>{RS}
       ↑
       {G}This is your interface name{RS}

{LINE2}
{Y}  Use it in WiFuX like this:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0{RS}
                     {Y}↑{RS}
              {Y}replace with your interface name{RS}

{WARN} {Y}Some devices may use wlan1 or a different name
   instead of wlan0.{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_attacks():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  4. All Attack Modes Explained{RS}
{LINE}

{LINE2}
{G}  ★ Pixie Dust Attack  (-K){RS}
{LINE2}

{INFO} The fastest attack. Extracts the PIN offline
   from the router's WPS handshake data.
   Can finish in just a few seconds if successful.

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}

  {G}✔{RS} Very fast   {R}✗{RS} Doesn't work on all routers

{LINE2}
{G}  ★ Bruteforce Attack  (-B){RS}
{LINE2}

{INFO} Tries all possible PINs one by one (up to 11000).
   Has a chance to work on any WPS-enabled router.

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}

  {G}✔{RS} Works on more routers
  {R}✗{RS} Can take a very long time (hours)

{LINE2}
{G}  ★ Auto Scan + Attack  (no BSSID){RS}
{LINE2}

{INFO} Scans and lists all nearby WPS networks.
   You pick one, then the attack starts.

{CMD} {C}python main.py -i wlan0 -K{RS}

{LINE2}
{G}  ★ Push Button Connect  (--pbc){RS}
{LINE2}

{INFO} Attempts to connect when you press the
   WPS button on the router.

{CMD} {C}python main.py -i wlan0 --pbc{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_commands():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  5. Full Command Argument List (A-Z){RS}
{LINE}

{Y}  ─── Required ───{RS}
  {G}-i{RS}, {G}--interface{RS}   WiFi interface name (e.g. wlan0)

{Y}  ─── Target ───{RS}
  {G}-b{RS}, {G}--bssid{RS}       Router MAC address (AA:BB:CC:DD:EE:FF)
  {G}-p{RS}, {G}--pin{RS}         Try a specific PIN

{Y}  ─── Attack Mode ───{RS}
  {G}-K{RS}, {G}--pixie-dust{RS}  Run Pixie Dust attack
  {G}-F{RS}, {G}--pixie-force{RS} Pixie Dust full range (slower but stronger)
  {G}-B{RS}, {G}--bruteforce{RS}  Run Bruteforce attack
  {G}--pbc{RS}             Push Button Connect

{Y}  ─── Timing ───{RS}
  {G}-d{RS}, {G}--delay{RS}       Delay between attempts (seconds)
  {G}-t{RS}, {G}--timeout{RS}     WPS response wait time [10s]
  {G}-T{RS}, {G}--m57-timeout{RS} M5/M7 message timeout [0.40s]
  {G}--lock-delay{RS}     Wait time when router is locked [60s]
  {G}--fail-wait{RS}      Pause after 10 failures (seconds)
  {G}--recurring-delay{RS} Pause Y seconds every X attempts (X:Y)

{Y}  ─── Bruteforce Control ───{RS}
  {G}-g{RS}, {G}--max-attempts{RS} Max number of attempts [0=unlimited]
  {G}-L{RS}, {G}--ignore-locks{RS} Ignore router lock and keep going
  {G}-M{RS}, {G}--mac-changer{RS}  Change MAC address on each attempt

{Y}  ─── Session ───{RS}
  {G}--list-sessions{RS}   Show saved sessions
  {G}--resume-session{RS}  Resume a previous session (provide BSSID)

{Y}  ─── Output / Report ───{RS}
  {G}--html-report{RS}     Generate HTML report
  {G}--report-format{RS}   Report format: html / txt / csv / json
  {G}--detailed-report{RS} Include more details in report
  {G}--json-output{RS}     Save results to JSON file
  {G}--csv-output{RS}      Save results to CSV file
  {G}--log-file{RS}        Log all activity to a file

{Y}  ─── Network Scan ───{RS}
  {G}--vuln-list{RS}       File with list of vulnerable devices
  {G}--auto-vuln-list{RS}  Auto-add cracked devices to vuln list
  {G}-r{RS}, {G}--reverse-scan{RS} Reverse the network list order
  {G}--detect-weak-algo{RS} Detect routers with weak WPS algorithm
  {G}--signal-analysis{RS}  Analyze signal strength before attack
  {G}--check-vuln{RS}       Show vulnerability report before attack
  {G}--pixie-list{RS}       Show all Pixie Dust vulnerable routers
  {G}--list-all-models{RS}  Show all router models in database

{Y}  ─── Quick Launch ───{RS}\n  {G}wifux{RS}              Run with default settings (wlan0 + Pixie Dust)\n  {G}wifux menu{RS}         Open WiFuX interactive menu (no auto-attack)\n  {G}wifux old{RS}          Run old engine (w1.py) with wlan0\n  {G}wifux update{RS}       Update WiFuX to latest version\n  {G}wifux help{RS}         Show this help guide\n  {G}wifux fix{RS}          Fix root/superuser issues\n  {G}wifux contact{RS}      Contact the developer (MSR)\n\n{Y}  ─── Android / Termux ───{RS}
  {G}--dts{RS}              Don't touch Android WiFi settings
  {G}--mtk-wifi{RS}         Enable MediaTek WiFi driver
  {G}--handle-rfkill{RS}    Auto-unblock if rfkill is blocking WiFi
  {G}--iface-down{RS}       Bring interface down after finishing

{Y}  ─── Other ───{RS}
  {G}-v{RS}, {G}--verbose{RS}      Show detailed debug output
  {G}-l{RS}, {G}--loop{RS}         Restart scan after finishing
  {G}-X{RS}, {G}--show-pixie-cmd{RS} Show the pixiewps command used
  {G}--no-colors{RS}        Disable colored output
  {G}--pin-algo{RS}         Choose a specific PIN algorithm
  {G}--write-legacy{RS}     Also save in legacy format
  {G}-h{RS}, {G}--help{RS}         Show help
''')
    pause()

# ────────────────────────────────────────────
def section_examples():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  6. Usage Examples (Copy-Paste ready){RS}
{LINE}

{LINE2}
{G}  Quick start — Scan and pick a network:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -K{RS}
  ↳ Scans nearby WPS networks, pick one, runs Pixie Dust

{CMD} {C}python main.py -i wlan0 -B{RS}
  ↳ Scans nearby WPS networks, pick one, runs Bruteforce

{LINE2}
{G}  Attack a specific router:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}
  ↳ Runs Pixie Dust directly on that router

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}
  ↳ Runs Bruteforce directly on that router

{LINE2}
{G}  Two attacks — Pixie first, then Bruteforce if it fails:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}
  ↳ If Pixie Dust fails:
{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}

{LINE2}
{G}  Slow attack to avoid router lockout:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B -d 2{RS}
  ↳ 2 second delay between each attempt

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B --recurring-delay 10:30{RS}
  ↳ Pause 30 seconds after every 10 attempts

{LINE2}
{G}  Attack with MAC changing:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B -M{RS}

{LINE2}
{G}  Resume a previous session:{RS}
{LINE2}

{CMD} {C}python main.py --list-sessions{RS}
  ↳ View saved sessions

{CMD} {C}python main.py -i wlan0 --resume-session AA:BB:CC:DD:EE:FF{RS}
  ↳ Continue attack from where you left off

{LINE2}
{G}  Generate reports:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K --html-report{RS}
{CMD} {C}python main.py -i wlan0 -K --html-report --report-format json{RS}

{LINE2}
{G}  Browse the database:{RS}
{LINE2}

{CMD} {C}python main.py --pixie-list{RS}
  ↳ Which routers are Pixie Dust vulnerable

{CMD} {C}python main.py --list-all-models{RS}
  ↳ All router models in the database

{LINE2}
{G}  Safe usage on Android / Termux:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -K --dts{RS}
  ↳ Won't change Android WiFi settings

{CMD} {C}python main.py -i wlan0 -K --handle-rfkill{RS}
  ↳ Auto-unblocks WiFi if rfkill is blocking it

{LINE2}
{G}  Signal analysis before attacking:{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 --signal-analysis -B{RS}

{LINE2}
{G}  Verbose mode (see everything):{RS}
{LINE2}

{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K -v{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_troubleshoot():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  7. Troubleshooting Common Errors{RS}
{LINE}

{LINE2}
{R}  ✗  "Run it as root" error{RS}
{LINE2}

  Cause: Running without root access
  Fix:
{CMD} {C}su{RS}
{CMD} {C}python main.py -i wlan0 -K{RS}

{LINE2}
{R}  ✗  "Unable to up interface" error{RS}
{LINE2}

  Cause: Wrong interface name or WiFi is off
  Fix:
{CMD} {C}ip link show{RS}          ← find the correct interface name
{CMD} {C}ip link set wlan0 up{RS}  ← bring the interface up

{LINE2}
{R}  ✗  wpa_supplicant error / crash{RS}
{LINE2}

  Cause: A previous instance is still running
  Fix:
{CMD} {C}pkill wpa_supplicant{RS}
{CMD} {C}python main.py -i wlan0 -K{RS}

{LINE2}
{R}  ✗  "WiFi is rfkill blocked" error{RS}
{LINE2}

  Cause: WiFi is blocked by rfkill
  Fix:
{CMD} {C}python main.py -i wlan0 -K --handle-rfkill{RS}
  or:
{CMD} {C}rfkill unblock wifi{RS}

{LINE2}
{R}  ✗  No WPS networks found{RS}
{LINE2}

  Try:
  • Move closer to the router
  • Turn Location off on Android
  • Toggle WiFi off and back on
  • Run with {C}--dts{RS} flag

{LINE2}
{R}  ✗  Pixie Dust always failing{RS}
{LINE2}

  Cause: Router is not Pixie Dust vulnerable
  Fix: Try Bruteforce instead
{CMD} {C}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}

{LINE2}
{R}  ✗  Router keeps locking{RS}
{LINE2}

  Fix 1 — Slow down:
{CMD} {C}python main.py -i wlan0 -b ... -B -d 3{RS}

  Fix 2 — Increase lock delay:
{CMD} {C}python main.py -i wlan0 -b ... -B --lock-delay 120{RS}

  Fix 3 — Change MAC on each attempt:
{CMD} {C}python main.py -i wlan0 -b ... -B -M{RS}

{LINE2}
{R}  ✗  pixiewps: command not found{RS}
{LINE2}

{CMD} {C}pkg install pixiewps{RS}

{LINE2}
{R}  ✗  ImportError / ModuleNotFoundError{RS}
{LINE2}

{CMD} {C}pkg install python{RS}
{CMD} {C}pip install -r requirements.txt{RS}  ← if the file exists
''')
    pause()

# ────────────────────────────────────────────
def section_warnings():
    clear()
    banner()
    print(f'''
{LINE}
{R}  8. Important Warnings & Rules{RS}
{LINE}

{R}╔══════════════════════════════════════════════╗
║   ⚠  Read carefully — this is important!    ║
╚══════════════════════════════════════════════╝{RS}

{LINE2}
{R}  What NOT to do:{RS}
{LINE2}

  {R}✗{RS} Do not attack someone else's router or network
  {R}✗{RS} Do not test any network without permission
  {R}✗{RS} Do not run this on public WiFi or unknown networks
  {R}✗{RS} Do not use this tool for illegal activity

{LINE2}
{G}  What you SHOULD do:{RS}
{LINE2}

  {G}✔{RS} Only test your own or authorized networks
  {G}✔{RS} Set up your own lab environment for learning
  {G}✔{RS} Keep your router updated and disable WPS
  {G}✔{RS} Use this tool for educational purposes only

{LINE2}
{Y}  Legal notice:{RS}
{LINE2}

  Attacking someone else's network without
  permission is {R}illegal and punishable by law{RS}
  in most countries.

  This tool is built strictly for {G}educational
  and authorized security testing{RS} purposes.

{LINE2}
{M}  Developer:{RS}
{LINE2}

  {W}MD Sakibur Rahman (MSR){RS}
  GitHub  : {C}msrofficial{RS}
  Website : {C}https://msrsakibur.netlify.app{RS}

{TIP} {M}Stay With MSR — Stay safe, stay ethical.{RS}
''')
    pause()

# ────────────────────────────────────────────
def section_wifux_commands():
    clear()
    banner()
    print(f'''
{LINE}
{Y}  9. Available wifux Commands — Quick Reference{RS}
{LINE}

{LINE2}
{G}  ─── Basic Commands ───{RS}
{LINE2}

  {G}wifux{RS}
  ↳ Run WiFuX with default settings
     (interface: wlan0, attack: Pixie Dust)

  {G}wifux menu{RS}
  ↳ Open WiFuX interactive menu without auto-attack
     (runs: sudo python main.py)

  {G}wifux old{RS}
  ↳ Run the old WiFuX engine (w1.py)
     (runs: sudo python w1.py -i wlan0 -K)

{LINE2}
{G}  ─── Tool Management ───{RS}
{LINE2}

  {G}wifux update{RS}
  ↳ Fetch & install latest updates from GitHub

  {G}wifux help{RS}
  ↳ Open this help guide

  {G}wifux fix{RS}
  ↳ Fix root / superuser issues in Termux

  {G}wifux contact{RS}
  ↳ Contact the developer (MSR)

{LINE2}
{G}  ─── With Arguments (Advanced) ───{RS}
{LINE2}

  {G}wifux -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}
  ↳ Pixie Dust on a specific router

  {G}wifux -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}
  ↳ Bruteforce on a specific router

  {G}wifux -i wlan0 -K --dts{RS}
  ↳ Pixie Dust without touching Android WiFi settings

{TIP} {M}For full argument list, see option 5 (Command List).{RS}
''')
    pause()

# ────────────────────────────────────────────
def main():
    handlers = {
        '1': section_intro,
        '2': section_install,
        '3': section_interface,
        '4': section_attacks,
        '5': section_commands,
        '6': section_examples,
        '7': section_troubleshoot,
        '8': section_warnings,
        '9': section_wifux_commands,
    }

    while True:
        choice = show_menu()
        if choice == '0':
            clear()
            print(f'\n{M}  ★ Stay With MSR — Thanks for using WiFuX!{RS}\n')
            sys.exit(0)
        elif choice in handlers:
            handlers[choice]()
        else:
            print(f'{WARN} {Y}Invalid choice! Please try again.{RS}')
            time.sleep(1)

if __name__ == '__main__':
    main()
