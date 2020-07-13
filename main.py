import sys
sys.path.append('Image/ProcessImg')
from Entities import entities as pi
import pygame
from pygame.locals import *

def main():
    WIDTH    = 800
    HEIGHT   = 600
    CELLSIZE = 40
    pygame.init()
    pygame.display.set_caption('Swarm Intelligence Game of Life')
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    
    Automata_1 = pi.GameOfLife("Turismo", "Image/TestImg/test.jpg", 'Image/CutImg/Turismo/', \
                             WIDTH, HEIGHT, CELLSIZE, 5)
    Automata_2 = pi.GameOfLife("Turismo", "Image/TestImg/machu.jpg", 'Image/CutImg/Machu/', \
                            WIDTH, HEIGHT, CELLSIZE, 10)
    Top = pi.Display(800, 600, 40, SURFACE)
    Top.AddAutomata(Automata_1)
    #Top.AddAutomata(Automata_2)
    Automata_1.Loafer()
    #Automata_2.initializeLife()
    while True:  # main loop that runs the game
        SURFACE.fill(pi.WHITE)
        Top.PutOnScreen()
        pygame.display.update()
        Top.RunStep()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                for automata in Top.Automatas:
                    automata.RemoveImages()
                sys.exit()
            if event.type == KEYDOWN:
                for automata in Top.Automatas:
                    automata.initializeLife()

        CLOCK.tick(50)
if __name__ == "__main__":
    main()