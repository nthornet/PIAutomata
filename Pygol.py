import pygame, sys
from pygame.locals import *
import random
from ProcessImg import Process as pi
import os, sys
import image_slicer
from Pygameoflife import entities
from PIL import Image
import cv2

WIDTH = 800
HEIGHT = 600
CELL = 10
REFRESH = 40

assert WIDTH % CELL == 0, "Window width must be a multiple of cell size"
assert HEIGHT % CELL == 0, "Window height must be a multiple of cell size"

CELL_WIDTH = int(WIDTH / CELL)
CELL_HEIGHT = int(HEIGHT / CELL)

#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREY = (40, 40, 40)

# global

global diccionario_cords
diccionario_cords = {}

# crea el grid para el automata
def drawGrid():
    cutimg = pi.ProcesarImagen('490149_905766.jpg',
                               WIDTH, HEIGHT, CELL)
    i = 1
    j = 1
    image_slicer.save_tiles(cutimg, directory='cut_images', prefix='slice', format='png')

    # imagen_transparente = imagen_transparente.save('cut_images/transparente.png')
    for img in cutimg:
        outfile = 'cut_images/slice_%02d_%02d.png' % (img.position[1], img.position[0])
        diccionario_cords[outfile] = img.coords
        try:
            imagen = pygame.image.load(outfile).convert()
        except:
            t = 1
        imagen.set_alpha(0)
        #  surface.blit(image, (0, 0))
        #  imagen = pygame.image.load(outfile)
        screen.blit(imagen, img.coords)


# resetea el automata
def resetLife():
    life_dict = {}
    for y in range(0, int(CELL_HEIGHT / CELL)):
        for x in range(0, int(CELL_WIDTH / CELL)):
            life_dict[x, y] = 0
    return life_dict


# Cambia el valor alpha de las celulas vivas
def colorize(item, life_dict):
    x = item[0]
    y = item[1]
    outfile = 'cut_images/slice_%02d_%02d.png' % (x + 1, y + 1)
    imagen = pygame.image.load(outfile).convert()
    coordinates = diccionario_cords[outfile]
    coordinates = (coordinates[1], coordinates[0])
    if life_dict[item] == 0:
        imagen.set_alpha(0)
    elif life_dict[item] == 1:
        imagen.set_alpha(255)
    screen.blit(imagen, coordinates)
    # else:
    #    imagen.set_alpha(0)
    #    screen.blit(imagen, diccionario_cords[outfile])
    return None


# inicializa el automata con una linea recta
def StraightLine(life_dict, size):
    while size > 0:
        midx = CELL_HEIGHT / 2
        midy = CELL_WIDTH / 2
        life_dict[midx + size, midy] = 1
        size = size - 1
    return life_dict


# cuenta el numero de vecinos
def getNeighbours(item, life_dict):
    neighbour_count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            neighbour = (item[0] + x, item[1] + y)
            if neighbour[0] < WIDTH and neighbour[0] >= 0:
                if neighbour[1] < HEIGHT and neighbour[1] >= 0:
                    try:
                        if life_dict[neighbour] == 1 and (x, y) != (0, 0):
                            neighbour_count += 1
                    except KeyError:
                        t = 1
                        # catch key errors
                        # print "error"
    return neighbour_count


# calcula el proximo paso
def runStep(life_dict):
    new_life = {}
    for item in life_dict:
        neighbour_count = getNeighbours(item, life_dict)
        if life_dict[item] == 1:  # cell is alive and we need to check if it will stay alive
            if neighbour_count < 2:
                # dies due to underpopulation
                new_life[item] = 0
            elif neighbour_count > 3:
                # dies due to overcrowding
                new_life[item] = 0
            else:
                # cell stays alive
                new_life[item] = 1
        elif life_dict[item] == 0:
            if neighbour_count == 3:
                new_life[item] = 1
            else:
                new_life[item] = 0
    #   print('Run Step')
    return new_life


def Loafer(life_dict):
    midx = CELL_HEIGHT / 2
    midy = CELL_WIDTH / 2
    life_dict[midx - 3, midy - 5] = 1
    life_dict[midx - 2, midy - 5] = 1
    life_dict[midx + 1, midy - 5] = 1
    life_dict[midx + 3, midy - 5] = 1
    life_dict[midx + 4, midy - 5] = 1

    life_dict[midx - 4, midy - 4] = 1
    life_dict[midx - 1, midy - 4] = 1
    life_dict[midx + 2, midy - 4] = 1
    life_dict[midx + 3, midy - 4] = 1

    life_dict[midx - 3, midy - 3] = 1
    life_dict[midx - 1, midy - 3] = 1

    life_dict[midx - 2, midy - 2] = 1

    life_dict[midx + 4, midy - 1] = 1

    life_dict[midx + 2, midy] = 1
    life_dict[midx + 3, midy] = 1
    life_dict[midx + 4, midy] = 1

    life_dict[midx + 1, midy + 1] = 1

    life_dict[midx + 2, midy + 2] = 1

    life_dict[midx + 3, midy + 3] = 1
    life_dict[midx + 4, midy + 3] = 1

    return life_dict




def main():
    # Initialization of the game board and cells
    pygame.init()
    global screen
    global COUNT

    life_dict = resetLife()
    COUNT = 0
    CLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    screen.fill(WHITE)
    life_dict = resetLife()
    life_dict = Loafer(life_dict)
    # life_dict = StraightLine(life_dict,10)
    drawGrid()
    for item in life_dict:
        colorize(item, life_dict)
    # drawGrid()
    pygame.display.update()
    #
    while True:  # main loop that runs the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        life_dict = runStep(life_dict)
        COUNT += 1
        screen.fill(WHITE)
        for item in life_dict:
            colorize(item, life_dict)
        # drawGrid()
        pygame.display.update()
        CLOCK.tick(REFRESH)


if __name__ == '__main__':
    main()
