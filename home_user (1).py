import pygame
import sys
import random

# Initialiser Pygame
pygame.init()

# Taille de chaque cellule dans le labyrinthe
CELL_SIZE = 25

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Taille du labyrinthe
ROWS = 15
COLS = 15

# Exemple d'un labyrinthe plus grand
labyrinthe = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

# Assurer qu'il y a un chemin du début à la sortie
labyrinthe[0][1] = 0  # Départ
labyrinthe[ROWS - 1][COLS - 2] = 0  # Sortie

# Fonction pour générer un labyrinthe connecté
def generate_connected_labyrinth():
    while not is_labyrinth_connected():
        labyrinthe[random.randint(0, ROWS - 1)][random.randint(0, COLS - 1)] = 0

def is_labyrinth_connected():
    visited = set()

    def dfs(row, col):
        if (row, col) not in visited:
            visited.add((row, col))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and labyrinthe[new_row][new_col] == 0:
                    dfs(new_row, new_col)

    dfs(0, 1)  # Départ
    return (ROWS - 1, COLS - 2) in visited  # Sortie

generate_connected_labyrinth()

# Position initiale de l'élément
position_element = [1, 1]

# Initialiser la fenêtre Pygame
width = COLS * CELL_SIZE
height = ROWS * CELL_SIZE
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conduire l'élément vers la sortie")

# Fonction pour dessiner le labyrinthe
def draw_labyrinthe():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if labyrinthe[row][col] == 0 else BLACK
            pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Gérer les touches du clavier pour déplacer l'élément
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
                and (new_row != ROWS - 1 or new_col != COLS - 2)  # Ne pas bloquer la sortie
            ):
                position_element = [new_row, new_col]

    # Dessiner le labyrinthe
    draw_labyrinthe()

    # Mettre à jour la position de l'élément
    pygame.draw.rect(window, RED, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
