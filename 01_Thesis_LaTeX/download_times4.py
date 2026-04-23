import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
font_dir = "tools/fonts"
os.makedirs(font_dir, exist_ok=True)

url = "https://ghproxy.net/https://raw.githubusercontent.com/Haixing-Hu/latex-zh-fonts/master/fonts/windows/times.ttf"

print(f"Downloading from {url}...")
try:
    urllib.request.urlretrieve(url, os.path.join(font_dir, "times.ttf"))
    print("Success")
except Exception as e:
    print(f"Failed: {e}")
