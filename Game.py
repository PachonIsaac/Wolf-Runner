import pygame
import random

Screen = pygame.display.set_mode((1000,600))
from Wolf import *
from Assets import *
pygame.init()

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1000


    def update(self):
        self.rect.x -= Game_Speed
        if self.rect.x < -self.rect.width:
            Obsta.pop()


    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class Ghost(Obstacle):
        def __init__(self, image):
            self.type = 0
            super().__init__(image, self.type)
            self.rect.y = 480
            self.index = 0

        def draw(self, screen):
            if self.index >= 4:
                self.index = 0
            screen.blit(self.image[self.index // 5], self.rect)
            self.index += 1



# class TwoGhost(Obstacle):
#     # Se implementa la clase TwoGhost para que aparezcan dos fantasmas a la vez, uno junto al otro
   


class Bat(Obstacle):

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 450
        self.index = 0

    def draw(self, screen):
        if self.index >= 3:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1


def Game():
    global Game_Speed, X_Pos_Bg, Y_Pos_Bg, Points, Obsta
    Game_Speed  = 20
    Run         = True
    clock       = pygame.time.Clock()
    Player      = Wolf()
    X_Pos_Bg    = 0
    Y_Pos_Bg    = 540
    Points      = 0
    font        = pygame.font.Font('freesansbold.ttf',20)
    Obsta = []

    def score():
        global Points, Game_Speed
        Points += 1
        if Points % 100 == 0:
            Game_Speed += 1

        text = font.render("Points: "+str(Points),True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = (900,40)
        Screen.blit(text, textRect)

    def background():
        global X_Pos_Bg, Y_Pos_Bg
        Screen.blit(Sky, (0,0))
        #Movement of floor
        Screen.blit(Floor, (X_Pos_Bg, Y_Pos_Bg))
        Screen.blit(Floor, (X_Pos_Bg + 1000, Y_Pos_Bg))
        if X_Pos_Bg <= -1000:
            Screen.blit(Floor, (X_Pos_Bg + 1000, Y_Pos_Bg))
            X_Pos_Bg = 0
        # #Movement of pines
        # Screen.blit(Pines, (X_Pos_Bg, Y_Pos_Bg-200))
        # Screen.blit(Pines, (X_Pos_Bg + 1000, Y_Pos_Bg-200))
        # if X_Pos_Bg <= -1000:
        #     Screen.blit(Pines, (X_Pos_Bg + 1000, Y_Pos_Bg-200))
        #     X_Pos_Bg = 0

        X_Pos_Bg -= Game_Speed


    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Screen.fill((255,255,255))
        userInput = pygame.key.get_pressed()


        background()
        Player.draw(Screen)
        Player.update(userInput)

        if len(Obsta) == 0:
            if random.randint(0,2) == 0:
                Obsta.append(Ghost(Ghost_Fly))
            # elif random.randint(0,2) == 1:
            #     Obsta.append(TwoGhost([Ghost_Fly], Game_Speed))
            elif random.randint(0,2) == 2:
                Obsta.append(Bat(Bat_Fly))
        
        for obstacle in Obsta:
            obstacle.draw(Screen)
            obstacle.update()
            if Player.wolf_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                Run = False
                
        
        

        score()
        clock.tick(30)
        pygame.display.update()

    return Points