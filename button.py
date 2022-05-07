import pygame


# класс для создания кнопок
class Button:
    def __init__(self, text, width, height, pos, top_color, bottom_color, font, font_color, hover_color, elevation):
        # атрибуты кнопки
        self.text = text
        self.elevation = elevation
        self.previous_elevation = elevation
        self.original_y_position = pos[1]

        self.previous_color = top_color
        self.hover_color = hover_color
        self.pressed = False

        # верхняя часть кнопки
        self.top_rectangle = pygame.Rect(pos, (width, height))
        self.top_color = top_color

        # нижняя часть кнопки
        self.bottom_rectangle = pygame.Rect(pos, (width, elevation))
        self.bottom_color = bottom_color

        # текст
        self.text_surface = font.render(text, True, font_color)
        self.text_rectangle = self.text_surface.get_rect(center=self.top_rectangle.center)

    # отрисовка кнопки
    def draw(self, surface):
        self.top_rectangle.y = self.original_y_position - self.previous_elevation
        self.text_rectangle.center = self.top_rectangle.center

        self.bottom_rectangle.midtop = self.top_rectangle.midtop
        self.bottom_rectangle.height = self.top_rectangle.height + self.previous_elevation

        pygame.draw.rect(surface, self.bottom_color, self.bottom_rectangle, border_radius=15)
        pygame.draw.rect(surface, self.top_color, self.top_rectangle, border_radius=15)
        surface.blit(self.text_surface, self.text_rectangle)

    # проверка на нажатие мыши
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rectangle.collidepoint(mouse_pos):
            self.top_color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.previous_elevation = 0
                self.pressed = True
            else:
                self.previous_elevation = self.elevation
                if self.pressed:
                    self.pressed = False
        else:
            self.previous_elevation = self.elevation
            self.top_color = self.previous_color
