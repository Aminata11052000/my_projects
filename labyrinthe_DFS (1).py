import time
import pygame
import sys
import random
from pygame.locals import *

# Fonction que vous souhaitez mesurer (DFS dans ce cas)
def dfs_solve_labyrinth():
    # Votre implémentation DFS ici
    pass

# Mesurer le temps d'exécution pour l'algorithme DFS
start_time_dfs = time.time()
dfs_solve_labyrinth()
end_time_dfs = time.time()

# Afficher le temps d'exécution pour l'algorithme DFS
execution_time_dfs = end_time_dfs - start_time_dfs
print(f"Temps d'exécution pour DFS : {execution_time_dfs} secondes")

# Initialiser Pygame
pygame.init()

# Taille de chaque cellule dans le labyrinthe
CELL_SIZE = 50

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)  # Couleur gris pour les positions visitées

# Taille du labyrinthe
ROWS = 15
COLS = 15

# Exemple d'un labyrinthe plus grand
labyrinthe = [[1] * COLS for _ in range(ROWS)]

# Assurer qu'il y a un chemin du début à la sortie
labyrinthe[0][1] = 0  # Départ
labyrinthe[ROWS - 1][COLS - 2] = 0  # Sortie

# Fonction pour générer un labyrinthe avec une seule sortie
def generate_labyrinth():
    stack = []
    start_row, start_col = 1, 1
    labyrinthe[start_row][start_col] = 0
    stack.append((start_row, start_col))

    while stack:
        current_row, current_col = stack.pop()
        neighbors = [
            (current_row + 2, current_col),
            (current_row - 2, current_col),
            (current_row, current_col + 2),
            (current_row, current_col - 2),
        ]
        random.shuffle(neighbors)

        for neighbor_row, neighbor_col in neighbors:
            if 0 < neighbor_row < ROWS - 1 and 0 < neighbor_col < COLS - 1 and labyrinthe[neighbor_row][neighbor_col] == 1:
                labyrinthe[neighbor_row][neighbor_col] = 0
                labyrinthe[current_row + (neighbor_row - current_row) // 2][current_col + (neighbor_col - current_col) // 2] = 0
                stack.append((neighbor_row, neighbor_col))

generate_labyrinth()

# Position initiale de l'élément (bonhomme)
position_element = [1, 1]

# Positions visitées
visited_positions = set()

# Charger l'image du bonhomme
bonhomme_image = pygame.image.load('image1.jpeg')
bonhomme_image = pygame.transform.scale(bonhomme_image, (CELL_SIZE, CELL_SIZE))

# Charger l'image du gazon
gazon_image = pygame.image.load('image2.jpeg')  # Assurez-vous de mettre le chemin correct vers votre image de gazon
gazon_image = pygame.transform.scale(gazon_image, (CELL_SIZE, CELL_SIZE))

# Initialiser la fenêtre Pygame
width = COLS * CELL_SIZE
height = ROWS * CELL_SIZE
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conduire le bonhomme vers la sortie en 30s")

# Initialiser le temps de départ
start_time = pygame.time.get_ticks()

# Fonction pour dessiner le labyrinthe et le bonhomme
def draw_labyrinthe_and_bonhomme():
    for row in range(ROWS):
        for col in range(COLS):
            if labyrinthe[row][col] == 0:  # Chemin du labyrinthe
                window.blit(gazon_image, (col * CELL_SIZE, row * CELL_SIZE))
            else:  # Cases noires du labyrinthe
                pygame.draw.rect(window, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Dessiner les positions visitées en gris
    for pos in visited_positions:
        pygame.draw.rect(window, GRAY, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Dessiner le bonhomme à sa position actuelle
    window.blit(bonhomme_image, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE))

# Boucle principale
running = True
while running:
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000  # Convertir en secondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Gérer les touches du clavier pour déplacer le bonhomme
            if event.key == pygame.K_UP:
                new_row = position_element[0] - 1
                new_col = position_element[1]
            elif event.key == pygame.K_DOWN:
                new_row = position_element[0] + 1
                new_col = position_element[1]
            elif event.key == pygame.K_LEFT:
                new_row = position_element[0]
                new_col = position_element[1] - 1
            elif event.key == pygame.K_RIGHT:
                new_row = position_element[0]
                new_col = position_element[1] + 1

            # Vérifier les limites du labyrinthe et s'assurer que la nouvelle position est sur un chemin noir
            if (
                0 <= new_row < ROWS
                and 0 <= new_col < COLS
                and labyrinthe[new_row][new_col] == 0
                and (new_row != 0 or new_col != 1)  # Ne pas bloquer le départ
                and (new_row != ROWS - 1 or new_col != COLS - 1)  # Ne pas bloquer la sortie
            ):
                position_element = [new_row, new_col]
                visited_positions.add(tuple(position_element))

    # Vérifier si le bonhomme atteint la sortie
    if position_element == [ROWS - 1, COLS - 2]:
        # Afficher une nouvelle fenêtre avec des boutons
        pygame.quit()  # Fermer la fenêtre principale
        pygame.init()
        win_width = 400
        win_height = 400
        win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Félicitations!")

        # Ajouter un bouton "Continuer"
        continue_button_rect = pygame.Rect(win_width // 4, win_height // 2 - 60, win_width // 2, 50)
        continue_button_color = (0, 255, 0)
        pygame.draw.rect(win, continue_button_color, continue_button_rect)
        continue_font = pygame.font.SysFont(None, 24)
        continue_text = continue_font.render("Continuer", True, WHITE)
        continue_text_rect = continue_text.get_rect(center=continue_button_rect.center)
        win.blit(continue_text, continue_text_rect)

        # Ajouter un bouton "Recommencer"
        restart_button_rect = pygame.Rect(win_width // 4, win_height // 2 + 60, win_width // 2, 50)
        restart_button_color = (255, 0, 0)
        pygame.draw.rect(win, restart_button_color, restart_button_rect)
        restart_font = pygame.font.SysFont(None, 24)
        restart_text = restart_font.render("Recommencer", True, WHITE)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        win.blit(restart_text, restart_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if continue_button_rect.collidepoint(x, y):
                        # Code pour continuer le jeu
                        running = False
                    elif restart_button_rect.collidepoint(x, y):
                        # Code pour recommencer le jeu
                        running = False
                        start_time = pygame.time.get_ticks()
                        position_element = [1, 1]
                        visited_positions = set()
                        generate_labyrinth()
                        break

    # Vérifier si une minute est écoulée
    elif elapsed_time >= 30:
        pygame.quit()  # Fermer la fenêtre principale
        pygame.init()
        game_over_width = 600
        game_over_height = 600
        game_over_window = pygame.display.set_mode((game_over_width, game_over_height))
        pygame.display.set_caption("Game Over")

        # Ajouter un bouton "Recommencer"
        restart_button_rect = pygame.Rect(game_over_width // 4, game_over_height // 2, game_over_width // 2, 50)
        restart_button_color = (255, 0, 0)
        pygame.draw.rect(game_over_window, restart_button_color, restart_button_rect)
        restart_font = pygame.font.SysFont(None, 24)
        restart_text = restart_font.render("Recommencer", True, WHITE)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        game_over_window.blit(restart_text, restart_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if restart_button_rect.collidepoint(x, y):
                        # Code pour recommencer le jeu
                        running = False
                        start_time = pygame.time.get_ticks()
                        position_element = [1, 1]
                        visited_positions = set()
                        generate_labyrinth()
                        break

    # Effacer l'écran
    window.fill(WHITE)

    # Dessiner le labyrinthe et le bonhomme
    draw_labyrinthe_and_bonhomme()

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
