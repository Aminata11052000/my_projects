
# import pygame
# import sys
# import random
# from collections import deque

# # Initialiser Pygame
# pygame.init()

# # Taille de chaque cellule dans le labyrinthe
# CELL_SIZE = 50

# # Couleurs
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (0, 0, 0)
# BLUE = (100, 100, 100)

# # Taille du labyrinthe
# ROWS = 15
# COLS = 15

# # Exemple d'un labyrinthe plus grand
# labyrinthe = [[1] * COLS for _ in range(ROWS)]

# # Assurer qu'il y a un chemin du début à la sortie
# labyrinthe[0][1] = 0  # Départ
# labyrinthe[ROWS - 1][COLS - 2] = 0  # Sortie

# # Fonction pour générer un labyrinthe avec une seule sortie en utilisant BFS
# def generate_labyrinth():
#     queue = deque()
#     start_row, start_col = 1, 1
#     labyrinthe[start_row][start_col] = 0
#     queue.append((start_row, start_col))

#     while queue:
#         current_row, current_col = queue.popleft()
#         neighbors = [
#             (current_row + 2, current_col),
#             (current_row - 2, current_col),
#             (current_row, current_col + 2),
#             (current_row, current_col - 2),
#         ]
#         random.shuffle(neighbors)

#         for neighbor_row, neighbor_col in neighbors:
#             if 0 < neighbor_row < ROWS - 1 and 0 < neighbor_col < COLS - 1 and labyrinthe[neighbor_row][neighbor_col] == 1:
#                 labyrinthe[neighbor_row][neighbor_col] = 0
#                 labyrinthe[current_row + (neighbor_row - current_row) // 2][current_col + (neighbor_col - current_col) // 2] = 0
#                 queue.append((neighbor_row, neighbor_col))

# generate_labyrinth()

# # Position initiale de l'élément
# position_element = [1, 1]

# # Positions visitées
# visited_positions = set()

# bonHomme_image = pygame.image.load('image1.jpeg')
# bonHomme_image = pygame.transform.scale(bonHomme_image, (CELL_SIZE, CELL_SIZE))

# gazon_image = pygame.image.load('image2.jpeg')
# gazon_image = pygame.transform.scale(gazon_image, (CELL_SIZE, CELL_SIZE))

# # Initialiser la fenêtre Pygame
# width = COLS * CELL_SIZE
# height = ROWS * CELL_SIZE
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Conduire l'élément vers la sortie")

# # Fonction pour dessiner le labyrinthe
# def draw_labyrinthe():
#     for row in range(ROWS):
#         for col in range(COLS):
#             color = WHITE 
#             if labyrinthe[row][col] == 0:
#                 window.blit(gazon_image, (col * CELL_SIZE, row * CELL_SIZE))
#             else:
#                 BLACK
#                 pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Dessiner les positions visitées en bleu
#     for pos in visited_positions:
#         pygame.draw.rect(window, BLUE, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
#     window.blit(bonHomme_image, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE))
#     pygame.display.flip()

# # Créer une police de caractères pour le message
# font = pygame.font.Font(None, 20)

# # Algorithme de Dijkstra pour trouver le chemin le plus court
# def dijkstra(start, end):
#     queue = deque()
#     queue.append(start)
#     visited = set()
#     parent = {}

#     while queue:
#         current = queue.popleft()
#         visited.add(current)

#         if current == end:
#             path = []
#             while current in parent:
#                 path.insert(0, current)
#                 current = parent[current]
#             return path

#         neighbors = [
#             (current[0] + 1, current[1]),
#             (current[0] - 1, current[1]),
#             (current[0], current[1] + 1),
#             (current[0], current[1] - 1),
#         ]

#         for neighbor in neighbors:
#             if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and labyrinthe[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
#                 queue.append(neighbor)
#                 parent[neighbor] = current

# # Trouver le chemin le plus court
# start_position = (1, 1)
# end_position = (ROWS - 1, COLS - 2)
# shortest_path = dijkstra(start_position, end_position)

