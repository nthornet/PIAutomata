import pygame, sys
from pygame.locals import *
import random

WIDTH=800
HEIGHT=600
CELL=10
REFRESH=40

assert WIDTH % CELL == 0, "Window width must be a multiple of cell size"
assert HEIGHT % CELL == 0, "Window height must be a multiple of cell size"

CELL_WIDTH=int(WIDTH/CELL)
CELL_HEIGHT=int(HEIGHT/CELL)

#
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (0,255,0)
DARKGREY = (40, 40, 40)

#Draw grid on game board
def drawGrid():
    for x in range(0,WIDTH,CELL):
        pygame.draw.line(SURFACE, DARKGREY, (x,0), (x,HEIGHT))
    for y in range(0,HEIGHT,CELL):
        pygame.draw.line(SURFACE, DARKGREY, (0,y), (WIDTH,y))

#resets board to empty
def resetLife():
    life_dict= {}
    for y in range(0,CELL_HEIGHT):
        for x in range(0,CELL_WIDTH):
            life_dict[x,y]=0
    return life_dict

def StraightLine(life_dict,size):
    while size>0:
        midx=CELL_HEIGHT/2
        midy=CELL_WIDTH/2
        life_dict[midx+size,midy] = 1
        size=size-1
    return life_dict

def RPentomino(life_dict):
    life_dict[48,32] = 1
    life_dict[49,32] = 1
    life_dict[47,33] = 1
    life_dict[48,33] = 1
    life_dict[48,34] = 1
    return life_dict

def Loafer(life_dict):
    midx=CELL_HEIGHT/2
    midy=CELL_WIDTH/2
    life_dict[midx-3,midy-5] = 1
    life_dict[midx-2,midy-5] = 1
    life_dict[midx+1,midy-5] = 1
    life_dict[midx+3,midy-5] = 1
    life_dict[midx+4,midy-5] = 1

    life_dict[midx-4,midy-4] = 1
    life_dict[midx-1,midy-4] = 1
    life_dict[midx+2,midy-4] = 1
    life_dict[midx+3,midy-4] = 1

    life_dict[midx-3,midy-3] = 1
    life_dict[midx-1,midy-3] = 1

    life_dict[midx-2,midy-2] = 1

    life_dict[midx+4,midy-1] = 1

    life_dict[midx+2,midy] = 1
    life_dict[midx+3,midy] = 1
    life_dict[midx+4,midy] = 1

    life_dict[midx+1,midy+1] = 1

    life_dict[midx+2,midy+2] = 1

    life_dict[midx+3,midy+3] = 1
    life_dict[midx+4,midy+3] = 1

    return life_dict

def GosperGlider(life_dict):
    qrtx=CELL_HEIGHT/4
    qrty=CELL_WIDTH/4

    #left square
    life_dict[qrtx+1,qrty] = 1
    life_dict[qrtx+1,qrty+1] = 1
    life_dict[qrtx+2,qrty] = 1
    life_dict[qrtx+2,qrty+1] = 1

    #left spaceship
    life_dict[qrtx+11,qrty] = 1
    life_dict[qrtx+11,qrty+1] = 1
    life_dict[qrtx+11,qrty+2] = 1

    life_dict[qrtx+12,qrty-1] = 1
    life_dict[qrtx+12,qrty+3] = 1

    life_dict[qrtx+13,qrty-2] = 1
    life_dict[qrtx+13,qrty+4] = 1

    life_dict[qrtx+14,qrty-2] = 1
    life_dict[qrtx+14,qrty+4] = 1

    life_dict[qrtx+15,qrty+1] = 1

    #Glider
    life_dict[qrtx+16,qrty-1] = 1
    life_dict[qrtx+16,qrty+3] = 1

    life_dict[qrtx+17,qrty] = 1
    life_dict[qrtx+17,qrty+1] = 1
    life_dict[qrtx+17,qrty+2] = 1

    life_dict[qrtx+18,qrty+1] = 1


    #Right Spaceship
    life_dict[qrtx+21,qrty] = 1
    life_dict[qrtx+21,qrty-1] = 1
    life_dict[qrtx+21,qrty-2] = 1

    life_dict[qrtx+22,qrty] = 1
    life_dict[qrtx+22,qrty-1] = 1
    life_dict[qrtx+22,qrty-2] = 1

    life_dict[qrtx+23,qrty-3] = 1
    life_dict[qrtx+23,qrty+1] = 1

    life_dict[qrtx+25,qrty+1] = 1
    life_dict[qrtx+25,qrty+2] = 1

    life_dict[qrtx+25,qrty-3] = 1
    life_dict[qrtx+25,qrty-4] = 1

    life_dict[qrtx+35,qrty-1] = 1
    life_dict[qrtx+35,qrty-2] = 1

    life_dict[qrtx+36,qrty-1] = 1
    life_dict[qrtx+36,qrty-2] = 1

    return life_dict

