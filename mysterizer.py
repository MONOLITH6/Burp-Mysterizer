import json
import random
import webbrowser
import os

# Step 1: Ask user for JSON file selection
json_files = {
    "1": "favourite.json",
    "2": "labs.json",
    "3": "allnoexpert.json",
    "4": "botesjuan.json"
}

print("\n📂 Choose a lab collection to randomize from:")
for key, name in json_files.items():
    print(f"{key}. {name}")
json_choice = input("\nEnter number of lab collection (e.g. 1): ").strip()

if json_choice not in json_files:
    print("Invalid selection.")
    exit(1)

selected_json = json_files[json_choice]

# Load labs from selected JSON file
try:
    with open(selected_json, "r", encoding="utf-8") as f:
        labs_by_category = json.load(f)
except FileNotFoundError:
    print(f"File '{selected_json}' not found.")
    exit(1)

# Pick a random lab from all categories
all_labs = [url for urls in labs_by_category.values() for url in urls]
selected = random.choice(all_labs)
print(f"\n🎯 Random lab selected:\n{selected}")

# Chrome setup (adjust path if needed)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if os.path.exists(chrome_path):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open(selected, new=2)
else:
    print("Chrome not found at expected path.")