# # Créer une copie du chemin le plus court
# shortest_path_copy = shortest_path.copy()

# # Boucle principale
# running = True
# exit_reached = False  # Variable pour suivre si la sortie est atteinte
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             # Gérer les touches du clavier pour déplacer l'élément
#             if event.key == pygame.K_UP:
#                 new_row = position_element[0] - 1
#                 new_col = position_element[1]
#             elif event.key == pygame.K_DOWN:
#                 new_row = position_element[0] + 1
#                 new_col = position_element[1]
#             elif event.key == pygame.K_LEFT:
#                 new_row = position_element[0]
#                 new_col = position_element[1] - 1
#             elif event.key == pygame.K_RIGHT:
#                 new_row = position_element[0]
#                 new_col = position_element[1] + 1

#             # Vérifier les limites du labyrinthe et s'assurer que la nouvelle position est sur un chemin noir
#             if (
#                 0 <= new_row < ROWS
#                 and 0 <= new_col < COLS
#                 and labyrinthe[new_row][new_col] == 0
#                 and (new_row != 0 or new_col != 1)  # Ne pas bloquer le départ
#                 and (new_row != ROWS - 1 or new_col != COLS - 1)  # Ne pas bloquer la sortie 
#             ):
#                 position_element = [new_row, new_col]
#                 visited_positions.add(tuple(position_element))

#                 # Vérifier si la sortie est atteinte
#                 if position_element == [ROWS - 1, COLS - 2]:
#                     exit_reached = True

#     # À la fin de la boucle principale, vérifiez si la sortie est atteinte et affichez une fenêtre de message appropriée
#     if exit_reached:
#         # Créer une nouvelle fenêtre pour le message
#         message_window = pygame.display.set_mode((400, 400))
#         message_window.fill(WHITE)  # Remplir la fenêtre avec la couleur blanche

#         # Rendre le texte de félicitations
#         text = font.render("Félicitations ! Vous avez atteint la sortie du labyrinthe !", True, BLACK)
#         text_rect = text.get_rect(center=(200, 200))  # Centrer le texte dans la fenêtre

#         # Afficher le texte dans la fenêtre
#         message_window.blit(text, text_rect)
#         pygame.display.flip()

#         pygame.time.delay(4000)  # Attendre 2 secondes avant de fermer la fenêtre
#         pygame.quit()
#         sys.exit()

#     # Effacer l'écran
#     window.fill(WHITE)

#     # Dessiner le labyrinthe
#     draw_labyrinthe()

#     # Mettre à jour la position de l'élément
#     pygame.draw.rect(window, RED, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Dessiner le chemin le plus court en vert
#     for path_position in shortest_path_copy:
#         pygame.draw.rect(window, (100, 100, 200), (path_position[1] * CELL_SIZE, path_position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     pygame.display.flip()

# # Quitter Pygame
# pygame.quit()
# sys.exit()


import pygame
import sys
import random
from collections import deque

# Initialiser Pygame
pygame.init()

# Taille de chaque cellule dans le labyrinthe
CELL_SIZE = 40

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (100, 100, 100)

# Taille du labyrinthe
ROWS = 15
COLS = 15

# Exemple d'un labyrinthe plus grand
labyrinthe = [[1] * COLS for _ in range(ROWS)]

# Assurer qu'il y a un chemin du début à la sortie
labyrinthe[0][1] = 0  # Départ
labyrinthe[ROWS - 1][COLS - 2] = 0  # Sortie

# Fonction pour générer un labyrinthe avec une seule sortie en utilisant BFS
def generate_labyrinth():
    queue = deque()
    start_row, start_col = 1, 1
    labyrinthe[start_row][start_col] = 0
    queue.append((start_row, start_col))

    while queue:
        current_row, current_col = queue.popleft()
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
                queue.append((neighbor_row, neighbor_col))

generate_labyrinth()

# Position initiale de l'élément
position_element = [1, 1]

