<h1 align="center">✦ IG-BY-GOX ✦</h1>
<p align="center">
  <b>High-Speed Multi-Provider Instagram Engine for Android / Termux</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Android-green?style=for-the-badge&logo=android" alt="Platform" />
  <img src="https://img.shields.io/badge/Language-Python%203.8+-blue?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License" />
</p>

---

## 🚀 Overview

**IG-BY-GOX** is an automated, ultra-fast engine designed specifically for Android mobile terminals (**Termux**). It features multi-provider temporary inboxes, automatic 2FA secret generation, direct-login session cookie extraction, and saves accounts directly into your phone's main storage.

### 🌟 Key Highlights

- ⚡ **Ultra-Fast Engine**: High efficiency with Human or Turbo execution modes.
- 📬 **6 Multi-Mail Providers**: Automatic failover inbox rotation.
- 🔐 **2FA Pre-Configured**: Instant TOTP secret keys and verified setup.
- 🍪 **Direct Login Cookies**: Full cookie sets exported for instant browser login.
- 📱 **Mobile Screen Optimized**: Compact 38-column terminal UI tailored for portrait Termux.
- 💾 **Main Storage Auto-Save**: Saves accounts directly to `/0/Instagram-Hitter/IG_2FA.csv`.

---

## ⚡ Quick Start (One-Line Command)

Run this single command in **Termux** to update, install all requirements, clone the repo, and start immediately:

```bash
pkg update -y && pkg upgrade -y && pkg install python git -y && termux-setup-storage && git clone https://github.com/Shadhink412/ig-by-gox && cd ig-by-gox && pip install -r requirements.txt && python hitter.py
```

---

## 🛠️ Step-by-Step Installation Guide

Follow these steps one by one in your **Termux** terminal:

### 1️⃣ Update & Upgrade Termux Packages
```bash
pkg update -y && pkg upgrade -y
```

### 2️⃣ Grant Storage Access
> [!IMPORTANT]
> When you run this command, tap **Allow** on your phone screen to give Termux access to your phone's internal storage.
```bash
termux-setup-storage
```

### 3️⃣ Install Python & Git
```bash
pkg install python git -y
```

### 4️⃣ Clone the Repository
```bash
git clone https://github.com/Shadhink412/ig-by-gox
```

### 5️⃣ Go to Directory
```bash
cd ig-by-gox
```

### 6️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 7️⃣ Run the Engine
```bash
python hitter.py
```

---

## 📂 Output & Saved Accounts Location

All created accounts are automatically saved to your phone's main internal memory:

- **Storage Path**: `/storage/emulated/0/Instagram-Hitter/IG_2FA.csv`
- **File Manager Path**: `Internal Storage > Instagram-Hitter > IG_2FA.csv`

### 📄 CSV Data Structure

| Column | Description |
| :--- | :--- |
| **`igusername`** | Registered Instagram username |
| **`password`** | Account password |
| **`2fa key`** | 16-character TOTP secret key |
| **`email`** | Verified temporary email address |
| **`time taken`** | Creation duration in seconds |
| **`cookies`** | Full direct-login session cookies (`csrftoken`, `sessionid`, `mid`, etc.) |

---

## ⚠️ Notes & Tips

1. **Storage Access**: Make sure Termux has storage permission so that the `/0/Instagram-Hitter` folder can be created without permission errors.
2. **Re-running**: To run the bot again in the future, simply enter:
   ```bash
   cd ig-by-gox && python hitter.py
   ```
3. **Updating**: To pull the latest updates anytime:
   ```bash
   cd ig-by-gox && git pull
   ```

---

<p align="center">
  <b>Repository:</b> <a href="https://github.com/Shadhink412/ig-by-gox">https://github.com/Shadhink412/ig-by-gox</a>
</p>
