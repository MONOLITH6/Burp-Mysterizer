import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random
import webbrowser
import os

# === Step 1: Scrape Latest Labs from PortSwigger ===
BASE_URL = "https://portswigger.net"
ALL_LABS_URL = urljoin(BASE_URL, "/web-security/all-labs")

print("📡 Fetching latest labs from PortSwigger...")
response = requests.get(ALL_LABS_URL)
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

# === Step 2: CLI Prompt ===
categories = sorted(labs_by_category.keys())
print("🎯 Select a category:")
for i, cat in enumerate(categories, 1):
    print(f"{i}. {cat}")
print("0. All categories")

try:
    choice = int(input("\nEnter number of category (0 for all): ").strip())
    if choice == 0:
        all_labs = [lab for labs in labs_by_category.values() for lab in labs]
        selected = random.choice(all_labs)
        print(f"\n🎲 Random lab from ALL categories:\n{selected}")
    elif 1 <= choice <= len(categories):
        selected_category = categories[choice - 1]
        selected = random.choice(labs_by_category[selected_category])
        print(f"\n🎲 Random lab from '{selected_category}':\n{selected}")
    else:
        print("❌ Invalid selection.")
        exit(1)
except ValueError:
    print("❌ Invalid input.")
    exit(1)

# === Step 3: Open in Chrome ===
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if os.path.exists(chrome_path):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open(selected, new=2)
else:
    print("⚠️ Chrome not found at expected path.")
