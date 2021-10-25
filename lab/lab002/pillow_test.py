from PIL import Image, ImageDraw

image = Image.new('RGB', (800, 600), (255, 0, 255))
image.putpixel((500, 500), (0, 0, 255))

draw = ImageDraw.Draw(image)
draw.rectangle((20, 20, 300, 300), (0, 255, 0))

image.save('test_image.png')