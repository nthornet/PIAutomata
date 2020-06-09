import pygame, sys
from pygame.locals import *
import random
from ProcessImg import Process as pi
import os,sys
import image_slicer
WIDTH = 800
HEIGHT = 600
CELL = 50
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


# crea el grid para el automata
def drawGrid():
    cutimg = pi.ProcesarImagen('490149_905766.jpg',
                               WIDTH, HEIGHT, CELL)
    i = 1
    j = 1

    image_slicer.save_tiles(cutimg, directory='cut_images', prefix='slice', format='png')
    for img in cutimg:
        img.image.putalpha(0)
        outfile = 'cut_images/slice_%02d_%02d.png' % (i,j)
        imagen = pygame.image.load(outfile)
        screen.blit(imagen, img.coords)
        if j == 16:
            j = 1 
            i += 1
        else:
            j += 1


# resetea el automata
def resetLife():
    T=1

# Cambia el valor alpha de las celulas vivas
def colorize(item, life_dict):
    t=1

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
                        if life_dict[neighbour] == 1:
                            if x != 0 or y != 0:
                                neighbour_count += 1
                    except KeyError:
                        # catch key errors
                        # print "error"
                        pass
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
    return new_life


def main():
    # Initialization of the game board and cells
    
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    screen.fill(WHITE)
    #life_dict = resetLife()

    drawGrid()
    pygame.display.update()
    # for item in life_dict:
    #     colorize(item, life_dict)
    # drawGrid()
    # pygame.display.update()
    #

    while True:  # main loop that runs the game
        for event in pygame.event.get():
            if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
    #         COUNT += 1
    #         life_dict = runStep(life_dict)
    #     for item in life_dict:
    #         colorize(item, life_dict)
        drawGrid()
        pygame.display.update()
    #     CLOCK.tick(REFRESH)


if __name__ == '__main__':
    pygame.init()
    global screen
    global COUNT
    COUNT = 0
    CLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main()
