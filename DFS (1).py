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
BLUE = (0, 0, 255)

# Taille du labyrinthe
ROWS = 15
COLS = 15

# Exemple d'un labyrinthe plus grand
labyrinthe = [[1] * COLS for _ in range(ROWS)]

# Assurer qu'il y a un chemin du début à la sortie
labyrinthe[0][1] = 0  # Départ
labyrinthe[ROWS - 1][COLS - 2] = 2  # Sortie

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

# Fonction pour dessiner le labyrinthe
def draw_labyrinthe():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if labyrinthe[row][col] == 0 else BLACK
            pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Dessiner les positions visitées en bleu
    for pos in visited_positions:
        pygame.draw.rect(window, BLUE, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Fonction pour effectuer le parcours en profondeur
def parcours_en_profondeur(row, col):
    if (row, col) == (ROWS - 1, COLS - 2):  # Si la position actuelle est la sortie
        visited_positions.add((row, col))  # Ajoute la sortie aux positions visitées
        pygame.time.delay(100)
        draw_labyrinthe()
        pygame.display.flip()
        return True

    if 0 <= row < ROWS and 0 <= col < COLS and labyrinthe[row][col] == 0 and (row, col) not in visited_positions:
        visited_positions.add((row, col))
        pygame.time.delay(100)  # Pause pour visualiser le parcours
        draw_labyrinthe()
        pygame.display.flip()

        # Essayer de se déplacer dans toutes les directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if parcours_en_profondeur(row + dr, col + dc):
                return True

        visited_positions.remove((row, col))  # Backtrack
        return False

# Initialiser la fenêtre Pygame
width = COLS * CELL_SIZE
height = ROWS * CELL_SIZE
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conduire l'élément vers la sortie")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effectuer le parcours en profondeur à partir de la position actuelle
    parcours_en_profondeur(position_element[0], position_element[1])

# Quitter Pygame
pygame.quit()
sys.exit()

# other method with user's direction
# import pygame
# import sys
# import random

# # Initialiser Pygame
# pygame.init()

# # Taille de chaque cellule dans le labyrinthe
# CELL_SIZE = 25

# # Couleurs
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# # Taille du labyrinthe
# ROWS = 15
# COLS = 15

# # Charger une image pour représenter le bonhomme
# bonhomme_image = pygame.image.load("image1.jpeg")
# bonhomme_image = pygame.transform.scale(bonhomme_image, (CELL_SIZE, CELL_SIZE))

# # Exemple d'un labyrinthe plus grand
# labyrinthe = [[1] * COLS for _ in range(ROWS)]

# # Assurer qu'il y a un seul chemin du début à la sortie en utilisant DFS
# def generate_single_path_labyrinth():
#     stack = [(1, 1)]
#     visited = set([(1, 1)])

#     while stack:
#         current_row, current_col = stack[-1]

#         neighbors = [
#             (current_row + 2, current_col),
#             (current_row - 2, current_col),
#             (current_row, current_col + 2),
#             (current_row, current_col - 2),
#         ]
#         random.shuffle(neighbors)

#         found_unvisited_neighbor = False
#         for neighbor_row, neighbor_col in neighbors:
#             if (
#                 0 < neighbor_row < ROWS - 1
#                 and 0 < neighbor_col < COLS - 1
#                 and (neighbor_row, neighbor_col) not in visited
#             ):
#                 labyrinthe[neighbor_row][neighbor_col] = 0
#                 labyrinthe[current_row + (neighbor_row - current_row) // 2][
#                     current_col + (neighbor_col - current_col) // 2
#                 ] = 0
#                 stack.append((neighbor_row, neighbor_col))
#                 visited.add((neighbor_row, neighbor_col))
#                 found_unvisited_neighbor = True
#                 break

#         if not found_unvisited_neighbor:
#             stack.pop()

#     # Sélectionner aléatoirement une sortie le long du chemin
#     path_with_exit = random.choice(list(visited))
#     labyrinthe[path_with_exit[0]][path_with_exit[1] + 1] = 0  # Sortie

# generate_single_path_labyrinth()

# # Position initiale du bonhomme
# position_bonhomme = [1, 1]

# # Liste pour enregistrer les positions visitées par le bonhomme
# positions_parcourues = []

# # Variable pour indiquer si le bonhomme a atteint la sortie
# bonhomme_atteint_sortie = False

# # Initialiser la fenêtre Pygame
# width = COLS * CELL_SIZE
# height = ROWS * CELL_SIZE
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Conduire le bonhomme vers la sortie")

# # Fonction pour dessiner le labyrinthe
# def draw_labyrinthe():
#     for row in range(ROWS):
#         for col in range(COLS):
#             color = WHITE if labyrinthe[row][col] == 0 else BLACK
#             pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#             if (row, col) in positions_parcourues:
#                 pygame.draw.rect(window, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Afficher l'image du bonhomme à la position actuelle
#     window.blit(bonhomme_image, (position_bonhomme[1] * CELL_SIZE, position_bonhomme[0] * CELL_SIZE))

# # Fonction pour afficher la fenêtre contextuelle
# def show_prompt():
#     font = pygame.font.SysFont(None, 55)
#     text = font.render("Vous avez atteint la sortie !", True, RED)
#     window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
#     pygame.display.flip()

# # Boucle principale
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             # Gérer les touches du clavier pour déplacer le bonhomme
#             if event.key == pygame.K_UP:
#                 new_row = position_bonhomme[0] - 1
#                 new_col = position_bonhomme[1]
#             elif event.key == pygame.K_DOWN:
#                 new_row = position_bonhomme[0] + 1
#                 new_col = position_bonhomme[1]
#             elif event.key == pygame.K_LEFT:
#                 new_row = position_bonhomme[0]
#                 new_col = position_bonhomme[1] - 1
#             elif event.key == pygame.K_RIGHT:
#                 new_row = position_bonhomme[0]
#                 new_col = position_bonhomme[1] + 1

#             # Vérifier les limites du labyrinthe et s'assurer que la nouvelle position est sur un chemin noir
#             if (
#                 0 <= new_row < ROWS
#                 and 0 <= new_col < COLS
#                 and labyrinthe[new_row][new_col] == 0
#                 and not (new_row == ROWS - 1 and new_col == COLS - 2)  # Ne pas bloquer la sortie
#             ):
#                 position_bonhomme = [new_row, new_col]
#                 positions_parcourues.append((new_row, new_col))

#                 # Vérifier si le bonhomme atteint la sortie
#                 if new_row == ROWS - 1 and new_col == COLS - 2:
#                     bonhomme_atteint_sortie = True

#     # Dessiner le labyrinthe
#     draw_labyrinthe()

#     # Mettre à jour la position du bonhomme
#     pygame.display.flip()

#     # Vérifier si le bonhomme a atteint la sortie après la mise à jour de l'écran
#     if bonhomme_atteint_sortie:
#         show_prompt()
#         pygame.time.delay(2000)  # Attendre 2000 millisecondes (2 secondes)
#         running = False  # Terminer la boucle principale

# # Quitter Pygame
# pygame.quit()
# sys.exit()