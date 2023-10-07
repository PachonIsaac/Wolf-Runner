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

#Load Images 
Start_Background = os.path.join(current_directory, "Assets/Background/Start.png")
Button_Play = os.path.join(current_directory, "Assets/Other/Button Play.png")
Button_Play_Iluminated = os.path.join(current_directory, "Assets/Other/Button Play Iluminated.png")

# status of button PLAY
button_play = False

# status of the game
in_game = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.VIDEORESIZE:
            new_size = event.size
            screen = pygame.display.set_mode(new_size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if mouse_pos[0] >= 280 and mouse_pos[0] <= 430 and mouse_pos[1] >= 540 and mouse_pos[1] <= 590:
                button_play = True
            else:
                button_play = False
        elif event.type == pygame.MOUSEBUTTONDOWN and button_play:
            in_game = True
            

    # Image of background (escalated to the size of the screen)
    background_image = pygame.image.load(Start_Background).convert()
    background_image = pygame.transform.scale(background_image, screen.get_size())
    screen.blit(background_image, (0, 0))

    if not in_game:
        if button_play:
            screen.blit(pygame.image.load(Button_Play_Iluminated).convert_alpha(), (280, 530))
        else:
            screen.blit(pygame.image.load(Button_Play).convert_alpha(), (280, 530))
    else:
        print("In Game") #Solo por llenar el else
        # Lógica del juego aquí
        # Puedes agregar toda la lógica del juego dentro de este bloque
    
    
    # Actualizate the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()