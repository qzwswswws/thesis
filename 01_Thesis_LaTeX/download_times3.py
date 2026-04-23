import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
font_dir = "tools/fonts"

url = "https://github.com/Haixing-Hu/latex-zh-fonts/raw/master/fonts/windows/times.ttf"

print(f"Downloading from {url}...")
try:
    urllib.request.urlretrieve(url.replace("github.com", "mirror.ghproxy.com/https://github.com"), os.path.join(font_dir, "times.ttf"))
    print("Success")
except Exception as e:
    print(f"Failed: {e}")
