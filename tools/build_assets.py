# Wraps src/app.html into the full page the Android app loads.
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
body = (root / "src" / "app.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="hi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#D9480F">
<style>[hidden]{display:none!important}html,body{margin:0}img{max-width:100%}</style>
</head><body>
"""
# the <title>/<meta>/<style> block lives at the top of app.html; browsers accept them in body too, so hoist nothing.
(root / "app/src/main/assets/index.html").write_text(head + body + "\n</body></html>\n", encoding="utf-8")
print("wrote assets/index.html")
