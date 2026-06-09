from PIL import Image, ImageDraw

img = Image.new("RGB", (800, 500), "white")

draw = ImageDraw.Draw(img)

draw.text((250, 50), "HAPPY DIWALI", fill="black")
draw.rectangle((100, 150, 700, 400), outline="black", width=3)

img.save("festival_poster.png")

print("Festival poster created successfully!")