import pygame
import os

# Inicializa pygame
pygame.init()
# Obtiene la ruta del directorio actual
current_directory = os.path.dirname(__file__)

SKY_BLUE  = (128, 191, 255)

Initial_Size = (700, 600)

# Create a screen
screen = pygame.display.set_mode(Initial_Size)
clock = pygame.time.Clock()
done= False

Start_Background = os.path.join(current_directory, "Assets/Background/Start.jpeg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.VIDEORESIZE:
            new_size = event.size
            screen = pygame.display.set_mode(new_size, pygame.RESIZABLE)

    # Image of background (escalated to the size of the screen)
    background_image = pygame.image.load(Start_Background).convert()
    background_image = pygame.transform.scale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))
    
    # Actualizate the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()