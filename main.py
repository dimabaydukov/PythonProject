from button import Button
import pygame

# параметры звуковых эффектов
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

# звуки
click = pygame.mixer.Sound("Music/click.ogg")
click.set_volume(0.25)
true = pygame.mixer.Sound("Music/true.mp3")
true.set_volume(0.25)
false = pygame.mixer.Sound("Music/false.mp3")
false.set_volume(0.25)

# шрифты
title_font = pygame.font.Font("Fonts/main.ttf", 28)
small_title_font = pygame.font.Font("Fonts/main.ttf", 22)
button_font_main = pygame.font.Font("Fonts/main.ttf", 24)


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
            elif event.type == pygame.MOUSEBUTTONUP:
                if animals_rect.collidepoint(mouse_pos):
                    click.play()
                    running = False
                    animals_def()
                if food_rect.collidepoint(mouse_pos):
                    click.play()
                    running = False
                    food_def()
                if sights_rect.collidepoint(mouse_pos):
                    click.play()
                    sights_def()
                    running = False
                if it_rect.collidepoint(mouse_pos):
                    click.play()
                    it_def()
                    running = False
        if animals_rect.collidepoint(mouse_pos):
            main_surface.blit(animals_hover, (140, 120))
        elif food_rect.collidepoint(mouse_pos):
            main_surface.blit(food_hover, (140, 320))
        elif sights_rect.collidepoint(mouse_pos):
            main_surface.blit(sights_hover, (WIDTH - 320, 120))
        elif it_rect.collidepoint(mouse_pos):
            main_surface.blit(it_hover, (WIDTH - 320, 320))

        if arrow_position.collidepoint(mouse_pos):
            main_surface.blit(back_arrow_hover, arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                main_menu()
                running = False

        pygame.display.update()
        clock.tick(FPS)


def animals_def():
    running = True

    score = 0

    score1 = game("Images/Animals/1.jpg", "Anteater", "Antelope", "Agouti", "Aardvark", "Anteater", score, "1/5")
    score2 = game("Images/Animals/2.jpg", "Bear", "Bongo", "Boar", "Bonobo", "Boar", score1, "2/5")
    score3 = game("Images/Animals/3.jpg", "Caribou", "Cheetah", "Clam", "Cattle", "Cheetah", score2, "3/5")
    score4 = game("Images/Animals/4.jpg", "Ferret", "Finch", "Fox", "Falcon", "Ferret", score3, "4/5")
    score5 = game("Images/Animals/5.jpg", "Hawk", "Hedgehog", "Hare", "Heron", "Hedgehog", score4, "5/5")

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    score_text_surface = title_font.render("Your score: ", True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    main_surface.blit(score_text_surface, score_text_position)

    score_text_surface = title_font.render(str(score5), True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    main_surface.blit(score_text_surface, score_text_position)

    next_arrow = pygame.image.load("Images/next.png").convert_alpha()
    next_arrow_position = next_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    next_arrow_hover = pygame.image.load("Images/next_hover.png").convert_alpha()

    while running:
        main_surface.blit(next_arrow, next_arrow_position)

        mouse_pos = pygame.mouse.get_pos()

        if next_arrow_position.collidepoint(mouse_pos):
            main_surface.blit(next_arrow_hover, next_arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                levels()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(FPS)


def food_def():
    running = True

    score = 0

    score1 = game("Images/Food/1.png", "Cookie", "Pie", "Candy", "Cake", "Cake", score, "1/5")
    score2 = game("Images/Food/2.png", "Egg", "Butter", "Cheese", "Yogurt", "Cheese", score1, "2/5")
    score3 = game("Images/Food/3.png", "Hot dog", "Hamburger", "Bread", "Pizza", "Hamburger", score2, "3/5")
    score4 = game("Images/Food/4.png", "Roast chicken", "Fish", "Seafood", "Steak", "Steak", score3, "4/5")
    score5 = game("Images/Food/5.png", "Ham", "Salad", "Bacon", "Sour cream", "Salad", score4, "5/5")

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    score_text_surface = title_font.render("Your score: ", True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    main_surface.blit(score_text_surface, score_text_position)

    score_text_surface = title_font.render(str(score5), True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    main_surface.blit(score_text_surface, score_text_position)

    next_arrow = pygame.image.load("Images/next.png").convert_alpha()
    next_arrow_position = next_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    next_arrow_hover = pygame.image.load("Images/next_hover.png").convert_alpha()

    while running:
        main_surface.blit(next_arrow, next_arrow_position)

        mouse_pos = pygame.mouse.get_pos()

        if next_arrow_position.collidepoint(mouse_pos):
            main_surface.blit(next_arrow_hover, next_arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                levels()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(FPS)


def sights_def():
    running = True

    score = 0

    score1 = game("Images/Sights/1.jpg", "Tower of London", "Westminster Abbey", "Kew Gardens", "St Paul's Cathedral",
                  "Westminster Abbey", score, "1/5")
    score2 = game("Images/Sights/2.jpg", "Chester Zoo", "Boat Cruises", "Flamingo Park", "Stonehenge", "Stonehenge",
                  score1, "2/5")
    score3 = game("Images/Sights/3.jpg", "York Minster", "Windsor Castle", "Canterbury Cathedral", "The Cotswold's",
                  "Windsor Castle", score2, "3/5")
    score4 = game("Images/Sights/4.jpg", "The National Gallery", "Tate Modern", "Warwick Castle", "Royal Museums ",
                  "The National Gallery", score3, "4/5")
    score5 = game("Images/Sights/5.jpg", "Roman Baths", "Blackpool Pleasure", "Eden Project", "The Lake District",
                  "Eden Project", score4, "5/5")

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    score_text_surface = title_font.render("Your score: ", True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    main_surface.blit(score_text_surface, score_text_position)

    score_text_surface = title_font.render(str(score5), True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    main_surface.blit(score_text_surface, score_text_position)

    next_arrow = pygame.image.load("Images/next.png").convert_alpha()
    next_arrow_position = next_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    next_arrow_hover = pygame.image.load("Images/next_hover.png").convert_alpha()

    while running:
        main_surface.blit(next_arrow, next_arrow_position)

        mouse_pos = pygame.mouse.get_pos()

        if next_arrow_position.collidepoint(mouse_pos):
            main_surface.blit(next_arrow_hover, next_arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                levels()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(FPS)


def it_def():
    running = True

    score = 0

    score1 = game("Images/IT/1.png", "Processor", "Power Supply", "Monitor", "Keyboard", "Processor", score, "1/5")
    score2 = game("Images/IT/2.jpg", "Memory", "Hard Drive", "Video card", "Motherboard", "Video card", score1, "2/5")
    score3 = game("Images/IT/3.jpg", "USB Port", "HDMI Port", "AUX", "Ethernet", "HDMI Port", score2, "3/5")
    score4 = game("Images/IT/4.jpg", "SSD", "Mouse", "Gamepad", "Optical Drive", "SSD", score3, "4/5")
    score5 = game("Images/IT/5.jpg", "Printer", "Webcam", "Microphone", "Sound card", "Webcam", score4, "5/5")

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    score_text_surface = title_font.render("Your score: ", True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    main_surface.blit(score_text_surface, score_text_position)

    score_text_surface = title_font.render(str(score5), True, BLACK)
    score_text_position = score_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    main_surface.blit(score_text_surface, score_text_position)

    next_arrow = pygame.image.load("Images/next.png").convert_alpha()
    next_arrow_position = next_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    next_arrow_hover = pygame.image.load("Images/next_hover.png").convert_alpha()

    while running:
        main_surface.blit(next_arrow, next_arrow_position)

        mouse_pos = pygame.mouse.get_pos()

        if next_arrow_position.collidepoint(mouse_pos):
            main_surface.blit(next_arrow_hover, next_arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                levels()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(FPS)


def game(picture_path, answer1, answer2, answer3, answer4, correct_answer, score, number):
    running = True

    correct_button = None

    main_surface.fill(WHITE)
    main_surface.blit(background_surface, (0, 0))

    back_arrow = pygame.image.load("Images/back.png").convert_alpha()
    arrow_position = back_arrow.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    back_arrow_hover = pygame.image.load("Images/back_hover.png").convert_alpha()

    picture = pygame.image.load(picture_path).convert()
    picture_position = picture.get_rect(center=(WIDTH // 2, 160))

    answer_button1 = Button(answer1, 320, 50, (60, 300), BLUE, DARK_BLUE, button_font_main,
                            WHITE, DARK_BLUE, 5)
    answer_button1.draw(main_surface)
    answer_button2 = Button(answer2, 320, 50, (420, 300), BLUE, DARK_BLUE, button_font_main,
                            WHITE, DARK_BLUE, 5)
    answer_button2.draw(main_surface)
    answer_button3 = Button(answer3, 320, 50, (60, 400), BLUE, DARK_BLUE, button_font_main,
                            WHITE, DARK_BLUE, 5)
    answer_button3.draw(main_surface)
    answer_button4 = Button(answer4, 320, 50, (420, 400), BLUE, DARK_BLUE, button_font_main,
                            WHITE, DARK_BLUE, 5)
    answer_button4.draw(main_surface)

    number_surface = small_title_font.render(number, True, BLACK)
    number_position = number_surface.get_rect(center=(WIDTH // 7, 60))

    buttons = [answer_button1, answer_button2, answer_button3, answer_button4]

    for i in range(len(buttons)):
        if buttons[i].text == correct_answer:
            correct_button = buttons[i]

    while running:
        main_surface.blit(picture, picture_position)
        main_surface.blit(back_arrow, arrow_position)

        main_surface.blit(number_surface, number_position)

        mouse_pos = pygame.mouse.get_pos()

        if arrow_position.collidepoint(mouse_pos):
            main_surface.blit(back_arrow_hover, arrow_position)
            if pygame.mouse.get_pressed()[0]:
                click.play()
                pygame.time.delay(100)
                levels()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if correct_button.pressed:
                    true.play()
                    score += 1
                    running = False
                else:
                    for i in range(len(buttons)):
                        if buttons[i].pressed:
                            false.play()
                            running = False

        answer_button1.check_click()
        answer_button1.draw(main_surface)
        answer_button2.check_click()
        answer_button2.draw(main_surface)
        answer_button3.check_click()
        answer_button3.draw(main_surface)
        answer_button4.check_click()
        answer_button4.draw(main_surface)

        pygame.display.update()
        clock.tick(FPS)

    return score


main_menu()
