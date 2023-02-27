import pygame
BLACK = (0,0,0)


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # вызывается контруктор базового класса
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Рисуем кирпичик
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Прямоугольник натягиваем на изображение
        self.rect = self.image.get_rect()