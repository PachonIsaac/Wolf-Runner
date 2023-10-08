import pygame
import os

# Inicializa pygame
pygame.init()
# Get the actual directory
current_directory = os.path.dirname(__file__)
# Dimensions of the screen
Screen_Size = (800, 600)

# Create a screen
screen = pygame.display.set_mode(Screen_Size) 
clock = pygame.time.Clock()
done= False

#Load Images 
Start_Background        = os.path.join(current_directory, "Assets/Background/Start.png")
Button_Play             = os.path.join(current_directory, "Assets/Other/Button Play.png")
Button_Play_Iluminated  = os.path.join(current_directory, "Assets/Other/Button Play Iluminated.png")
Game_Background         = os.path.join(current_directory, "Assets/Background/GameBackground.png")

# status of button PLAY
button_play = False

# status of the game
in_game = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Analize if the user quit the game
            done = True
        
        elif event.type == pygame.MOUSEMOTION: #Analize if the user move the mouse
            mouse_pos = event.pos
            if mouse_pos[0] >= 325 and mouse_pos[0] <= 325+150 and mouse_pos[1] >= 540 and mouse_pos[1] <= 590: #Analize if the mouse is over the button PLAY
                button_play = True #Activate animation of button PLAY
            else:
                button_play = False #Deactivate animation of button PLAY
        elif event.type == pygame.MOUSEBUTTONDOWN and button_play: #Analize if the user click the mouse and the mouse is over the button PLAY
            in_game = True
            

    
    

    if not in_game:
        # Image of initial background (escalated to the size of the screen)
        background_image = pygame.image.load(Start_Background).convert()
        background_image = pygame.transform.scale(background_image, screen.get_size())
        screen.blit(background_image, (0, 0))
        if button_play:
            screen.blit(pygame.image.load(Button_Play_Iluminated).convert_alpha(), (325, 530))
        else:
            screen.blit(pygame.image.load(Button_Play).convert_alpha(), (325, 530))
    else:
        screen.blit(pygame.image.load(Game_Background).convert_alpha(), (0, 0)) # Image of game background
        # Lógica del juego aquí
        # Puedes agregar toda la lógica del juego dentro de este bloque
    
    
    # Actualizate the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()