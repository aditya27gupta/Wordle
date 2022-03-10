import re

from PIL import Image, ImageDraw, ImageFont
import subprocess

pytest_coverage_report = subprocess.run(["pytest", "--cov=src"], stdout=subprocess.PIPE)
report = pytest_coverage_report.stdout.decode("utf-8")
coverage = report.split("TOTAL")[-1]


pattern = r"\d+%"
coverage_match = re.search(pattern=pattern, string=coverage)
coverage_match = coverage_match.group()


GREY = (100, 100, 100, 255)
RED = (203, 67, 53, 255)
YELLOW = (212, 172, 13, 255)
GREEN = (19, 141, 117, 255)
WHITE = (255, 255, 255, 255)

coverage_value = int(coverage_match[:-1])

if coverage_value < 30:
    FILL_COLOR = RED
elif coverage_value < 60:
    FILL_COLOR = YELLOW
else:
    FILL_COLOR = GREEN

HEIGHT = 20
WIDTH_TEXT = 65
WIDTH_TOTAL = 104


txt = Image.new("RGBA", (WIDTH_TOTAL, HEIGHT), (255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.rounded_rectangle((0, 0, WIDTH_TEXT, HEIGHT), radius=4, fill=GREY)
d.rounded_rectangle((WIDTH_TEXT, 0, WIDTH_TOTAL, HEIGHT), radius=4, fill=FILL_COLOR)
d.line((WIDTH_TEXT, 0, WIDTH_TEXT, HEIGHT), width=5, fill=GREY)
fnt = ImageFont.truetype(font="./assets/OpenSans.ttf", size=12)
d.text((10, 2), "Coverage", fill=WHITE, font=fnt)
d.text((74, 2), coverage_match, fill=WHITE, font=fnt)
txt.save("./assets/coverage_image.png", format="PNG")
