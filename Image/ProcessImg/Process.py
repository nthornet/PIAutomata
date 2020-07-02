import image_slicer
from PIL import ImageDraw, ImageFont, Image
import copy


def ProcesarImagen(filepath,width, height,cellsize):
    # cargar imagen
    img = Image.open(filepath)

    # Cambiar tamano de la imagen
    imgresize = changeImageSize(width, height, img)

    # Darle un canal Aplha
    imgresize = imgresize.convert("RGBA")
    imgresize.save(filepath, 'PNG')

    # Corta la imagen
    tiles = image_slicer.slice(filepath, number_tiles=None, col=int(width/cellsize), row=int(height/cellsize), save=False)

    # Mostrar los corte *Solo para debugeo*
    #for tile in tiles:
    #    tile.image.show()    

    return tiles


def changeImageSize(maxWidth,
                    maxHeight,
                    image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]

    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])

    newImage = image.resize((newWidth, newHeight))
    return newImage


if __name__ == "__main__":
    newcut = ProcesarImagen('../Pygameoflife/490149_905766.jpg',800, 600,100)
    viejo = copy.deepcopy(newcut)
    tempimg = newcut[1]
    tempimg.image.putalpha(255)
    tempimg.image.show()
    viejo[39].image.show()
