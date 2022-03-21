import pygame

pygame.init()

sc = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("Замечательная игра")

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.draw.rect(sc, WHITE, (10, 10, 580, 380), 3)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)
