# WOLF RUNNER
# By Maria José Medina - Isaac Pachón Zuleta

import pygame
import random

Screen = pygame.display.set_mode((1000, 600))
from Wolf import *
from Assets import *
pygame.init()
#Inicializar mixer para sonido
pygame.mixer.init()

class Obstacle:
    """
    Clase que representa un obstáculo en el juego Wolf Runner.
    """
    def __init__(self, image, type):
        """
        Inicializa una instancia de la clase Obstacle.

        Args:
            image (list): Lista de imágenes del obstáculo.
            type (int): Tipo de obstáculo.
        """
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1000

    def update(self):
        """
        Actualiza la posición del obstáculo en el juego.
        """
        self.rect.x -= Game_Speed
        if self.rect.x < -self.rect.width:
            Obsta.pop()

    def draw(self, screen):
        """
        Dibuja el obstáculo en la pantalla del juego.

        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        """
        screen.blit(self.image[self.type], self.rect)

class Ghost(Obstacle):
    """
    Clase que representa un fantasma en el juego Wolf Runner.
    """
    def __init__(self, image):
        """
        Inicializa una instancia de la clase Ghost.

        Args:
            image (list): Lista de imágenes del fantasma.
        """
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 480
        self.index = 0

    def draw(self, screen):
        """
        Dibuja el fantasma en la pantalla del juego.

        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        """
        if self.index >= len(self.image) * 10:
            self.index = 0
        screen.blit(self.image[self.index // 10], self.rect)
        self.index += 1

class TwoGhost(Obstacle):
    """
    Clase que representa dos fantasmas juntos en el juego Wolf Runner.
    """
    def __init__(self, image):
        """
        Inicializa una instancia de la clase TwoGhost.

        Args:
            image (list): Lista de imágenes de los dos fantasmas.
        """
        self.type = 0
        super().__init__(image, self.type)
        super().__init__(image, self.type)
        self.rect.y = 480
        self.index = 0

class Bat(Obstacle):
    """
    Clase que representa un murciélago en el juego Wolf Runner.
    """
    def __init__(self, image):
        """
        Inicializa una instancia de la clase Bat.

        Args:
            image (list): Lista de imágenes del murciélago.
        """
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 450
        self.index = 0

    def draw(self, screen):
        """
        Dibuja el murciélago en la pantalla del juego.

        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        """
        if self.index >= len(self.image) * 8:
            self.index = 0
        screen.blit(self.image[self.index // 8], self.rect)
        self.index += 1

def Game():
    """
    Función principal que ejecuta el juego Wolf Runner.
    """
    global Game_Speed, X_Pos_Bg, Y_Pos_Bg, Points, Obsta
    Game_Speed = 25
    Run = True
    clock = pygame.time.Clock()
    Player = Wolf()
    X_Pos_Bg = 0
    Y_Pos_Bg = 540
    Points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    Obsta = []

    def score():
        """
        Incrementa la puntuación del jugador y ajusta la velocidad del juego según la puntuación.
        """
        global Points, Game_Speed
        Points += 1
        if Points % 100 == 0:
            Game_Speed += 1

        text = font.render("Points: " + str(Points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        Screen.blit(text, textRect)

    def background():
        """
        Dibuja el fondo del juego con efecto de movimiento.
        """
        global X_Pos_Bg, Y_Pos_Bg
        Screen.blit(Sky, (0, 0))

        # Movimiento de montañas
        Screen.blit(Mountain, (X_Pos_Bg, Y_Pos_Bg-600))
        Screen.blit(Mountain, (X_Pos_Bg + 1000, Y_Pos_Bg-600))
        if X_Pos_Bg <= -1000:
            Screen.blit(Mountain, (X_Pos_Bg + 1000, Y_Pos_Bg-200))
            X_Pos_Bg = 0

        # Movimiento de montañas
        Screen.blit(Mountains, (X_Pos_Bg, Y_Pos_Bg-250))
        Screen.blit(Mountains, (X_Pos_Bg + 1000, Y_Pos_Bg-250))
        if X_Pos_Bg <= -1000:
            Screen.blit(Mountains, (X_Pos_Bg + 1000, Y_Pos_Bg-200))
            X_Pos_Bg = 0

        # Movimiento del suelo
        Screen.blit(Floor, (X_Pos_Bg, Y_Pos_Bg))
        Screen.blit(Floor, (X_Pos_Bg + 1000, Y_Pos_Bg))
        if X_Pos_Bg <= -1000:
            Screen.blit(Floor, (X_Pos_Bg + 1000, Y_Pos_Bg))
            X_Pos_Bg = 0

        # Movimiento de pinos
        Screen.blit(Pines, (X_Pos_Bg, Y_Pos_Bg-150))
        Screen.blit(Pines, (X_Pos_Bg + 1000, Y_Pos_Bg-150))
        if X_Pos_Bg <= -1000:
            Screen.blit(Pines, (X_Pos_Bg + 1000, Y_Pos_Bg-200))
            X_Pos_Bg = 0

        X_Pos_Bg -= Game_Speed

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()
        Player.draw(Screen)
        Player.update(userInput)

        if len(Obsta) == 0:
            if random.randint(0, 2) == 0:
                Obsta.append(Ghost(Ghost_Fly))
            elif random.randint(0, 2) == 1:
                Obsta.append(TwoGhost(Ghost_Fly))
            elif random.randint(0, 2) == 2:
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
