# WOLF RUNNER
# By Maria José Medina - Isaac Pachón Zuleta

import pygame
from Assets import Wolf_Crounching, Wolf_Run, Wolf_Run1

class Wolf:
    """
    Clase que representa al personaje principal, el lobo, en el juego Wolf Runner.

    Atributos:
    x_coor (int): Coordenada en el eje x del lobo.
    y_coor (int): Coordenada en el eje y del lobo.
    y_coor_crounching (int): Coordenada en el eje y del lobo cuando está agachado.
    Jump_Vel (int): Velocidad de salto del lobo.
    """
    x_coor = 50
    y_coor = 500
    y_coor_crounching = 530
    Jump_Vel = 8.5

    def __init__(self):
        """
        Inicializa la instancia de la clase Wolf.

        Atributos:
            crounch_img (pygame.Surface): Imagen del lobo agachado.
            run_img (list): Lista de imágenes del lobo corriendo.
            jump_img (pygame.Surface): Imagen del lobo saltando.
            wolf_crounch (bool): Indica si el lobo está agachado.
            wolf_run (bool): Indica si el lobo está corriendo.
            wolf_jump (bool): Indica si el lobo está saltando.
            step_index (int): Índice para rastrear el paso actual en la animación.
            jump_vel (float): Velocidad de salto del lobo.
            image (pygame.Surface): Imagen actual del lobo.
            wolf_rect (pygame.Rect): Rectángulo que rodea al lobo en la pantalla.
        """
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
        """
        Actualiza el estado del lobo según la entrada del usuario.

        Args:
            userInput (dict): Diccionario que indica las teclas presionadas por el usuario.
        """
        if self.wolf_crounch:
            self.crounch()
        if self.wolf_run:
            self.run()
        if self.wolf_jump:
            self.jump()

        if self.step_index >= 12:
            self.step_index = 0

        if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] and not self.wolf_jump:
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
        """
        Realiza la animación de correr del lobo.
        """
        self.image = self.run_img[self.step_index // 5]
        self.wolf_rect = self.image.get_rect()
        self.wolf_rect.x = self.x_coor
        self.wolf_rect.y = self.y_coor
        self.step_index += 1

    def crounch(self):
        """
        Realiza la animación de agacharse del lobo.
        """
        self.image = self.crounch_img
        self.wolf_rect = self.image.get_rect()
        self.wolf_rect.x = self.x_coor
        self.wolf_rect.y = self.y_coor_crounching
        self.step_index += 1
    
    def jump(self):
        """
        Realiza la animación de saltar del lobo.
        """
        self.image = self.jump_img
        if self.wolf_jump:
            self.wolf_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.Jump_Vel:
            self.wolf_jump = False
            self.jump_vel = self.Jump_Vel

    def draw(self, screen):
        """
        Dibuja al lobo en la pantalla.

        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        """
        screen.blit(self.image, (self.wolf_rect.x, self.wolf_rect.y))
