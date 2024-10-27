import pygame
import sys
import random

# Mauvais il y a plusieurs sorties

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

# Assurer qu'il y a un seul chemin du début à la sortie en utilisant DFS
def generate_single_path_labyrinth():
    stack = [(1, 1)]
    visited = set([(1, 1)])

    while stack:
        current_row, current_col = stack[-1]

        neighbors = [
            (current_row + 2, current_col),
            (current_row - 2, current_col),
            (current_row, current_col + 2),
            (current_row, current_col - 2),
        ]
        random.shuffle(neighbors)

        found_unvisited_neighbor = False
        for neighbor_row, neighbor_col in neighbors:
            if (
                0 < neighbor_row < ROWS - 1
                and 0 < neighbor_col < COLS - 1
                and (neighbor_row, neighbor_col) not in visited
            ):
                labyrinthe[neighbor_row][neighbor_col] = 0
                labyrinthe[current_row + (neighbor_row - current_row) // 2][
                    current_col + (neighbor_col - current_col) // 2
                ] = 0
                stack.append((neighbor_row, neighbor_col))
                visited.add((neighbor_row, neighbor_col))
                found_unvisited_neighbor = True
                break

        if not found_unvisited_neighbor:
            stack.pop()

    # Sélectionner aléatoirement une sortie le long du chemin
    path_with_exit = random.choice(list(visited))
    labyrinthe[path_with_exit[0]][path_with_exit[1] + 1] = 0  # Sortie

generate_single_path_labyrinth()

# Position initiale de l'élément
position_element = [1, 1]

# Liste pour enregistrer les positions visitées par l'élément
positions_parcourues = []

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

            if (row, col) in positions_parcourues:
                pygame.draw.rect(window, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

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
                and not (new_row == ROWS - 1 and new_col == COLS - 2)  # Ne pas bloquer la sortie
            ):
                position_element = [new_row, new_col]
                positions_parcourues.append((new_row, new_col))

    # Dessiner le labyrinthe
    draw_labyrinthe()

    # Mettre à jour la position de l'élément
    pygame.draw.rect(window, RED, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