def DrawSquare(life_dict):
    qrtx=CELL_HEIGHT/4
    qrty=CELL_WIDTH/4

    life_dict[qrtx+1,qrty] = 1
    life_dict[qrtx+1,qrty+1] = 1
    life_dict[qrtx+2,qrty] = 1
    life_dict[qrtx+2,qrty+1] = 1

    return life_dict

def DrawLoaf(life_dict):
    midx=CELL_HEIGHT/2
    midy=CELL_WIDTH/2

    life_dict[midx-1,midy] = 1
    life_dict[midx,midy-1] = 1
    life_dict[midx+1,midy-1] = 1
    life_dict[midx+2,midy] = 1
    life_dict[midx,midy+1] = 1
    life_dict[midx+1,midy+1] = 1

    return life_dict

def DrawToad(life_dict):
    qrtx=CELL_HEIGHT/4
    qrty=CELL_WIDTH/4

    life_dict[qrtx+1,qrty] = 1
    life_dict[qrtx+2,qrty] = 1
    life_dict[qrtx+3,qrty] = 1
    life_dict[qrtx+2,qrty+1] = 1
    life_dict[qrtx+3,qrty+1] = 1
    life_dict[qrtx+4,qrty+1] = 1

    return life_dict

def DrawGlider(life_dict):
    midx=CELL_HEIGHT/2
    midy=CELL_WIDTH/2

    life_dict[midx+1,midy] = 1
    life_dict[midx+2,midy] = 1
    life_dict[midx+3,midy] = 1
    life_dict[midx+3,midy+1] = 1
    life_dict[midx+2,midy+2] = 1

    return life_dict

def DrawGLider2(life_dict,center):
    midx = center[0]
    midy = center[1]

def DrawEater(life_dict,center):
    midx = center[0]
    midy = center[1]

    life_dict[midx-1,midy-1] = 1
    life_dict[midx-1,midy-2] = 1
    life_dict[midx,midy-2] = 1
    # life_dict[midx,midy+1] = 1
    life_dict[midx+1,midy-1] = 1
    life_dict[midx+1,midy] = 1
    life_dict[midx+1,midy+1] = 1
    life_dict[midx+2,midy+1] = 1

    return life_dict

def initializeLife(life_dict):
    for cell in life_dict:
        life_dict[cell]=random.randint(0,1)
    return life_dict

#Colors cells if they are alive
def colorize(item, life_dict):
    x = item[0]
    y = item[1]
    y = y * CELL
    x = x * CELL
    if life_dict[item] == 0:
        pygame.draw.rect(SURFACE, WHITE, (x ,y, CELL, CELL))
    if life_dict[item] == 1:
        pygame.draw.rect(SURFACE, GREEN, (x ,y, CELL, CELL))
    return None

#finds neighbours of a specific cell
def getNeighbours(item,life_dict):

    neighbour_count=0

    for x in range(-1,2):
        for y in range(-1,2):
            neighbour=(item[0]+x,item[1]+y)
            if neighbour[0]<WIDTH and neighbour[0]>=0:
                if neighbour[1]<HEIGHT and neighbour[1]>=0:
                    try:
                        if life_dict[neighbour]==1:
                            if x!=0 or y!=0:
                                neighbour_count+=1
                    except KeyError:
                        #catch key errors
                        #print "error"
                        pass
    return neighbour_count

def runStep(life_dict):
    new_life={}
    for item in life_dict:
        neighbour_count = getNeighbours(item,life_dict)
        if life_dict[item]==1: #cell is alive and we need to check if it will stay alive
            if neighbour_count<2:
                #dies due to underpopulation
                new_life[item]=0
            elif neighbour_count>3:
                #dies due to overcrowding
                new_life[item]=0
            else:
                # cell stays alive
                new_life[item]=1
        elif life_dict[item]==0:
            if neighbour_count==3:
                new_life[item]=1
            else:
                new_life[item]=0
    return new_life

def main():

    #Initialization of the game board and cells
    pygame.init()
    global SURFACE
    global COUNT
    COUNT=0
    CLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    SURFACE.fill(WHITE)
    life_dict = resetLife()
    #life_dict = initializeLife(life_dict)
    #life_dict = RPentomino(life_dict)
    #life_dict = Loafer(life_dict)
    #life_dict = GosperGlider(life_dict)
    life_dict = StraightLine(life_dict,20)
    #life_dict = DrawLoaf(life_dict)
    #life_dict = DrawToad(life_dict)
    #life_dict = DrawGlider(life_dict)
    # life_dict = DrawEater(life_dict,[CELL_WIDTH/2,CELL_HEIGHT/2])

    for item in life_dict:
        colorize(item,life_dict)
    drawGrid()
    pygame.display.update()

    while True: #main loop that runs the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        COUNT += 1
        life_dict=runStep(life_dict)
        for item in life_dict:
            colorize(item,life_dict)
        drawGrid()
        pygame.display.update()
        CLOCK.tick(REFRESH)

if __name__=='__main__':
    main()