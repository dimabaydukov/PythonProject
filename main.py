from button import Button
import pygame

pygame.mixer.pre_init(20000, -16, 2, 512)
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

# музыка главного меню
pygame.mixer.music.load("Music/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

# звук клика по кнопке
click = pygame.mixer.Sound("Music/click.ogg")
click.set_volume(0.25)

# заголовок
title_font = pygame.font.Font("Fonts/main.ttf", 28)

# подзаголовок
small_title_font = pygame.font.Font("Fonts/main.ttf", 22)


# главное меню
def main_menu():
    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    title_surface = title_font.render("Hello! Welcome to this wonderful game", True, BLACK)
    title_position = title_surface.get_rect(center=(WIDTH // 2, 75))

    main_surface.blit(title_surface, title_position)

    small_title_surface1 = small_title_font.render("Here you can improve your English skills", True, BLACK)
    small_title_position1 = small_title_surface1.get_rect(center=(WIDTH // 2, 125))

    small_title_surface2 = small_title_font.render("by completing various interesting levels", True, BLACK)
    small_title_position2 = small_title_surface2.get_rect(center=(WIDTH // 2, 145))

    main_surface.blit(small_title_surface1, small_title_position1)
    main_surface.blit(small_title_surface2, small_title_position2)

    button_font_main = pygame.font.Font("Fonts/main.ttf", 24)

    play_button = Button("Play", 200, 50, (WIDTH // 2 - 100, HEIGHT // 2 - 25), BLUE, DARK_BLUE, button_font_main,
                         WHITE, DARK_BLUE, 5)
    play_button.draw(main_surface)
    exit_button = Button("Exit", 200, 50, (WIDTH // 2 - 100, HEIGHT // 2 + 50), BLUE, DARK_BLUE, button_font_main,
                         WHITE, DARK_BLUE, 5)
    exit_button.draw(main_surface)

    play_pressed = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if play_button.pressed:
                    click.play()
                    play_pressed = True
                    levels()
                    running = False
                elif exit_button.pressed:
                    click.play()
                    pygame.time.delay(500)
                    exit()
            elif not play_pressed:
                play_button.check_click()
                play_button.draw(main_surface)
                exit_button.check_click()
                exit_button.draw(main_surface)
        pygame.display.update()
        clock.tick(FPS)


# экран с выбором уровня
def levels():
    running = True

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    level_text_surface = small_title_font.render("Choose your level", True, BLACK)
    level_text_position = level_text_surface.get_rect(center=(WIDTH // 2, 75))
    main_surface.blit(level_text_surface, level_text_position)

    image_font = pygame.font.Font("Fonts/main.ttf", 14)

    animals = pygame.image.load("Images/animals.jpg").convert()
    animals_text = image_font.render("Animals", True, BLACK)
    main_surface.blit(animals_text, (140, 100))
    animals_rect = animals.get_rect(topleft=(140, 120))
    animals_hover = pygame.image.load("Images/animals_hover.jpg").convert()

    food = pygame.image.load("Images/food.jpg").convert()
    food_text = image_font.render("Food", True, BLACK)
    main_surface.blit(food_text, (140, 300))
    food_rect = food.get_rect(topleft=(140, 320))
    food_hover = pygame.image.load("Images/food_hover.jpg").convert()

    sights = pygame.image.load("Images/sights.jpg").convert()
    sights_text = image_font.render("Sights", True, BLACK)
    main_surface.blit(sights_text, (WIDTH - 320, 100))
    sights_rect = sights.get_rect(topleft=(WIDTH - 320, 120))
    sights_hover = pygame.image.load("Images/sights_hover.jpg").convert()

    it = pygame.image.load("Images/it.jpg").convert()
    it_text = image_font.render("IT", True, BLACK)
    main_surface.blit(it_text, (WIDTH - 320, 300))
    it_rect = it.get_rect(topleft=(WIDTH - 320, 320))
    it_hover = pygame.image.load("Images/it_hover.jpg").convert()

    back_arrow = pygame.image.load("Images/back.png").convert_alpha()
    arrow_position = back_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    back_arrow_hover = pygame.image.load("Images/back_hover.png").convert_alpha()

    while running:
        main_surface.blit(animals, (140, 120))
        main_surface.blit(food, (140, 320))
        main_surface.blit(sights, (WIDTH - 320, 120))
        main_surface.blit(it, (WIDTH - 320, 320))

        main_surface.blit(back_arrow, arrow_position)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if arrow_position.collidepoint(mouse_pos):
            main_surface.blit(back_arrow_hover, arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                main_menu()
                running = False
        elif animals_rect.collidepoint(mouse_pos):
            main_surface.blit(animals_hover, (140, 120))
            if pygame.mouse.get_pressed()[0]:
                click.play()
                animals_def()
                running = False
        elif food_rect.collidepoint(mouse_pos):
            main_surface.blit(food_hover, (140, 320))
            if pygame.mouse.get_pressed()[0]:
                click.play()
                food_def()
                running = False
        elif sights_rect.collidepoint(mouse_pos):
            main_surface.blit(sights_hover, (WIDTH - 320, 120))
            if pygame.mouse.get_pressed()[0]:
                click.play()
                sights_def()
                running = False
        elif it_rect.collidepoint(mouse_pos):
            main_surface.blit(it_hover, (WIDTH - 320, 320))
            if pygame.mouse.get_pressed()[0]:
                click.play()
                it_def()
                running = False

        pygame.display.update()
        clock.tick(FPS)


def animals_def():
    pass


def food_def():
    pass


def sights_def():
    pass


def it_def():
    pass


main_menu()
