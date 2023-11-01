#OBSTACLE CLASS

import pygame
class Obstacle:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        # Lógica de movimiento o comportamiento del obstáculo
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
