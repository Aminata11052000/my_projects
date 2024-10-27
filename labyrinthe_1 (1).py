import pygame
import sys
import random


# Bon mais utilise le DFS


# Initialiser Pygame
pygame.init()

# Taille de chaque cellule dans le labyrinthe
CELL_SIZE = 25

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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

# Position initiale de l'élément
position_element = [1, 1]

# Positions visitées
visited_positions = set()

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

    # Dessiner les positions visitées en bleu
    for pos in visited_positions:
        pygame.draw.rect(window, BLUE, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

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
                and (new_row != ROWS - 1 or new_col != COLS - 1)  # Ne pas bloquer la sortie 
            ):
                position_element = [new_row, new_col]
                visited_positions.add(tuple(position_element))

    # Dessiner le labyrinthe
    draw_labyrinthe()

    # Mettre à jour la position de l'élément
    pygame.draw.rect(window, RED, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
