from PIL import Image, ImageDraw

img = Image.new("RGB", (800, 500), "white")

draw = ImageDraw.Draw(img)

draw.text((220, 50), "MEGA SALE 50% OFF", fill="black")

img.save("business_poster.png")

print("Business poster created successfully!")