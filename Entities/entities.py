import sys,pygame
import random
import os
from math import floor 
from shutil import rmtree
from copy import copy
from pygame.locals import *
try:
    from Process import ProcesarImagen
except:
    sys.path.append('../Image/ProcessImg/')
    from Process import ProcesarImagen

class Display():
    def __init__(self, width, height, cellsize, screen, listAutomatas = []):
        self.Width = width
        self.Height = height
        self.Cell = cellsize
        self.Automatas = listAutomatas
        self.screen = screen

    def AddAutomata(self, Automata):
        self.Automatas.append(Automata) 

    def RunStep(self):
        for automata in self.Automatas:
            automata.RunStep()
            automata.Colorize()

    def ImageChange(self,filenames):  
        for i in range(len(filenames)):
            self.Automatas[i].ImageChange(filenames[i])
        for automata in self.Automatas:
            automata.initializeLife()
    
    def RemoveImages(self):
        for automata in self.Automatas:
            automata.RemoveImages()

    def AddCell(self,pos):
        for automata in self.Automatas:
            automata.AddCell(pos)
            automata.Colorize()

    def InitializeLife(self):
        for automata in self.Automatas:
            automata.initializeLife()

    def PutOnScreen(self):
        OrderedAutomatons = sorted(self.Automatas, key = lambda automata : automata.Priority, reverse = True)

        cell_width = int(self.Width / self.Cell)
        cell_height = int(self.Height / self.Cell)
        for y in range(0, cell_height):
            for x in range(0, cell_width):
                for automata in OrderedAutomatons:
                    if(automata.life_dict[x,y].alive == 1):
                        image       = automata.life_dict[x,y].convertedImage
                        coordinates = automata.life_dict[x,y].slice.coords
                        self.screen.blit(image, coordinates)
                        break

class Celula():
    def __init__(self, alive, sliceImg):
        self.alive = alive
        self.slice = sliceImg
        self.convertedImage = pygame.image.load(self.slice.filename).convert()
        
class GameOfLife():
    def __init__(self, name,  filepath, DirectorySlices, DirectoryAutomata, width, height, cellsize, priority,color):
        self.name = name
        self.Width = width
        self.Height = height
        self.life_dict = self.GetLife_Dict(filepath, DirectorySlices, DirectoryAutomata, width, height, cellsize,color)
        self.Cellsize = cellsize
        self.Priority = priority 
        self.DirectorySlices = DirectorySlices
        self.DirectoryAutomata = DirectoryAutomata
        self.Color = color 

    def AddCell(self, pos):
        x = floor(pos[0]/self.Cellsize)
        y = floor(pos[1]/self.Cellsize)
        if self.life_dict[x,y].alive == 1:
            self.life_dict[x,y].alive = 0
        else:
            self.life_dict[x,y].alive = 1

    def GetLife_Dict(self, filepath, DirectorySlices, DirectoryAutomata, width, height, cellsize, color):
        try:
            os.makedirs(DirectorySlices)
        except:
            pass
        
        tiles = ProcesarImagen(filepath, DirectorySlices, DirectoryAutomata, width, height, cellsize, color)
        life_dict = {}

        cell_width = int(width/cellsize)
        cell_height = int(height/cellsize)
        
        for y in range(0, cell_height):
            for x in range(0, cell_width):
                life_dict[x,y] = Celula(0, tiles[y*cell_width+x])
        
        return life_dict

    def GetCell(self,x,y):
        return self.life_dict[x,y]

    
    def Colorize(self):
        for cell in self.life_dict.values():
            if(cell.alive == 0):
                cell.convertedImage.set_alpha(0)
            elif(cell.alive == 1):
                cell.convertedImage.set_alpha(255)

    def RunStep(self):
        new_life = {}
        for item in self.life_dict:
            neighbour_count = self.GetNeighbours(item)
            if self.life_dict[item].alive == 1:  # cell is alive and we need to check if it will stay alive
                if neighbour_count < 2:
                    # dies due to underpopulation
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
                elif neighbour_count > 3:
                    # dies due to overcrowding
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
                else:
                    # cell stays alive
                    new_life[item] = Celula(1, self.life_dict[item].slice) #1
            
            elif self.life_dict[item].alive == 0:
                if neighbour_count == 3:
                    new_life[item] = Celula(1, self.life_dict[item].slice) #1
                else:
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
        #   print('Run Step')
        self.life_dict = new_life

    def GetNeighbours(self, item):
        neighbour_count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                neighbour = (item[0] + x, item[1] + y)
                if neighbour[0] < self.Width and neighbour[0] >= 0:
                    if neighbour[1] < self.Height and neighbour[1] >= 0:
                        try:
                            if self.life_dict[neighbour].alive == 1 and (x, y) != (0, 0):
                                neighbour_count += 1
                        except KeyError:
                            t = 1
                            # catch key errors
                            # print "error"
        return neighbour_count

    def RemoveImages(self):
        try:
            rmtree(self.DirectorySlices)
        except:
            pass
    
    def ImageChange(self, filepath):
        self.life_dict.clear()
        self.RemoveImages()
        self.life_dict = self.GetLife_Dict(filepath, self.DirectorySlices, self.DirectoryAutomata, self.Width, self.Height, self.Cellsize,self.Color)
        self.Colorize()

    def Loafer(self):
        midx= int((self.Height/self.Cellsize)/2)
        midy= int((self.Width/self.Cellsize)/2)
        self.life_dict[midx-3,midy-5].alive = 1
        self.life_dict[midx-2,midy-5].alive = 1
        self.life_dict[midx+1,midy-5].alive = 1
        self.life_dict[midx+3,midy-5].alive = 1
        self.life_dict[midx+4,midy-5].alive = 1

        self.life_dict[midx-4,midy-4].alive = 1
        self.life_dict[midx-1,midy-4].alive = 1
        self.life_dict[midx+2,midy-4].alive = 1
        self.life_dict[midx+3,midy-4].alive = 1

        self.life_dict[midx-3,midy-3].alive = 1
        self.life_dict[midx-1,midy-3].alive = 1

        self.life_dict[midx-2,midy-2].alive = 1

        self.life_dict[midx+4,midy-1].alive = 1

        self.life_dict[midx+2,midy].alive = 1
        self.life_dict[midx+3,midy].alive = 1
        self.life_dict[midx+4,midy].alive = 1

        self.life_dict[midx+1,midy+1].alive = 1

        self.life_dict[midx+2,midy+2].alive = 1

        self.life_dict[midx+3,midy+3].alive = 1
        self.life_dict[midx+4,midy+3].alive = 1

        self.Colorize()

    def DrawSquare(self):
        cell_width = int(self.Width / self.Cellsize)
        cell_height = int(self.Height / self.Cellsize)

        qrtx=int(cell_height/4)
        qrty=int(cell_width/4)

        self.life_dict[qrtx+1,qrty].alive = 1
        self.life_dict[qrtx+1,qrty+1].alive = 1
        self.life_dict[qrtx+2,qrty].alive = 1
        self.life_dict[qrtx+2,qrty+1].alive = 1

        self.Colorize()
    
    def initializeLife(self):
        for cell in self.life_dict.values():
            cell.alive = random.randint(0,1)
        self.Colorize()