import matplotlib.font_manager as fm

for f in fm.fontManager.ttflist:
    if "Times" in f.name or "Nimbus Roman" in f.name or "DejaVu Serif" in f.name:
        print(f.name)
