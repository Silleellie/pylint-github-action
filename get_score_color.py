import re
import os

with open("pylint_score.txt", "r") as f:
    pylint_result = f.read()
numeric_score = re.search(r"(?<=\s)(\d+\.\d+)\/\d+(?=\s)", pylint_result).group().split("/")[0]

color = "red"
if 5 < float(numeric_score) < 8:
    color = "orange"
elif 8 < float(numeric_score) < 10:
    color = "yellow"
elif float(numeric_score) == 10:
    color = "brightgreen"

os.system("echo badge_color=" + color + " >> $GITHUB_OUTPUT")
os.system("echo pylint_score=" + numeric_score + " >> $GITHUB_OUTPUT")
