import matplotlib.font_manager as fm
import os

font_path = "/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"
if os.path.exists(font_path):
    fm.fontManager.addfont(font_path)
    for f in fm.fontManager.ttflist:
        if f.fname == font_path:
            print("Name for AR PL:", f.name)
            break
