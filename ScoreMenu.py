# WOLF RUNNER
# By Maria José Medina - Isaac Pachón Zuleta

import sys
import pygame
from Menu import read_high_scores

Screen = pygame.display.set_mode((1000, 600))
from Wolf import *
from Assets import *
pygame.init()
#Inicializar mixer para sonido
pygame.mixer.init()


def Scores_Window():
    Screen.blit(ScoreMenu, (0, 0))
    pygame.display.update()
    scores = read_high_scores()
    font = pygame.font.Font(pixel_font, 36)
    
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            Screen.blit(ScoreMenu, (0, 0))
            Screen.blit(Play_Button[0], pygame.Rect(500, 500, 150, 50))
            Screen.blit(Exit_Button[0], pygame.Rect(800, 500, 150, 50))
            for i in range(len(scores)):
                text_name = scores[i]["name"]
                text_score = str(scores[i]["score"])
                text1 = font.render(text_name, True, (0, 255, 0))
                text2 = font.render(text_score, True, (0, 255, 0))
                Screen.blit(text1, (500, 80 + i * 40))
                Screen.blit(text2, (900, 80 + i * 40))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                if 500 <= mouse_pos[0] <= 650 and 500 <= mouse_pos[1] <= 550:
                    Screen.blit(Play_Button[1], pygame.Rect(500, 500, 150, 50))
                elif 800 <= mouse_pos[0] <= 950 and 500 <= mouse_pos[1] <= 550:
                    Screen.blit(Exit_Button[1], pygame.Rect(800, 500, 150, 50))
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if 500 <= mouse_pos[0] <= 650 and 500 <= mouse_pos[1] <= 550:
                    return "Play"
                if 800 <= mouse_pos[0] <= 950 and 500 <= mouse_pos[1] <= 550:
                    return "Exit"
        pygame.display.update()