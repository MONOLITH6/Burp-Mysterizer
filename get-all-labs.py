import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# Constants
BASE_URL = "https://portswigger.net"
ALL_LABS_URL = urljoin(BASE_URL, "/web-security/all-labs")

# Fetch the latest lab listing page
response = requests.get(ALL_LABS_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Initialize dictionary for labs by category
labs_by_category = {}
current_category = None

# Loop through all children inside the #all-labs div
for tag in soup.select("#all-labs > *"):
    if tag.name == "h2":
        # New category title
        current_category = tag.get_text(strip=True)
        labs_by_category[current_category] = []
    elif tag.name == "div" and "widgetcontainer-lab-link" in tag.get("class", []):
        # Get link inside this lab block
        a_tag = tag.find("a", href=True)
        if a_tag and current_category:
            full_url = urljoin(BASE_URL, a_tag["href"])
            labs_by_category[current_category].append(full_url)

# Save to JSON file for the randomizer to load later
with open("labs.json", "w", encoding="utf-8") as f:
    json.dump(labs_by_category, f, indent=2)

print(f"✅ {sum(len(v) for v in labs_by_category.values())} labs saved to labs.json")
