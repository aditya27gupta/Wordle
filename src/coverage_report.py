import re
from PIL import Image, ImageDraw, ImageFont

coverage_file_loc = "cov.xml"

with open(coverage_file_loc, "r") as file:
    file_content = file.read()


pattern = r"line-rate=\"([\d\.]+)\""
coverage_match = re.search(pattern=pattern, string=file_content)
coverage_match = float(coverage_match.group(1)) * 100


GREY = (20, 20, 20, 255)
RED = (203, 67, 53, 255)
YELLOW = (212, 172, 13, 255)
GREEN = (19, 141, 117, 255)
WHITE = (255, 255, 255, 255)

if coverage_match < 30:
    FILL_COLOR = RED
elif coverage_match < 60:
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
d.text((71, 2), f"{int(coverage_match)} %", fill=WHITE, font=fnt)
txt.save("./assets/coverage_image.png", format="PNG")
