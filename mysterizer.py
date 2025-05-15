import json
import random
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://portswigger.net"
ALL_LABS_URL = urljoin(BASE_URL, "/web-security/all-labs")
LABS_JSON = "labs.json"

# === Step 1: Scrape Latest Labs from PortSwigger and save labs.json ===
print("📡 Fetching latest labs from PortSwigger...")
try:
    response = requests.get(ALL_LABS_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    labs_by_category = {}
    current_category = None

    for tag in soup.select("#all-labs > *"):
        if tag.name == "h2":
            current_category = tag.get_text(strip=True)
            labs_by_category[current_category] = []
        elif tag.name == "div" and "widgetcontainer-lab-link" in tag.get("class", []):
            a_tag = tag.find("a", href=True)
            if a_tag and current_category:
                full_url = urljoin(BASE_URL, a_tag["href"])
                labs_by_category[current_category].append(full_url)

    total_labs = sum(len(v) for v in labs_by_category.values())
    print(f"✅ {total_labs} labs loaded across {len(labs_by_category)} categories.\n")

    with open(LABS_JSON, "w", encoding="utf-8") as f:
        json.dump(labs_by_category, f, indent=2)

except Exception as e:
    print(f"❌ Failed to fetch or parse labs: {e}")
    exit(1)

# === Step 2: User Options ===

lab_sources = {
    "1": ("labs.json", "All labs (with expert)"),
    "2": ("allnoexpert.json", "All labs (no expert)"),
    "3": ("favourite.json", "My favourite labs"),
    "4": ("botesjuan.json", "Botesjuan labs"),
    "5": ("BURP_OFFICIAL", "Burp Official Mystery Challenge")
}

# Prompt: Do you want to select a category?
print("❓ Do you want to select a category?")
print("1. Yes")
print("2. No")
category_choice = input("Enter choice (1 or 2): ").strip()

if category_choice not in {"1", "2"}:
    print("Invalid selection.")
    exit(1)

# If user selects Yes, always use labs.json
if category_choice == "1":
    json_file = "labs.json"
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            labs_by_category = json.load(f)
    except FileNotFoundError:
        print(f"File '{json_file}' not found.")
        exit(1)

    # Show and select category
    categories = sorted(labs_by_category.keys())
    print("\n🔍 Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    try:
        selected_index = int(input("Enter number of category: ").strip())
        if 1 <= selected_index <= len(categories):
            selected_category = categories[selected_index - 1]
            selected = random.choice(labs_by_category[selected_category])
            print(f"\n🎯 Random lab from '{selected_category}':\n{selected}")
        else:
            print("Invalid category selection.")
            exit(1)
    except ValueError:
        print("Invalid input.")
        exit(1)

else:
    # Choose lab list source
    print("\n📂 Choose a lab list to randomize from:")
    for key, (_, label) in lab_sources.items():
        print(f"{key}. {label}")

    source_choice = input("Enter number of lab list (1–5): ").strip()

    if source_choice not in lab_sources:
        print("Invalid selection.")
        exit(1)

    if source_choice == "5":
        selected = "https://portswigger.net/academy/labs/launchMystery?categoryId=-1&level=1&referrer=/web-security/certification/how-to-prepare&onlyCompleted=false"
        print(f"\n🎯 Launching Burp Official Mystery Challenge:\n{selected}")
    else:
        json_file = lab_sources[source_choice][0]
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                labs_by_category = json.load(f)
        except FileNotFoundError:
            print(f"File '{json_file}' not found.")
            exit(1)

        all_labs = [url for urls in labs_by_category.values() for url in urls]
        selected = random.choice(all_labs)
        print(f"\n🎯 Random lab selected:\n{selected}")

# === Step 3: Open in Chrome with fallback ===
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

try:
    if os.path.exists(chrome_path):
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        print("🚀 Attempting to open in Chrome...")
        webbrowser.get("chrome").open(selected, new=2)
    else:
        raise FileNotFoundError("Chrome not found at expected path.")

except Exception as e:
    print(f"⚠️  Failed to open in Chrome: {e}")
    print("🌐 Falling back to system default browser...")
    try:
        webbrowser.open(selected, new=2)
        print("✅ Lab opened in default browser.")
    except Exception as e2:
        print(f"❌ Failed to open in system default browser: {e2}")