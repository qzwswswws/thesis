import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams["font.sans-serif"] = ["SimHei"]
prop = fm.FontProperties(family=["Times New Roman", "SimSun", "Noto Serif CJK SC", "sans-serif"])
prop.set_size(14)

fig, ax = plt.subplots()
ax.text(0.5, 0.5, "English Text 英文测试", fontproperties=prop)
fig.savefig("test_font.png")
