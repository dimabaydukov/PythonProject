import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning English")

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 22)
sc_title = font.render('Hello! Nice to meet you here', True, WHITE)
pos_title = sc_title.get_rect(center=(WIDTH//2, 50))
sc.blit(sc_title, pos_title)

pygame.draw.rect(sc, WHITE, (10, 10, 580, 380), 3)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)
