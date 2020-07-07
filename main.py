import sys
sys.path.append('Image/ProcessImg')
from Entities import entities as pi

Top = pi.Display(800,600,40)
Automata_1 = pi.GameOfLife("Turismo", "Image/TestImg/test.jpg", 'Image/CutImg/', \
                            Top.WIDTH, Top.HEIGHT, Top.CELL)
Automata_1.Loafer()
Top.AddAutomata(Automata_1)
Top.PlayGame()