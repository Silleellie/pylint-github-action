import os.path
import re
import sys

README_PATH = sys.argv[1]
NUMERIC_SCORE = sys.argv[2]
BADGE_COLOR = sys.argv[3]

if not os.path.isfile(README_PATH):
    raise FileNotFoundError(f"README.md path is wrong, no file can be located at {README_PATH}")

with open(README_PATH, "r", encoding="utf8") as f:
    content = f.read()

query = f"pylint-{NUMERIC_SCORE}-{BADGE_COLOR}?logo=python&logoColor=white"
badge_url = f"https://img.shields.io/badge/{query}"

result = re.sub(r"(?<=!\[pylint]\()(.*?)(?=\))", badge_url, content)
with open(README_PATH, "w", encoding="utf8") as f:
    f.write(result)
