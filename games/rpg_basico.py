import pygame

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela do jogo
screen = pygame.display.set_mode((800, 600))

# Define o título da janela do jogo
pygame.display.set_caption("RPG básico com Pygame")

# Carrega a imagem do personagem
player_image = pygame.image.load("player.png")

# Define a posição inicial do personagem
player_x = 400
player_y = 300

# Define a velocidade de movimento do personagem
player_speed = 1

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)

# Define a fonte para mostrar o HP do personagem
font = pygame.font.Font(None, 30)

# Define o HP inicial do personagem
player_hp = 100

# Cria um loop principal para o jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtém as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Move o personagem de acordo com as teclas pressionadas
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Atualiza a tela
    screen.fill(white)
    screen.blit(player_image, (player_x, player_y))

    # Mostra o HP do personagem
    player_hp_text = font.render("HP: " + str(player_hp), True, black)
    screen.blit(player_hp_text, (650, 550))

    pygame.display.update()

# Encerra o pygame
pygame.quit()