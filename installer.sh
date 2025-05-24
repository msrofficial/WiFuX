#!/data/data/com.termux/files/usr/bin/bash

echo -e "\033[1;32m[+] Updating packages…\033[0m"
pkg update -y && pkg upgrade -y

echo -e "\033[1;32m[+] Installing required packages…\033[0m"
pkg install root-repo -y
pkg install git tsu python wpa-supplicant pixiewps iw -y

echo -e "\033[1;32m[+] Cloning WiFuX repository…\033[0m"
git clone https://github.com/msrofficial/WiFuX
cd WiFuX || exit

echo -e "\033[1;32m[+] Installing Python dependencies…\033[0m"
pip install -r requirements.txt

chmod +x main.py

# Setup alias
SCRIPT_DIR="$(pwd)"
ALIAS_COMMAND="cd $SCRIPT_DIR && sudo python main.py -i wlan0 -K"

# Detect shell config
if [ -n "$ZSH_VERSION" ]; then
  SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
  SHELL_CONFIG="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
  SHELL_CONFIG="$HOME/.zshrc"
else
  SHELL_CONFIG="$HOME/.bashrc"
fi

if grep -q "alias wifux=" "$SHELL_CONFIG"; then
  echo "[✓] Alias 'wifux' already exists"
else
  echo "alias wifux='$ALIAS_COMMAND'" >> "$SHELL_CONFIG"
  echo "[+] Alias 'wifux' added"
fi

source "$SHELL_CONFIG"
echo -e "\n\033[1;32m[✓] Setup complete! Now just restart termux and type: wifux\033[0m"
