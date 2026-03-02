#!/data/data/com.termux/files/usr/bin/bash

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[0m"

echo -e "${GREEN}[+] Setting up local WiFuX environment...${RESET}"

echo -e "${GREEN}[+] Installing Python dependencies...${RESET}"
pip install -r requirements.txt --break-system-packages

chmod +x main.py

echo -e "${GREEN}[+] Setting up 'wifux' command...${RESET}"

BIN_DIR="$PREFIX/bin"
WIFUX_BIN="$BIN_DIR/wifux"
SCRIPT_DIR="$(pwd)"

cat > "$WIFUX_BIN" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$SCRIPT_DIR" || exit

# Update Logic
if [ "\$1" == "update" ]; then
    echo -e "\033[1;32m[+] Fetching latest updates from MSR's GitHub...\033[0m"
    git reset --hard HEAD > /dev/null 2>&1
    git pull origin main
    
    echo -e "\033[1;32m[+] Checking for new requirements...\033[0m"
    pip install -r requirements.txt --break-system-packages > /dev/null 2>&1
    
    chmod +x main.py
    echo -e "\033[1;32m[✓] WiFuX updated successfully!\033[0m"
    exit 0
fi

# Run Logic
if [ -z "\$1" ]; then
    sudo python main.py -i wlan0 -K
else
    sudo python main.py "\$@"
fi
EOF

chmod +x "$WIFUX_BIN"

echo -e "\n${GREEN}[✓] Local setup complete!${RESET}"
echo -e "${YELLOW}[✓] Type 'wifux' from anywhere to run the tool.${RESET}"