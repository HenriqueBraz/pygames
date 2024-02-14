import pygame
import sys

pygame.init()

# Definindo algumas cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Configurações da janela
WIDTH, HEIGHT = 800, 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Resgate Princesa Isthar")

# Carregando a imagem original
original_background_image = pygame.image.load("images/images.jpeg")
background_image = pygame.transform.scale(original_background_image, (780, 480))

# Adicionando uma borda à imagem
border_size = 10
bordered_width = WIDTH + 2 * border_size
bordered_height = HEIGHT + 2 * border_size

# Criando uma nova superfície com a borda
bordered_surface = pygame.Surface((bordered_width, bordered_height))
bordered_surface.fill(GRAY)  # Preenchendo a superfície com a cor

# Desenhando a imagem original no centro da superfície com a borda
bordered_surface.blit(background_image, (border_size, border_size))

# Função para desenhar texto na tela
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Loop principal do jogo
def game_loop():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenhando a superfície com a borda
        screen.blit(bordered_surface, (0, 0))

        # Desenhando texto na tela
        font = pygame.font.Font(None, 30)
        draw_text("O que voce faz? Digite uma opção (0 para sair):", font, BLACK, screen, 200, 500)

        draw_text("1: Bláaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", font, BLACK, screen, 10, 528)
        draw_text("2: Poft", font, BLACK, screen, 10, 548)
        draw_text("3: Crash", font, BLACK, screen, 10, 568)
        draw_text("4: Run", font, BLACK, screen, 10, 588)

        # Exibindo na tela
        pygame.display.flip()
        # Agora, você pode adicionar uma lógica para detectar a escolha do jogador
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Jogador escolheu a opção 1")
                    # Adicione lógica adicional para a opção 1, se necessário
                elif event.key == pygame.K_2:
                    print("Jogador escolheu a opção 2")
                    # Adicione lógica adicional para a opção 2, se necessário
                # Adicione outras verificações de tecla conforme necessário
                elif event.key == pygame.K_0:
                    print("Jogador escolheu a opção 0. O jogo será encerrado.")
                    pygame.quit()
                    sys.exit()

        # Definindo a taxa de atualização da tela
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
