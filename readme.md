## 🔀 PortSwigger Mystery Lab Randomizer

This Python script fetches the **latest labs from PortSwigger Web Security Academy** and lets you **randomly select a challenge** to sharpen your offensive security skills.

### ✨ Features

* 📡 **Auto-updates** with the newest labs directly from [PortSwigger's All Labs](https://portswigger.net/web-security/all-labs)
* 🎯 **Category-based randomization** (optional)
* 🧩 Choose from multiple lab sets:

  * All labs (with or without expert-level)
  * Personal favorites (`favourite.json`)
  * Custom `botesjuan.json` list inspired by [botesjuan](https://github.com/botesjuan/Burp-Suite-Certified-Practitioner-Exam-Study/commits?author=botesjuan)
  * Official **Burp Mystery Challenge**
* 🌐 **Browser selection** with remembered preferences
* 🔁 **Fallback to system default** if the preferred browser fails

### 🛠 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

### 📁 JSON Lab Lists

You can customize the script by editing or adding these JSON files:

* `labs.json`: All categories and labs auto-fetched from PortSwigger
* `favourite.json`, `allnoexpert.json`, `botesjuan.json`: Customizable lists of handpicked labs

### 🚀 Getting Started

Run the script and follow the interactive prompts to:

1. Choose a lab source
2. (Optional) Select a category
3. Launch the lab in your browser of choice

---

Let me know if you want a matching `README.md` or a badge-friendly header for your GitHub page.
