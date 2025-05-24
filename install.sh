#!/data/data/com.termux/files/usr/bin/bash

SCRIPT_PATH="$(realpath $0)"
SCRIPT_DIR="$(dirname $SCRIPT_PATH)"
ALIAS_COMMAND="cd $SCRIPT_DIR && sudo python main.py -i wlan0 -K"

# Detect shell config file
if [ -n "$ZSH_VERSION" ]; then
  SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
  SHELL_CONFIG="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
  SHELL_CONFIG="$HOME/.zshrc"
else
  SHELL_CONFIG="$HOME/.bashrc"
fi

# Check if alias already exists
if grep -q "alias wifux=" "$SHELL_CONFIG"; then
  echo "[✓] Alias 'wifux' already exists in $SHELL_CONFIG"
else
  echo "alias wifux='$ALIAS_COMMAND'" >> "$SHELL_CONFIG"
  echo "[+] Alias 'wifux' added to $SHELL_CONFIG"
fi

# Reload shell config
source "$SHELL_CONFIG"
echo "[✓] Now you can use 'wifux' command in Termux!So Restart your Termux"
