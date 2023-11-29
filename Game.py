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
    Contiene los metodos
    - __init__ "Constructor"
    - update   "Actualiza la posición del obstáculo en el juego"
    - draw     "Dibuja el obstáculo en la pantalla del juego"
    
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
    Tiene los metodos:
    - __init__ "Constructor"
    - draw     "Dibuja el fantasma en la pantalla del juego"
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
    tiene los metodos:
    - __init__ "Constructor"
    - update   "Actualiza la posición del conjunto de dos fantasmas en el juego"
    - draw     "Dibuja los dos fantasmas en la pantalla del juego"
    """
    def __init__(self, image):
        """
        Inicializa una instancia de la clase TwoGhost.

        Args:
            image (list): Lista de imágenes del conjunto de dos fantasmas.
        """
        super().__init__(image, 0)
        self.rect.y = 480
        self.index = 0

    def update(self):
        """
        Actualiza la posición del conjunto de dos fantasmas en el juego.
        """
        self.rect.x -= Game_Speed
        if self.rect.x < -self.rect.width:
            Obsta.pop()

    def draw(self, screen):
        """
        Dibuja los dos fantasmas en la pantalla del juego.

        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        """
        screen.blit(self.image[0], self.rect)
        # Ajusta la posición del segundo fantasma a la derecha del primero
        screen.blit(self.image[0], (self.rect.x + self.rect.width, self.rect.y))


class Bat(Obstacle):
    """
    Clase que representa un murciélago en el juego Wolf Runner.
    Tiene los metodos:
    - __init__ "Constructor"
    - draw     "Dibuja el murciélago en la pantalla del juego"
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


def game_over():
    """
    Muestra la pantalla de "Game Over" y realiza acciones después de una colisión.
    """
    pygame.mixer.music.stop()  # Detener la música de fondo

    # Copiar la pantalla actual
    colision_final = Screen.copy()
    grayscale_image = pygame.Surface((colision_final.get_width(), colision_final.get_height()))
    
    for x in range(colision_final.get_width()):
        for y in range(colision_final.get_height()):
            color = colision_final.get_at((x, y))
            grayscale_color = (int(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]),) * 3
            grayscale_image.set_at((x, y), grayscale_color)
    
    Screen.blit(grayscale_image, (0, 0))
    pygame.display.update()
    GameOverSong.play() 
    pygame.time.wait(3000)
   



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
                print("Two Ghost")
            elif random.randint(0, 2) == 2:
                Obsta.append(Bat(Bat_Fly))
        
        for obstacle in Obsta:
            obstacle.draw(Screen)
            obstacle.update()
            if Player.wolf_rect.colliderect(obstacle.rect):
                game_over() 
                Run = False
    
        
        score()
        pygame.display.update()
        clock.tick(30)
    
    return Points