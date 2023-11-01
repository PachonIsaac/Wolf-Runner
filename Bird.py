#BIRD CLASS

import pygame
import os

current_directory = os.path.dirname(__file__)


class Bird:

    def __init__(self):
        self.width = 50
        self.height = 50
        self.x_coor = 800
        self.y_coor = 200
        self.x_speed = 0
        self.y_speed = 0
        self.image = pygame.image.load(os.path.join(current_directory, "Assets/Bird/Bird.png")).convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, (self.x_coor, self.y_coor))  

    def move(self):
        self.x_coor += self.x_speed
        self.y_coor += self.y_speed
