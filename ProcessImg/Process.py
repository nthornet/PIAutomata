import image_slicer
from PIL import ImageDraw, ImageFont, Image

im = Image.open('490149_905766.jpg')


tiles = image_slicer.slice('490149_905766.jpg', 4, save=False)
for tile in tiles:
    overlay = ImageDraw.Draw(tile.image)
    overlay.text((5, 5), str(tile.number), (255, 255, 255), ImageFont.load_default())
    overlay.show()

im.show()