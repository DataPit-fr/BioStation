import re
from pathlib import Path

roadmap = Path("README.md").read_text(encoding="utf-8")

done = len(re.findall(r"^\s*[-*]\s+\[x\]", roadmap, re.IGNORECASE | re.MULTILINE))
total = len(re.findall(r"^\s*[-*]\s+\[[ x]\]", roadmap, re.IGNORECASE | re.MULTILINE))

percent = round((done / total) * 100) if total > 0 else 0

if percent < 25:
    color = "red"
elif percent < 50:
    color = "orange"
elif percent < 75:
    color = "yellow"
elif percent < 100:
    color = "brightgreen"
else:
    color = "success"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <rect width="150" height="20" fill="#555"/>
  <rect x="70" width="80" height="20" fill="{color}"/>
  <text x="10" y="14" fill="#fff" font-family="Verdana" font-size="11">Roadmap</text>
  <text x="80" y="14" fill="#fff" font-family="Verdana" font-size="11">{percent}%</text>
</svg>
"""

Path("roadmap.svg").write_text(svg, encoding="utf-8")
print(f"✔ Roadmap progress: {done}/{total} → {percent}%")
