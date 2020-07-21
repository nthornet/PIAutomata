import sys
sys.path.append('Image/ProcessImg')
from Entities import entities as pi
sys.path.append('Image/GetImg/Twitter')
import api as ap
from shutil import rmtree
import pygame
from pygame.locals import *
import time

def main():
    Hashtags = ap.getInputHastags()
    directorio = "Image/TestImg/"
    FileNames = ap.dowloadImagesbyHastag(Hashtags, directorio)

    WIDTH    = 800
    HEIGHT   = 600
    CELLSIZE = 40
    pygame.init()
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()


    FirstPath =  "Image/TestImg/" + FileNames[0]  
    SecondPath =  "Image/TestImg/" + FileNames[1] 
    
    FileNames.remove(FileNames[0])
    FileNames.remove(FileNames[0])

    Automata_1 = pi.GameOfLife("Turismo", SecondPath, 'Image/CutImg/Turismo/', \
                             WIDTH, HEIGHT, CELLSIZE, 5, 'R')
    Automata_2 = pi.GameOfLife("Turismo", FirstPath, 'Image/CutImg/Machu/', \
                            WIDTH, HEIGHT, CELLSIZE, 10 , 'B')
    Top = pi.Display(800, 600, 40, SURFACE)
    Top.AddAutomata(Automata_1)
    Top.AddAutomata(Automata_2)
    Automata_1.Loafer()
    Automata_2.initializeLife()
    t0 = time.clock()
    while True:  # main loop that runs the game
        SURFACE.fill(pi.WHITE)
        Top.PutOnScreen()
        pygame.display.update()
        CLOCK.tick(5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                for automata in Top.Automatas:
                    automata.RemoveImages()
                rmtree(directorio)
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                Top.AddCell(pos)
            if event.type == KEYDOWN:
                if event.key == ord ("p"):
                    ext = True
                    while ext:
                        t0 = time.clock() 
                        for event2 in pygame.event.get():
                            if event2.type == KEYDOWN:
                                if event2.key == ord ("p"):
                                    ext = False 
                                    break     
                            if event2.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                Top.AddCell(pos)
                                SURFACE.fill(pi.WHITE)
                                Top.PutOnScreen()
                                pygame.display.update()                        
                else:
                    for automata in Top.Automatas:
                        automata.initializeLife() 

        Top.RunStep()
        t1 = time.clock()
        if( t1 - t0 >= 20):
            if len(FileNames) != 0:
                FirstPath =  "Image/TestImg/" + FileNames[0]  
                SecondPath =  "Image/TestImg/" + FileNames[1] 
                Top.ImageChange([FirstPath,SecondPath])
                FileNames.remove(FileNames[0])
                FileNames.remove(FileNames[0])
            t0 = time.clock()

        
if __name__ == "__main__":
    main()