import re
import os
import sys

COLOR_BAD_SCORE = sys.argv[1]
COLOR_OK_SCORE = sys.argv[2]
COLOR_GOOD_SCORE = sys.argv[3]
COLOR_PERFECT_SCORE = sys.argv[4]

with open("pylint_score.txt", "r") as f:
    pylint_result = f.read()
numeric_score = re.search(r"(?<=\s)(\d+\.\d+)\/\d+(?=\s)", pylint_result).group().split("/")[0]

color = COLOR_BAD_SCORE
if 5 <= float(numeric_score) < 8:
    color = COLOR_OK_SCORE
elif 8 <= float(numeric_score) < 10:
    color = COLOR_GOOD_SCORE
elif float(numeric_score) == 10:
    color = COLOR_PERFECT_SCORE

os.system("echo badge_color=" + color + " >> $GITHUB_OUTPUT")
os.system("echo pylint_score=" + numeric_score + " >> $GITHUB_OUTPUT")
