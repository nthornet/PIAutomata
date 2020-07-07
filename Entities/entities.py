import sys,pygame
from pygame.locals import *
try:
    from Process import ProcesarImagen
except:
    sys.path.append('../Image/ProcessImg/')
    from Process import ProcesarImagen

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREY = (40, 40, 40)

class Display():
    def __init__(self, width, height, cellsize):
        self.WIDTH = width
        self.HEIGHT = height
        self.CELL = cellsize
        self.Automatas = []
        self.screen = None
        self.CLOCK = None

    def AddAutomata(self, Automata):
        self.Automatas.append(Automata)

    def DrawGrid(self):
        for item in self.Automatas[0].life_dict.values():
           item.convertedImage = pygame.image.load(item.slice.filename).convert()            

    def PlayGame(self): 
        pygame.init()
        pygame.display.set_caption('Swarm Intelligence Game of Life')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CLOCK = pygame.time.Clock()

        self.DrawGrid()
        self.Automatas[0].Colorize()
        self.PutOnScreen()

        while True:  # main loop that runs the game
            pygame.display.update()
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.RunStep()
            self.PutOnScreen()
            self.CLOCK.tick(5)

    def RunStep(self):
        for automata in self.Automatas:
            automata.RunStep()
            automata.Colorize()

    def PutOnScreen(self):
        for item in self.Automatas[0].life_dict:
            image       = self.Automatas[0].life_dict[item].convertedImage
            coordinates = self.Automatas[0].life_dict[item].slice.coords
            self.screen.blit(image, coordinates)

class Celula():
    def __init__(self, alive, sliceImg, convertedImage = None):
        self.alive = alive
        self.slice = sliceImg
        self.convertedImage = convertedImage
        
class GameOfLife():
    def __init__(self, name,  filepath, directory, width, height, cellsize):
        self.name = name
        self.WIDTH = width
        self.HEIGHT = height
        self.life_dict = self.GetLife_Dict(filepath, directory, width, height, cellsize)
        self.Cellsize = cellsize

    def GetLife_Dict(self, filepath, directory, width, height, cellsize):
        tiles = ProcesarImagen(filepath, directory, width, height, cellsize)
        
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
        cell_width = int(self.WIDTH / self.Cellsize)
        cell_height = int(self.HEIGHT / self.Cellsize)

        for y in range(0, cell_height):
            for x in range(0, cell_width):
                if self.life_dict[x, y].alive == 0:
                    self.life_dict[x, y].convertedImage.set_alpha(0)
                elif self.life_dict[x, y].alive == 1:
                    self.life_dict[x, y].convertedImage.set_alpha(255)

    def RunStep(self):
        new_life = {}
        for item in self.life_dict:
            neighbour_count = self.GetNeighbours(item)
            if self.life_dict[item].alive == 1:  # cell is alive and we need to check if it will stay alive
                if neighbour_count < 2:
                    # dies due to underpopulation
                    new_life[item] = Celula(0, self.life_dict[item].slice, self.life_dict[item].convertedImage)  # 0
                elif neighbour_count > 3:
                    # dies due to overcrowding
                    new_life[item] = Celula(0, self.life_dict[item].slice, self.life_dict[item].convertedImage)  # 0
                else:
                    # cell stays alive
                    new_life[item] = Celula(1, self.life_dict[item].slice, self.life_dict[item].convertedImage)  # 1

            elif self.life_dict[item].alive == 0:
                if neighbour_count == 3:
                    new_life[item] = Celula(1, self.life_dict[item].slice, self.life_dict[item].convertedImage)  # 1
                else:
                    new_life[item] = Celula(0, self.life_dict[item].slice, self.life_dict[item].convertedImage)  # 0
        #   print('Run Step')
        self.life_dict = new_life

    def GetNeighbours(self, item):
        neighbour_count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                neighbour = (item[0] + x, item[1] + y)
                if neighbour[0] < self.WIDTH and neighbour[0] >= 0:
                    if neighbour[1] < self.HEIGHT and neighbour[1] >= 0:
                        try:
                            if self.life_dict[neighbour].alive == 1 and (x, y) != (0, 0):
                                neighbour_count += 1
                        except KeyError:
                            t = 1
                            # catch key errors
                            # print "error"
        return neighbour_count

    def Loafer(self):
        midx= int((self.HEIGHT/self.Cellsize)/2)
        midy= int((self.WIDTH/self.Cellsize)/2)
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

if __name__ == '__main__':
    Go = Display(800,600,40)
    Automata_1 = GameOfLife("Turismo", "../Image/TestImg/test.jpg", '../Image/CutImg/', \
                             Go.WIDTH, Go.HEIGHT, Go.CELL)
    Automata_1.Loafer()
    Go.AddAutomata(Automata_1)
    Go.PlayGame()
