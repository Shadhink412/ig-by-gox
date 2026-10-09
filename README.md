<h1 align="center">✦ IG-BY-GOX ✦</h1>
<p align="center">
  <b>High-Speed Multi-Provider Instagram Engine for Android / Termux</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Android-green?style=for-the-badge&logo=android" alt="Platform" />
  <img src="https://img.shields.io/badge/Architecture-ARM64%20%7C%20ARMv7%20%7C%20x86_64-blue?style=for-the-badge" alt="Architecture" />
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License" />
</p>

---

## 🚀 Overview

**IG-BY-GOX** is an automated, ultra-fast engine designed specifically for Android mobile terminals (**Termux**). It features multi-provider temporary inboxes, automatic 2FA secret generation, direct-login session cookie extraction, and saves accounts directly into your phone's main internal storage.

### 🌟 Key Highlights

- ⚡ **Ultra-Fast Engine**: High efficiency with Human or Turbo execution modes.
- 📬 **6 Multi-Mail Providers**: Automatic failover inbox rotation (NukeMail, Driftz, Smails, Neighbours, GrabMail, DevMail).
- 🔐 **2FA Pre-Configured**: Instant TOTP secret keys and verified setup.
- 🍪 **Direct Login Cookies**: Full cookie sets exported for instant browser login.
- 📱 **Mobile Screen Optimized**: Compact 38-column terminal UI tailored for portrait Termux.
- 💾 **Main Storage Auto-Save**: Saves accounts directly to `/0/Instagram-Hitter/IG_2FA.csv`.

---

## 🛠️ Step-by-Step Installation Guide (Termux)

> [!IMPORTANT]
> **Follow each step one by one in order.** Do not skip any steps.
> In Termux on Android, libraries like `cryptography` and `pynacl` require native system packages rather than default `pip` compilations. Following these verified steps ensures smooth installation on **all Android versions and CPU architectures** (ARM64, ARMv7, x86_64).

---

### 1️⃣ Update Package Lists
Updates the Termux repository package index:
```bash
pkg update -y
```

---

### 2️⃣ Upgrade Installed Packages
Upgrades all existing packages to their latest versions:
```bash
pkg upgrade -y
```
*(If prompted with `[default=N]`, press **Enter** to continue).*

---

### 3️⃣ Grant Storage Permission
Allows Termux to save created accounts to your phone's internal storage (`/0/Instagram-Hitter`):
```bash
termux-setup-storage
```
> [!IMPORTANT]
> A popup will appear on your phone screen: Tap **Allow** (বা পারমিশন দিন).

---

### 4️⃣ Install Compilers, Python, Git & Native Libraries
Installs Python, Git, C/C++ compilers, and essential crypto dependencies (`libsodium`, `openssl`, `libffi`):
```bash
pkg install clang make pkg-config python git libffi openssl libsodium -y
```

---

### 5️⃣ Install Pre-Compiled Cryptography
Installs Termux's official pre-built `cryptography` package (avoids failing Rust compiler builds):
```bash
pkg install python-cryptography -y
```

---

### 6️⃣ Install PyNaCl with System Libsodium
Compiles and links PyNaCl natively with Termux's system `libsodium` in seconds:
```bash
SODIUM_INSTALL=system pip install --no-cache-dir pynacl
```

---

### 7️⃣ Clone the Repository
Downloads the latest project code from GitHub:
```bash
git clone https://github.com/Shadhink412/ig-by-gox
```

---

### 8️⃣ Enter Project Directory
```bash
cd ig-by-gox
```

---

### 9️⃣ Install Python Dependencies
Installs remaining pure-Python packages (`requests`, `faker`, `pyotp`):
```bash
pip install -r requirements.txt
```

---

### 🔟 Launch the Engine
```bash
python hitter.py
```

---

## ⚡ Quick Re-run & Updating

Once setup is complete, you only need to use these short commands:

### 🔄 How to Run Later:
Whenever you open Termux again:
```bash
cd ig-by-gox && python hitter.py
```

### 📥 How to Update to the Latest Version:
To pull updates and bug fixes:
```bash
cd ig-by-gox && git pull
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

## 🔧 Troubleshooting & Common Issues

<details>
<summary><b>1. Package 'python-cryptography' not found?</b></summary>

If your Termux repository doesn't list `python-cryptography`, install the Termux User Repository (TUR) first:
```bash
pkg install tur-repo -y && pkg install python-cryptography -y
```
</details>

<details>
<summary><b>2. Repository connection or download fails during `pkg update`?</b></summary>

Switch to an active global mirror:
```bash
termux-change-repo
```
Select **Main repository** and choose **Grimler** or **Albatross**, then re-run `pkg update -y`.
</details>

<details>
<summary><b>3. Permission Denied when saving accounts?</b></summary>

Ensure Termux has full storage permissions:
1. Re-run: `termux-setup-storage`
2. Or go to your phone: **Settings > Apps > Termux > Permissions > Storage / Files > Allow**.
</details>

<details>
<summary><b>4. Missing Dependency notice when running `python hitter.py`?</b></summary>

If `hitter.py` outputs a missing dependency notice, simply run the specific fix command displayed on your screen, for example:
- For `pynacl`: `SODIUM_INSTALL=system pip install --no-cache-dir pynacl`
- For `cryptography`: `pkg install python-cryptography -y`
- For other packages: `pip install -r requirements.txt`
</details>

---

<p align="center">
  <b>Repository:</b> <a href="https://github.com/Shadhink412/ig-by-gox">https://github.com/Shadhink412/ig-by-gox</a>
</p>
