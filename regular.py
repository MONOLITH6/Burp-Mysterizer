import random
import tkinter as tk
from tkinter import ttk
import webbrowser
import os

# 1. Register Chrome browser (update path if needed)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if os.path.exists(chrome_path):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
else:
    print("⚠️ Chrome not found at the default path. Please update the chrome_path variable.")

# 2. Sample categories with sample labs (expand this to 31 total)
labs = {
    "SQL Injection": [
        "https://portswigger.net/academy/labs/launch/d9a071d8264e85184722707ff5747bbbd77963967d1d01f1b22f5dd8252f9767?referrer=%2fweb-security%2fsql-injection%2flab-retrieve-hidden-data",
        "https://portswigger.net/academy/labs/launch/befc0f5ddbc0e32a7adc4c9d4d286582f462f70bf32a8d5df15489d679dcd5c9?referrer=%2fweb-security%2fsql-injection%2flab-login-bypass",
        "https://portswigger.net/academy/labs/launch/974bd9df06352f8b59c679f854a5bc7e3db6c7fb83f72db653509252a6d47e28?referrer=%2fweb-security%2fsql-injection%2fexamining-the-database%2flab-querying-database-version-oracle",
        "https://portswigger.net/academy/labs/launch/13e48d1949abb8793e11da34ed06a5811ea3a9b2be0501a5e9f0deb255d37406?referrer=%2fweb-security%2fsql-injection%2fexamining-the-database%2flab-querying-database-version-mysql-microsoft",
        "https://portswigger.net/academy/labs/launch/81986add1fa6ec438867539cc2f562f01dcf9faf6a0b82766269c3dbeef30b00?referrer=%2fweb-security%2fsql-injection%2fexamining-the-database%2flab-listing-database-contents-non-oracle",
        "https://portswigger.net/academy/labs/launch/de4256d42cc604a2a3f7e792c5fff88df1712f1537cd506ed2537efedbd4c665?referrer=%2fweb-security%2fsql-injection%2fexamining-the-database%2flab-listing-database-contents-oracle",
        "https://portswigger.net/academy/labs/launch/c0cf223d86b3189ea471d7a4dfe43987f9306dcd549be77599964da1b517b307?referrer=%2fweb-security%2fsql-injection%2funion-attacks%2flab-determine-number-of-columns",
        "https://portswigger.net/academy/labs/launch/dc3ff4b519f1a96f0bd7507a607ced9ca7f87900eb196d0a9b25001de1833f5e?referrer=%2fweb-security%2fsql-injection%2funion-attacks%2flab-find-column-containing-text",
        "https://portswigger.net/academy/labs/launch/7c96fa50c7c53c9f9c96467a8b9e76f070dafcf9bfdcc4f04fc786ef0b0819d2?referrer=%2fweb-security%2fsql-injection%2funion-attacks%2flab-retrieve-multiple-values-in-single-column",
        "https://portswigger.net/academy/labs/launch/5aeeac77d52d55cdff3f9a5d86d050c9a77ebfef7657cccb459bee29ad5c3fce?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-conditional-responses",
        "https://portswigger.net/academy/labs/launch/9622f310ce0fc2a85821811f98f2be7b23e049667d49d018ca28f06dc0b7875a?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-conditional-errors",
        "https://portswigger.net/academy/labs/launch/706318b8f1857a10698288c9bf7712276e4ab38822541edeb0385a44da54de78?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-sql-injection-visible-error-based",
        "https://portswigger.net/academy/labs/launch/5d7c0f6ae7e03b08a47f4f6bff758a7c1b154753efea5dc4d4b847f7d1eab0a7?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-time-delays",
        "https://portswigger.net/academy/labs/launch/90b742428496fd275bba4a89c5b13e2fa4dea4be3875ec8f6b09cdcd4cb63e7d?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-time-delays-info-retrieval",
        "https://portswigger.net/academy/labs/launch/bd885d4dca761e440e1c4056234b100f514a5ba06cb79df59a7fdb02eda2af17?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-out-of-band",
        "https://portswigger.net/academy/labs/launch/365ed5e4a7dbea87f7a659dd1349317f193bd4449f6ab6ed8062e5a319f553c6?referrer=%2fweb-security%2fsql-injection%2fblind%2flab-out-of-band-data-exfiltration",
        "https://portswigger.net/academy/labs/launch/c8332afeeb7acf103db621a4d16b7249c26f7040478a07ff274d2f98687b02b6?referrer=%2fweb-security%2fsql-injection%2flab-sql-injection-with-filter-bypass-via-xml-encoding",
    ],
    "Cross-Site Scripting (XSS)": [
        "https://portswigger.net/web-security/xss/reflected",
        "https://portswigger.net/web-security/xss/stored",
    ],
    "CSRF": [
        "https://portswigger.net/web-security/csrf/lab-change-email",
    ],
    "Access Control": [
        "https://portswigger.net/web-security/access-control/lab-user-id-in-url",
    ],
    "SSRF": [
        "https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost",
    ],
    "Command Injection": [
        "https://portswigger.net/web-security/os-command-injection/lab-simple",
    ],
    # Add the rest of the 31 categories and labs here...
}

category_list = ["All Categories"] + sorted(labs.keys())

# 3. Function to open lab
def open_random_lab(selected_category):
    if selected_category == "All Categories":
        all_links = [link for sublist in labs.values() for link in sublist]
        url = random.choice(all_links)
    else:
        url = random.choice(labs[selected_category])

    print(f"Launching: {url}")
    try:
        webbrowser.get("chrome").open(url, new=2)
    except webbrowser.Error:
        print("⚠️ Failed to launch Chrome. Is the path correct?")

# 4. GUI
root = tk.Tk()
root.title("🔍 PortSwigger Mystery Lab Picker")

label = tk.Label(root, text="Select a category:")
label.pack(pady=10)

combo = ttk.Combobox(root, values=category_list, width=45)
combo.set("All Categories")
combo.pack(pady=5)

btn = tk.Button(root, text="🎲 Pick a Mystery Lab", command=lambda: open_random_lab(combo.get()))
btn.pack(pady=20)

root.mainloop()
