import pygame
import os
pygame.mixer.init()

current_directory = os.path.dirname(__file__)
PrincipalMenu           = pygame.image.load(os.path.join(current_directory, "Assets/Background/PrincipalMenu.png" ))
ScoreMenu               = pygame.image.load(os.path.join(current_directory, "Assets/Background/ScoreMenu.png" ))
NicknameMenu            = pygame.image.load(os.path.join(current_directory, "Assets/Background/Nickname.png" ))
Ghost_Fly               = [pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost1.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost2.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost3.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost4.png")).convert_alpha(),pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost5.png")).convert_alpha(),
                           pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost6.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost7.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost8.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost9.png")).convert_alpha(),pygame.image.load(os.path.join(current_directory, "Assets/Ghost/Ghost10.png")).convert_alpha()] 
Bat_Fly                 = [pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat1.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat2.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat3.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat4.png")).convert_alpha(),
                           pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat5.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat6.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat7.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Bat/Bat8.png")).convert_alpha()]

#Buttons
Play_Button             = [pygame.image.load(os.path.join(current_directory, "Assets/Other/Play_OFF.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Other/Play_ON.png")).convert_alpha()]
Exit_Button             = [pygame.image.load(os.path.join(current_directory, "Assets/Other/Exit_OFF.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Other/Exit_ON.png")).convert_alpha()]
Retry_Button            = [pygame.image.load(os.path.join(current_directory, "Assets/Other/Retry_OFF.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Other/Retry_ON.png")).convert_alpha()]
Scores_Button           = [pygame.image.load(os.path.join(current_directory, "Assets/Other/Score_OFF.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Other/Score_ON.png")).convert_alpha()]

#Backgrounds
Sky                     = pygame.image.load(os.path.join(current_directory, "Assets/Background/Sky.png" ))
Floor                   = pygame.image.load(os.path.join(current_directory, "Assets/Background/Floor.png" ))
Mountain                = pygame.image.load(os.path.join(current_directory, "Assets/Background/Mountain.png" ))
Mountains               = pygame.image.load(os.path.join(current_directory, "Assets/Background/Mountains.png" ))
Pines                   = pygame.image.load(os.path.join(current_directory, "Assets/Background/Pines.png" ))

#Wolf
Wolf_Run                = [pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Wolf.png")),pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Run1.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Run2.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Run3.png")).convert_alpha(), pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Run4.png")).convert_alpha()]
Wolf_Crounching         = pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Crounching.png")).convert_alpha()
Wolf_Run1               = pygame.image.load(os.path.join(current_directory, "Assets/Wolf/Run1.png")).convert_alpha()

#Sound
MenuSong                = pygame.mixer.Sound(os.path.join(current_directory, "Assets/Sound/heisenburger.mp3"))
ForestSong              = pygame.mixer.Sound(os.path.join(current_directory, "Assets/Sound/forest.mp3"))
GameOverSong            = pygame.mixer.Sound(os.path.join(current_directory, "Assets/Sound/GameOver.mp3"))

#Font
pixel_font              = os.path.join(current_directory, "Assets/Font/Pixels.ttf")