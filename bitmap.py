from PIL import Image, ImageDraw, ImageFont

img = Image.new('L', (100, 10))

d = ImageDraw.Draw(img)

d.text((1,1), "SCIENCE",255)
d.text((1,1), "hello there",255)

img.save('pil_text.png')
