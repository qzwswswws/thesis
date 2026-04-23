import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
font_dir = "tools/fonts"
os.makedirs(font_dir, exist_ok=True)

url = "https://ghproxy.net/https://raw.githubusercontent.com/microsoft/fonts/master/Times.ttf"
url2 = "https://ghproxy.net/https://raw.githubusercontent.com/Haixing-Hu/latex-zh-fonts/master/fonts/windows/times/times.ttf"

try:
    urllib.request.urlretrieve("https://ghproxy.net/https://raw.githubusercontent.com/whtiehack/win10_fonts/master/times.ttf", os.path.join(font_dir, "times.ttf"))
    print("Success win10_fonts")
except Exception as e:
    print(f"Failed: {e}")
