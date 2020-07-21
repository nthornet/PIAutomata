import random


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
        life_dict[cell]= random.randint(0,1)
    return life_dict