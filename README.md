
          # WiFuX - WiFi Hacker Tool

**WiFuX** is a Python-based tool designed for testing the security of wireless networks by exploiting vulnerabilities in the WPS (Wi-Fi Protected Setup) protocol. It includes various features such as Pixie Dust attacks, brute-force attacks, and support for multiple WPS PIN generation algorithms.

This project is intended for educational purposes and ethical use only. Always ensure you have proper authorization before using this tool on any network.

---

## 🔧 Features

- **WPS PIN Generation**: Supports multiple algorithms to generate potential WPS PINs based on MAC addresses.
- **Pixie Dust Attack**: Integration with `pixiewps` for offline brute-forcing of WPS PINs using captured EAP messages.
- **Online Brute-force Attack**: Online brute-force attack capabilities for guessing WPS PINs.
- **Network Scanner**: Built-in scanner to detect nearby WPS-enabled networks and display detailed information.
- **Session Management**: Saves progress during brute-force sessions for resuming later.
- **Credential Storage**: Stores successfully recovered credentials into text and CSV files.
- **Vulnerability Detection**: Highlights known vulnerable devices from a custom list.

---

## ⚙️ Requirements

- Python 3.6 or newer
- Linux environment (required for wireless tools)
- Root privileges (`sudo`)
- `wpa_supplicant`, `iw`, and `pixiewps` installed
- A wireless interface capable of monitor mode

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/msrofficial/WiFuX.git
   cd WiFuX
   ```

2. **Install dependencies:**

   Ensure `wpa_supplicant`, `iw`, and `pixiewps` are installed:

   ```bash
   sudo apt install wpa_supplicant iw pixiewps
   ```

3. **Run the tool:**

   ```bash
   sudo python3 main.py -i wlan0
   ```

---

## 🖥️ Usage Examples

### Scan for WPS Networks
```bash
sudo python3 main.py -i wlan0
```

### Run Pixie Dust Attack on Target AP
```bash
sudo python3 main.py -i wlan0 -b 00:90:4C:C1:AC:21 -K
```

### Online Brute-force Attack
```bash
sudo python3 main.py -i wlan0 -b 00:90:4C:C1:AC:21 -B
```

### Use Custom Vulnerable Devices List
```bash
sudo python3 main.py -i wlan0 --vuln-list vulnwsc.txt
```

---

## 🛡 Disclaimer

This tool is for educational and ethical use only. The developer assumes no responsibility for misuse or unauthorized access. Always obtain explicit permission before testing any network.

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**MD Sakibur Rahman (MSR)**  
GitHub: [@msrofficial](https://github.com/msrofficial)  
Facebook: [sakibur.msr](https://facebook.com/sakibur.msr)  
Portfolio: [https://msrsakibur.netlify.app](https://msrsakibur.netlify.app)

---

## 📬 Feedback & Contributions

Feel free to open issues or submit pull requests! Your feedback helps improve the tool.

---

## ✅ Acknowledgments

- Inspired by popular tools like Reaver and Pixiewps.
- Special thanks to the open-source community for contributions and testing.

---

Happy hacking, stay ethical! 💻🔒
