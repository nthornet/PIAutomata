import image_slicer
from PIL import Image
from os import remove, makedirs
from shutil import rmtree

def ProcesarImagen(filepath, directory, width, height, cellsize):
    # cargar imagen
    img = Image.open(filepath)

    # Cambiar tamano de la imagen
    imgresize = img.resize( (width, height) )

    # Darle un canal Aplha
    imgresize = imgresize.convert("RGBA")
    imgresize.save(filepath, 'PNG')

    # Corta la imagen
    tiles = image_slicer.slice(filepath, \
                            number_tiles=None, \
                            col=int(width/cellsize), \
                            row=int(height/cellsize), \
                            save=False)

    image_slicer.save_tiles(tiles, directory=directory, prefix='slice', format='png')

    return tiles

if __name__ == "__main__":
    makedirs('cuting/')
    newcut = ProcesarImagen('../TestImg/test.jpg', 'cuting/', 600, 600, 100)
    a = input("orden: ")
    rmtree('cuting/')
