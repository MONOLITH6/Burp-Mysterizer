import json
import random
import webbrowser
import os

# Load labs from JSON
with open("labs.json", "r", encoding="utf-8") as f:
    labs_by_category = json.load(f)

# Prepare category list
categories = sorted(labs_by_category.keys())
print("\n🔍PortSwigger Mystery Lab Picker")
print("==================================")
print("Choose a category:")

# Print numbered list of categories
for i, cat in enumerate(categories, 1):
    print(f"{i}. {cat}")
print("0. All categories")

# Get user input
try:
    choice = int(input("\nEnter number of category (0 for all): ").strip())
    if choice == 0:
        all_labs = [url for urls in labs_by_category.values() for url in urls]
        selected = random.choice(all_labs)
        print(f"\nRandom lab from ALL categories:\n{selected}")
    elif 1 <= choice <= len(categories):
        selected_category = categories[choice - 1]
        selected = random.choice(labs_by_category[selected_category])
        print(f"\nRandom lab from '{selected_category}':\n{selected}")
    else:
        print("Invalid selection.")
        exit(1)
except ValueError:
    print("Invalid input.")
    exit(1)

# Chrome setup (change path if needed)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if os.path.exists(chrome_path):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open(selected, new=2)
else:
    print("Chrome not found at expected path.")
0