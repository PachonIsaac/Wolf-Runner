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

#Fix route of the images
Start_Background        = os.path.join(current_directory, "Assets/Background/Start.png")
Button_Play             = os.path.join(current_directory, "Assets/Other/Button Play.png")
Button_Play_Iluminated  = os.path.join(current_directory, "Assets/Other/Button Play Iluminated.png")
Game_Background         = os.path.join(current_directory, "Assets/Background/GameBackground.png")

Shrub1                  = os.path.join(current_directory, "Assets/Tree/Shrub1.png")
Shrub2                  = os.path.join(current_directory, "Assets/Tree/Shrub2.png")
Tree                    = os.path.join(current_directory, "Assets/Tree/Tree1.png")
Bird1                   = os.path.join(current_directory, "Assets/Bird/Bird1.png")
Bird2                   = os.path.join(current_directory, "Assets/Bird/Bird2.png")
Bird3                   = os.path.join(current_directory, "Assets/Bird/Bird3.png")

#Load images
Start_Background        = pygame.image.load(Start_Background).convert()
Button_Play             = pygame.image.load(Button_Play).convert_alpha()
Button_Play_Iluminated  = pygame.image.load(Button_Play_Iluminated).convert_alpha()
Game_Background         = pygame.image.load(Game_Background).convert_alpha()
Shrub1                  = pygame.image.load(Shrub1).convert_alpha()
Shrub2                  = pygame.image.load(Shrub2).convert_alpha()
Tree                    = pygame.image.load(Tree).convert_alpha()
Bird_FlyImages          = [pygame.image.load(Bird1).convert_alpha(), pygame.image.load(Bird2).convert_alpha(), pygame.image.load(Bird3).convert_alpha()]

# Index of the image of the wolf
Wolf_Index = 0
# Index of the image of the bird
Bird_Index = 0

# status of button PLAY
button_play = False

# If the wolf is crounching
is_crounching = False

#If the wolf is jumping
is_jumping = False

# status of the game

in_game = False

# Speed variables
Game_speed = 1  # Initial speed
Max_Game_Speed = 50  # Maximum speed

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
        # Image of initial background
        screen.blit(Start_Background, (0, 0))
        if button_play:
            screen.blit(Button_Play_Iluminated, (325, 530))
        else:
            screen.blit(Button_Play, (325, 530))

    else: #Start the game
        screen.blit(Game_Background, (0, 0)) # Image of game background
        
        #Pruebas
        #Aument speed
        if Game_speed < Max_Game_Speed:
                Game_speed += 0.1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    is_crounching = True
                elif event.key == pygame.K_UP:
                    is_jumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    is_crounching = False
                elif event.key == pygame.K_UP:
        #             is_jumping = False
        # if is_crounching and not is_jumping:
        #     screen.blit(Wolf_Crounching, (20, 450))
        # elif is_jumping:
        #     screen.blit(Wolf_RunImages[0], (20, 450))
        # else:
        #     screen.blit(Wolf_RunImages[Wolf_Index], (20, 450))
        #     Wolf_index = (Wolf_Index + 1) %  len(Wolf_RunImages)
            
        # clock.tick(Game_speed)
        # Fin de pruebas

        
        pygame.display.update()
        
    
    
    # Actualizate the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()