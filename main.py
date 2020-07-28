import sys

sys.path.append('Image/ProcessImg')
sys.path.append('Image/GetImg/Twitter')

from Entities import entities as pi
import api as ap
from shutil import rmtree
import pygame
from pygame.locals import *
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREY = (40, 40, 40)

Folder = "Image/TestImg/"

WIDTH    = 800
HEIGHT   = 600
CELLSIZE = 40

SURFACE = None
CLOCK = None

Top = None
AutomataA = None
AutomataB = None

t0 = None
t1 = None

def InicializarAutomatas(FirstPath, SecondPath):
    global Top, AutomataA, AutomataB
    AutomataA = pi.GameOfLife("Turismo", FirstPath, 'Image/CutImg/Turismo/', \
                             WIDTH, HEIGHT, CELLSIZE, 0, 'R')
    AutomataB = pi.GameOfLife("Turismo", SecondPath, 'Image/CutImg/Machu/', \
                            WIDTH, HEIGHT, CELLSIZE,  0, 'B')
    Top = pi.Display(WIDTH, HEIGHT, CELLSIZE, SURFACE, [AutomataA, AutomataB])
    Top.InitializeLife()

def InitPygame():
    global SURFACE, CLOCK
    pygame.init()
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

def Update():
    global Top, SURFACE
    SURFACE.fill(WHITE)
    Top.PutOnScreen()
    pygame.display.update()

def QuitEv(event):
    global Top
    if(event.type == QUIT):
        pygame.quit()
        Top.RemoveImages()
        rmtree(Folder)
        sys.exit()

def ClickEv(event):
    global Top
    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
        Top.AddCell(pos)
        Update()

def PauseProgram():
    NotExit = True
    while NotExit:
        for event in pygame.event.get():
            QuitEv(event)
            ClickEv(event)
            if event.type == KEYDOWN:
                if event.key == ord("p"):
                    NotExit = False
                    break

def KeyDownEv(event):
    global Top, t0
    if(event.type == KEYDOWN):
        if(event.key == ord("p")):
            t0 = time.clock()
            PauseProgram()
        else:
            Top.InitializeLife()

def ShowTemp(path):
    global SURFACE
    
    img = Image.open(filepath)
    imgresize = img.resize( (width, height) )
    imgresize.save(path,'PNG')

    img = pygame.image.load(path).convert()
    
    SURFACE.fill(WHITE)
    SURFACE.blit(img, (0,0))
    SURFACE.pygame.display.update()                    

def main():
    global Top, AutomataA, AutomataB, SURFACE, CLOCK, t0, t1
    Hashtags = ap.getInputHastags()
    FileNames = ap.dowloadImagesbyHastag(Hashtags, Folder)
    
    FirstPath =  Folder + FileNames[0]  
    SecondPath =  Folder + FileNames[1] 
    FileNames.remove(FileNames[0])
    FileNames.remove(FileNames[0])

    InitPygame()
    InicializarAutomatas(FirstPath, SecondPath)

    t0 = time.clock()
    ShowTemp()
    while True:  # main loop that runs the game
        Update()
        CLOCK.tick(5)
        
        for event in pygame.event.get():
            QuitEv(event)
            ClickEv(event)
            KeyDownEv(event)

        Top.RunStep()
        t1 = time.clock()
        if( t1 - t0 >= 20):
            ShowTemp()
            if len(FileNames) != 0:
                FirstPath =  Folder + FileNames[0]  
                SecondPath =  Folder + FileNames[1] 
                Top.ImageChange([FirstPath,SecondPath])
                FileNames.remove(FileNames[0])
                FileNames.remove(FileNames[0])
            t0 = time.clock()

if __name__ == "__main__":
    main()