# Positions visitées
visited_positions = set()

bonHomme_image = pygame.image.load('image1.jpeg')
bonHomme_image = pygame.transform.scale(bonHomme_image, (CELL_SIZE, CELL_SIZE))

gazon_image = pygame.image.load('image2.jpeg')
gazon_image = pygame.transform.scale(gazon_image, (CELL_SIZE, CELL_SIZE))

# Initialiser la fenêtre Pygame
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conduire l'élément vers la sortie")

# Créer une police de caractères pour le message
font = pygame.font.Font(None, 20)

# Durée maximale du jeu (1 minute = 60000 millisecondes)
MAX_GAME_TIME = 30000
start_time = pygame.time.get_ticks()  # Enregistrer le temps de début du jeu

# Variable pour contrôler l'affichage de la fenêtre de message de sortie atteinte
show_exit_message = False

# Variable pour contrôler l'affichage de la fenêtre de message de recommencement
show_reset_message = False

# Boucle principale
running = True
exit_reached = False  # Variable pour suivre si la sortie est atteinte
while running:
    current_time = pygame.time.get_ticks()  # Obtenir le temps actuel du jeu
    game_time = current_time - start_time  # Calculer le temps écoulé

    if game_time >= MAX_GAME_TIME:
        if not show_reset_message:
            # Créer une nouvelle fenêtre pour le message de réinitialisation
            reset_message_window = pygame.display.set_mode((400, 400))
            reset_message_window.fill(WHITE)  # Remplir la fenêtre avec la couleur blanche

            # Dessiner le bouton de recommencement
            reset_button_rect = pygame.Rect(150, 300, 100, 50)
            pygame.draw.rect(reset_message_window, RED, reset_button_rect)
            reset_button_text = font.render("Recommencer", True, WHITE)
            reset_message_window.blit(reset_button_text, reset_button_text.get_rect(center=reset_button_rect.center))
            pygame.display.flip()

            show_reset_message = True

        # Gérer les événements de la fenêtre de message de recommencement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button_rect.collidepoint(event.pos):
                    # Réinitialiser le jeu
                    generate_labyrinth()
                    position_element = [1, 1]
                    visited_positions.clear()
                    start_time = pygame.time.get_ticks()  # Réinitialiser le temps de début
                    # Réinitialiser la taille de la fenêtre du labyrinthe
                    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    show_reset_message = False  # Cacher la fenêtre de message de recommencement

    else:
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

                    # Vérifier si la sortie est atteinte
                    if position_element == [ROWS - 1, COLS - 2]:
                        exit_reached = True

        # À la fin de la boucle principale, vérifie si la sortie est atteinte et affiche une fenêtre de message appropriée
        if exit_reached:
            if not show_exit_message:
                # Créer une nouvelle fenêtre pour le message
                message_window = pygame.display.set_mode((400, 400))
                message_window.fill(WHITE)  # Remplir la fenêtre avec la couleur blanche

                # Rendre le texte de félicitations
                text = font.render("Félicitations ! Vous avez atteint la sortie du labyrinthe !", True, BLACK)
                text_rect = text.get_rect(center=(200, 200))  # Centrer le texte dans la fenêtre

                # Afficher le texte dans la fenêtre
                message_window.blit(text, text_rect)

                pygame.display.flip()

                show_exit_message = True

        else:
            # Effacer l'écran
            window.fill(WHITE)

            # Dessiner le labyrinthe
            for row in range(ROWS):
                for col in range(COLS):
                    color = WHITE 
                    if labyrinthe[row][col] == 0:
                        window.blit(gazon_image, (col * CELL_SIZE, row * CELL_SIZE))
                    else:
                        pygame.draw.rect(window, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Dessiner les positions visitées en bleu
            for pos in visited_positions:
                pygame.draw.rect(window, BLUE, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            window.blit(bonHomme_image, (position_element[1] * CELL_SIZE, position_element[0] * CELL_SIZE))
            pygame.display.flip()

pygame.quit()
sys.exit()
