import pygame
import sys
from pygame.locals import *
from Game import *

pygame.init()
#Crear la ventana
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Wolf-Runner")
from Assets import *



class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"image": Play_Button[0], "rect": pygame.Rect(425, 500, 150, 50), "game": "Play"},
            {"image": Scores_Button[0], "rect": pygame.Rect(175, 500, 150, 50), "game": "Score"},
            {"image": Exit_Button[0], "rect": pygame.Rect(675, 500, 150, 50), "game": "Exit"},
        ]

    def draw_menu(self):
        self.screen.blit(PrincipalMenu, (0, 0))
        for button in self.buttons:
            self.screen.blit(button["image"], button["rect"])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            selected_game = button["game"]
                            return selected_game

                self.draw_menu()

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    if 425 <= mouse_pos[0] <= 575 and 500 <= mouse_pos[1] <= 550:
                        self.screen.blit(Play_Button[1], (425, 500))
                    if 175 <= mouse_pos[0] <= 325 and 500 <= mouse_pos[1] <= 550:
                        self.screen.blit(Scores_Button[1], (175, 500))
                    if 675 <= mouse_pos[0] <= 825 and 500 <= mouse_pos[1] <= 550:
                        self.screen.blit(Exit_Button[1], (675, 500))
                
            pygame.display.update()

def main_menu():
    options = ["Score", "Play", "Exit"]

    menu = Menu(screen, options)
    while True:
        selected_game = menu.run()
        if selected_game == "Play":
            screen.fill((0,0,0)) #Mientras tanto
            pygame.display.update()
            #Aquí va el llamado al Game.py
            final_score = Game()
            print("Puntaje final:", final_score)
        
        # Salir
        if selected_game == "Exit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main_menu()