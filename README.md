# 📶 WiFuX - WiFi Hacker Tool

### 🔥 Hack WiFi Using Termux (Requires Root)  
A powerful **WiFi hacking tool** designed for ethical use to test the security of wireless networks using **WPS vulnerabilities**, including **Pixie Dust Attack**, **Brute-force Attack**, and more.

---

## 🛠 Installation

```bash
pkg update && pkg upgrade -y
```

```bash
pkg install root-repo -y
```

```bash
pkg install git tsu python wpa-supplicant pixiewps iw -y
```

```bash
git clone https://github.com/msrofficial/WiFuX
```

```bash
cd WiFuX
```

```bash
pip3 install -r requirements.txt
```

```bash
chmod +x main.py
```

---

## 💻 Usage

### Show Help
```bash
sudo python main.py --help
```

### Scan & Start Pixie Dust Attack
```bash
sudo python main.py -i wlan0 -K
```

### Start Pixie Dust Attack on Specific BSSID
```bash
sudo python main.py -i wlan0 -b 00:91:4C:C3:AC:28 -K
```

### Launch Online WPS Brute-force Attack with PIN
```bash
sudo python main.py -i wlan0 -b 00:90:4C:C1:AC:21 -B -p 1234
```

---

## ⚠️ Notes

- **First turn off your WiFi.**
- **Turn on Hotspot.**
- If you get `"Device or resource busy (-16)"`, **turn on WiFi and then turn it off again**.
- **If failed, turn off Location services if turned on.**

---

## 📌 Disclaimer

This tool is for educational and ethical purposes only. Do not use without proper authorization. The author is not responsible for any misuse or damage caused by this tool.

---

## 📄 License

```
MIT License

Copyright (c) 2023 MSR🇧🇩

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📱 WiFi Hacking with Android

WiFuX is fully compatible with **Android devices running Termux**. You can perform advanced WiFi penetration testing directly from your phone with root access and a supported wireless interface (e.g., Alfa adapter via OTG).

Make sure:
- Your device supports monitor mode.
- You're using a rooted Android environment.
- WiFi is turned off before running the script.

---

## 🧑‍💻 Author

**MD Sakibur Rahman (MSR)**  
GitHub: [@msrofficial](https://github.com/msrofficial)  
Facebook: [sakibur.msr](https://facebook.com/sakibur.msr)  
Portfolio: [https://msrsakibur.netlify.app](https://msrsakibur.netlify.app)

---

## ❤️ Connect with Me

<div align="center">
<h3>━━━━ Connect with me ━━━━</h3>
<a href="https://fb.com/sakibur.msr" target="_blank">
  <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
</a>
<a href="https://github.com/sadman-11">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=sadman-11.wifi-hack" alt="Visitor Count" />
</a>
</div>

---

## 📦 Repository

[GitHub Repo](https://github.com/msrofficial/WiFuX)

---

Happy hacking, stay ethical! 💻🔒
