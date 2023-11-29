#WOLF RUNNER 
# By Maria José Medina -Isaac Pachón Zuleta

import pygame
import sys
from pygame.locals import *
from Game import *
from ScoreMenu import *

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
            #Musica de fondo miestras selecciona
            MenuSong.play(-1)

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
    
    def show_text_input(self):
        input_active = True
        input_text = ""
        clock = pygame.time.Clock()
        input_rect = pygame.Rect(550, 440, 150, 50)
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('gray15')
        color = color_passive
        blink_activate = True

        while input_active:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        input_active = not input_active
                    color = color_active if input_active else color_passive
                if event.type == KEYDOWN:
                    if input_active:
                        if event.key == K_RETURN:
                            input_active = False
                        elif event.key == K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            self.screen.blit(NicknameMenu, (0, 0))
            if blink_activate:
                pygame.draw.rect(self.screen, color, input_rect, 2)
            else:
                text_color = (255, 255, 255) if input_active else (0, 0, 0)
            pygame.draw.rect(self.screen, color, input_rect, 2)

            text_surface = self.font.render(input_text or "|", True, (255, 255, 255))
            width = max(200, text_surface.get_width() + 10)
            input_rect.w = width
            self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            pygame.display.flip()
            clock.tick(30)

        return input_text


def main_menu():
    options = ["Score", "Play", "Exit"]

    menu = Menu(screen, options)
    while True:
        selected_game = menu.run()
        if selected_game == "Score":
            selected_game = Scores_Window()
            
        if selected_game == "Play":
            pygame.display.update()
            MenuSong.stop()
            ForestSong.play(-1)
            final_score = Game()
            print("Puntaje final:", final_score)

            # Guardar el puntaje solo si está entre los 10 mejores
            high_scores = read_high_scores()
            if is_high_score(final_score, high_scores):
                # Solicitar el nombre al jugador
                pygame.display.update()
                player_name = menu.show_text_input()
                high_scores.append({"name": player_name, "score": final_score})
                high_scores.sort(key=lambda x: x["score"], reverse=True)
                write_high_scores(high_scores)

            print("Puntaje final:", final_score)
        
        # Salir
        if selected_game == "Exit":
            pygame.quit()
            sys.exit()

# ... (código existente)

def read_high_scores():
    try:
        with open("scores.txt", "r") as file:
            content = file.read()
            if content.strip():  # Verificar si el contenido no está vacío
                high_scores = eval(content)
            else:
                high_scores = []
    except FileNotFoundError:
        # Si el archivo no existe, retorna una lista vacía
        high_scores = []
    return high_scores

def is_high_score(score, high_scores):
    # Verificar si el puntaje es uno de los 10 mejores
    return len(high_scores) < 10 or score > high_scores[-1]["score"]

def write_high_scores(high_scores):
    # Escribir los 10 mejores puntajes en el archivo
    with open("scores.txt", "w") as file:
        # Ordenar la lista de puntajes antes de escribir en el archivo
        high_scores.sort(key=lambda x: x["score"], reverse=True)
        file.write(repr(high_scores[:10]))

# ... (código existente)



if __name__ == "__main__":
    main_menu()