#WOLF CLASS
import pygame
from Assets import Wolf_Crounching, Wolf_Run, Wolf_Run1


class Wolf:
    x_coor = 50
    y_coor = 500
    y_coor_crounching= 530
    Jump_Vel = 8.5

    def __init__(self):
        self.crounch_img = Wolf_Crounching
        self.run_img = Wolf_Run
        self.jump_img = Wolf_Run1

        self.wolf_crounch = False
        self.wolf_run = True
        self.wolf_jump = False

        self.step_index = 0
        self.jump_vel = self.Jump_Vel
        self.image = self.run_img[0]
        self.wolf_rect = self.image.get_rect()
        self.wolf_rect.x = self.x_coor
        self.wolf_rect.y = self.y_coor

    def update(self, userInput):
        if self.wolf_crounch:
            self.crounch()
        if self.wolf_run:
            self.run()
        if self.wolf_jump:
            self.jump()

        if self.step_index >= 12:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.wolf_jump:
            self.wolf_crounch = False
            self.wolf_run = False
            self.wolf_jump = True
        if userInput[pygame.K_DOWN] and not self.wolf_jump:
            self.wolf_crounch = True
            self.wolf_run = False
            self.wolf_jump = False
        elif not (self.wolf_jump or userInput[pygame.K_DOWN]):
            self.wolf_crounch = False
            self.wolf_run = True
            self.wolf_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.wolf_rect = self.image.get_rect()
        self.wolf_rect.x = self.x_coor
        self.wolf_rect.y = self.y_coor
        self.step_index += 1

    def crounch(self):
        self.image = self.crounch_img
        self.wolf_rect = self.image.get_rect()
        self.wolf_rect.x = self.x_coor
        self.wolf_rect.y = self.y_coor_crounching
        self.step_index += 1
    
    def jump(self):
        self.image = self.jump_img
        if self.wolf_jump:
            self.wolf_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.Jump_Vel:
            self.wolf_jump = False
            self.jump_vel = self.Jump_Vel

    def draw(self, screen):
        screen.blit(self.image, (self.wolf_rect.x, self.wolf_rect.y))

 
