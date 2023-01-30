import pygame
import os

pygame.init()

def create_path():
    path_abs = os.path.abspath(__file__ + "/..")
    path_abs = path_abs.split("\\") 
    del path_abs[-1]
    path_abs = "\\".join(path_abs)
    return path_abs

class Settings:
    def __init__(self, x = None, y = None, width = None, height = None, name_image = None, color = None):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.IMAGE = None
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) 
        self.COLOR = color
        if self.NAME_IMAGE:
            self.load_image()

    def load_image(self,direction = False):
        path_image = create_path()
        path_image = os.path.join(path_image, self.NAME_IMAGE)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE,direction,False)

    def blit_sprite(self,win):
        win.blit(self.IMAGE, (self.X,self.Y))


    def draw_rect(self, win):
            pygame.draw.rect(win, self.COLOR, self.RECT)

bg = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/background/bg.png")
bg_pipes = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/pipes/bg_pipes.png")
bg_menu = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg_menu_1.png")
bg_minigame = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg_inglation_minigame.png")

play = Settings(color =(255,0,0), x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/play.png")
play.RECT = pygame.Rect(470, 320, 300, 80)
developers = Settings(color =(255,0,0), x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/developers.png")
developers.RECT = pygame.Rect(470, 440, 300, 80)
exit = Settings(color =(255,0,0), x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/exit.png")
exit.RECT = pygame.Rect(470, 550, 300, 80)
bg_developers = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg_developers.png")
back = Settings(x = 700,y = 0, width = 100, height = 100,name_image = "game2/images/back.png")
lever = Settings(x = 20,y = 620, width = 60, height = 60,name_image = "game2/images/lever.png")
injured = Settings(x = 750,y = 675, width = 50, height = 50,name_image = "game2/images/injured.png")