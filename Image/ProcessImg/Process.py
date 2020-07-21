import image_slicer
from PIL import Image
from os import remove, makedirs
from shutil import rmtree
from copy import copy

def ProcesarImagen(filepath, directory, width, height, cellsize,color):
    # cargar imagen
    img = Image.open(filepath)

    # Cambiar tamano de la imagen
    imgresize = img.resize( (width, height) )

    # Darle un canal Aplha
    imgresize = imgresize.convert("RGB")
    
    width, height = imgresize.size
    newImg = copy(imgresize)
    pixels = newImg.load() 
    for py in range(height):
        for px in range(width):
            r, g, b = imgresize.getpixel( (px,py) )
            newr = 0
            if color == 'B':
                newr = int(r*90/255)
                newg = int(g*85/255)
                newb = int(b*222/255)
            if color == 'R':
                newr = int(r*222/255)
                newg = int(g*85/255)
                newb = int(b*90/255)
            pixels[px,py] = (newr, newg, newb)
    remove(filepath)
    newImg.save(filepath,'PNG')

    #imgresize.save(filepath, 'PNG')

    # Corta la imagen
    tiles = image_slicer.slice(filepath, \
                            number_tiles=None, \
                            col=int(width/cellsize), \
                            row=int(height/cellsize), \
                            save=False)

    image_slicer.save_tiles(tiles, directory=directory, prefix='slice', format='png')

    return tiles

if __name__ == "__main__":
    img = Image.open('../TestImg/machu.jpg').convert("RGB")
    width, height = img.size
    imgRed = copy(img)
    pixels = imgRed.load() 
    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel( (px,py) )
            newr = 0
            newg = 0
            newb = b
            pixels[px,py] = (newr, newg, newb)
    imgRed.save("azul.png")
    #makedirs('cuting/')
    #newcut = ProcesarImagen('../TestImg/test.jpg', 'cuting/', 600, 600, 100)
    #a = input("orden: ")
    #rmtree('cuting/')
