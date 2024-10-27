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
ROWS = 20
COLS = 20

# Exemple d'un labyrinthe plus grand
labyrinthe = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

# Position initiale du parcours
position_parcours = [1, 1]

# Initialiser la fenêtre Pygame
width = COLS * CELL_SIZE
height = ROWS * CELL_SIZE
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Parcours du Labyrinthe")

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

    # Dessiner le labyrinthe
    draw_labyrinthe()

    # Mettre à jour la position du parcours
    pygame.draw.rect(window, RED, (position_parcours[1] * CELL_SIZE, position_parcours[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

    # Choisir une direction aléatoire pour le parcours
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random_direction = random.choice(directions)

    # Mettre à jour la position du parcours en fonction de la direction choisie
    new_row = position_parcours[0] + random_direction[0]
    new_col = position_parcours[1] + random_direction[1]

    # Vérifier les limites du labyrinthe et s'assurer que la nouvelle position est sur un chemin noir
    if 0 <= new_row < ROWS and 0 <= new_col < COLS and labyrinthe[new_row][new_col] == 1:
        position_parcours = [new_row, new_col]

    pygame.time.delay(100)  # Ajouter un délai pour rendre le parcours plus visible

# Quitter Pygame
pygame.quit()
sys.exit()
