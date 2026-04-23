import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
font_dir = "tools/fonts"
os.makedirs(font_dir, exist_ok=True)

urls = [
    "https://raw.gitmirror.com/dolbydu/font/master/times.ttf",
    "https://gitee.com/yaoyue123/fonts/raw/master/times.ttf",
    "https://ghproxy.net/https://raw.githubusercontent.com/dolbydu/font/master/times.ttf"
]

for url in urls:
    print(f"Downloading from {url}...")
    try:
        urllib.request.urlretrieve(url, os.path.join(font_dir, "times.ttf"))
        if os.path.getsize(os.path.join(font_dir, "times.ttf")) > 100000:
            print("Success")
            break
    except Exception as e:
        print(f"Failed: {e}")
