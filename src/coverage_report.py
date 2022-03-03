import re
from PIL import Image, ImageDraw, ImageFont

coverage_file_loc = "cov.xml"

with open(coverage_file_loc, "r") as file:
    file_content = file.read()


pattern = r"line-rate=\"([\d\.]+)\""
coverage_match = re.search(pattern=pattern, string=file_content)
coverage_match = float(coverage_match.group(1)) * 100


GREY = (20, 20, 20, 255)
RED = (188, 27, 27, 255)
YELLOW = (188, 198, 52, 255)
GREEN = (46, 152, 54, 255)
WHITE = (255, 255, 255, 255)

if coverage_match < 30:
    FILL_COLOR = RED
elif coverage_match < 60:
    FILL_COLOR = YELLOW
else:
    FILL_COLOR = GREEN


txt = Image.new("RGBA", (104, 20), (255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.rounded_rectangle((0, 0, 70, 20), radius=4, fill=GREY)
d.rounded_rectangle((70, 0, 104, 20), radius=4, fill=FILL_COLOR)
d.line((70, 0, 70, 20), width=5, fill=GREY)
fnt = ImageFont.truetype(font="./assets/OpenSans.ttf", size=12)
d.text((10, 2), "Coverage", fill=WHITE, font=fnt)
d.text((75, 2), f"{int(coverage_match)} %", fill=WHITE, font=fnt)
txt.save("./assets/coverage_image.png", format="PNG")
