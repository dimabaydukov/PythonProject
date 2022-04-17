from button import Button

# инициализация библиотеки PyGame и звуковых эффектов в ней
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# параметры окна
WIDTH = 800
HEIGHT = 600

# создание окна, изменение названия и иконки приложения
main_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning English")
pygame.display.set_icon(pygame.image.load("Images/icon.bmp"))

# количество кадров в секунду
clock = pygame.time.Clock()
FPS = 60

# инициализация цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (31, 117, 254)
DARK_BLUE = (4, 41, 131)

# задний фон
background_surface = pygame.image.load("Images/background.png").convert()
main_surface.blit(background_surface, (0, 0))

# музыка главного меню
pygame.mixer.music.load("Music/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

# заголовок
title_font = pygame.font.Font("Fonts/main.ttf", 28)
title_surface = title_font.render("Hello! Welcome to this wonderful game", True, BLACK)
title_position = title_surface.get_rect(center=(WIDTH//2, 75))
main_surface.blit(title_surface, title_position)

# подзаголовок
small_title_font = pygame.font.Font("Fonts/main.ttf", 22)
small_title_surface1 = small_title_font.render("Here you can improve your English skills", True, BLACK)
small_title_position1 = small_title_surface1.get_rect(center=(WIDTH//2, 125))
small_title_surface2 = small_title_font.render("by completing various interesting levels", True, BLACK)
small_title_position2 = small_title_surface2.get_rect(center=(WIDTH//2, 145))
main_surface.blit(small_title_surface1, small_title_position1)
main_surface.blit(small_title_surface2, small_title_position2)

# шрифт для кнопок в главном меню
button_font_main = pygame.font.Font("Fonts/main.ttf", 24)

# создание кнопок
play_button = Button("Play", 200, 50, (WIDTH//2 - 100, HEIGHT//2 - 25), BLUE, DARK_BLUE, button_font_main,
                     WHITE, DARK_BLUE, 5)
play_button.draw(main_surface)
exit_button = Button("Exit", 200, 50, (WIDTH//2 - 100, HEIGHT//2 + 50), BLUE, DARK_BLUE, button_font_main,
                     WHITE, DARK_BLUE, 5)
exit_button.draw(main_surface)

pygame.display.update()

# игровой круг
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    play_button.check_click()
    play_button.draw(main_surface)
    exit_button.check_click()
    exit_button.draw(main_surface)
    pygame.display.update()
    clock.tick(FPS)
