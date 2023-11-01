#WOLF CLASS
import pygame
import os
current_directory = os.path.dirname(__file__)

Wolf                    = os.path.join(current_directory, "Assets/Wolf/Wolf.png")
Wolf_Run1               = os.path.join(current_directory, "Assets/Wolf/Run1.png")
Wolf_Run2               = os.path.join(current_directory, "Assets/Wolf/Run2.png")
Wolf_Run3               = os.path.join(current_directory, "Assets/Wolf/Run3.png")
Wolf_Run4               = os.path.join(current_directory, "Assets/Wolf/Run4.png")
Wolf_Crounching         = os.path.join(current_directory, "Assets/Wolf/Crounching.png")
Wolf_RunImages          = [pygame.image.load(Wolf_Run1).convert_alpha(), pygame.image.load(Wolf_Run2).convert_alpha(), pygame.image.load(Wolf_Run3).convert_alpha(), pygame.image.load(Wolf_Run4).convert_alpha()]


class Wolf:
    def __init__(self):
        self.width = 15
        self.height = 90
        self.x_coor = 50
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.jump = False
        self.image = Wolf_Run1

    def draw(self, screen):
        screen.blit(self.image, (self.x_coor, self.y_coor))

    def move(self):
        self.x_coor += self.x_speed
        self.y_coor += self.y_speed

    def jump(self):
        self.y_speed = -10
        self.jump = True

    def crounch(self):
        self.image = Wolf_Crounching

 
