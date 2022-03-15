from PIL import Image, ImageDraw, ImageFont

img = Image.new('L', (100, 10))
drawing = ImageDraw.Draw(img)
drawing.text((1,1), "hello there",255)
img.save('pil_text.png')
