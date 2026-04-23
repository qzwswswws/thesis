import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
font_dir = "tools/fonts"
os.makedirs(font_dir, exist_ok=True)

cdn_times = "https://raw.githubusercontent.com/justinmchase/times-new-roman/master/times.ttf"
cdn_simsun = "https://raw.githubusercontent.com/StellarCN/scp_zh/master/fonts/SimSun.ttf"

def download_font(url, filename):
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, os.path.join(font_dir, filename))
        print("Success")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

download_font(cdn_times.replace("raw.githubusercontent.com", "ghproxy.net/https://raw.githubusercontent.com"), "times.ttf")
download_font(cdn_simsun.replace("raw.githubusercontent.com", "ghproxy.net/https://raw.githubusercontent.com"), "simsun.ttf")
