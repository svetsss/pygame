import pygame

from platform import Platform
from ball import Ball
from brick import Brick

pygame.init()

#  Определяем цвета
WHITE = (255,255,255)
BLUE = (0, 102, 153)
LIGHTBLUE = (102,204,255)
RED = (255,0,0)

score = 0
lives = 3

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Арканоид - Классическая игра из глубин времени")

sprites = pygame.sprite.Group()

#  Создаем платформу
platform = Platform(LIGHTBLUE, 100, 10)
platform.rect.x = 350
platform.rect.y = 560

#  Создаем шарик
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
# три ряда кирпичиков
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    sprites.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    sprites.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    sprites.add(brick)
    all_bricks.add(brick)

sprites.add(platform)
sprites.add(ball)
playing = True
clock = pygame.time.Clock()

# ИГРОВОЙ ЦИКЛ
while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              playing = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        platform.moveRight(5)
    sprites.update()

    if ball.rect.x >= 790:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.x <= 0:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.y > 590:
        ball.speed[1] = -ball.speed[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 44)
            text = font.render("Попытки закончились :(", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)  #задержка 3 секунды
            playing = False
    if ball.rect.y < 40:
        ball.speed[1] = -ball.speed[1]

    # Столкновение шарика и кирпича
    if pygame.sprite.collide_mask(ball, platform):
        ball.rect.x -= ball.speed[0]
        ball.rect.y -= ball.speed[1]
        ball.bounce()

    # Проверка удара шариком кирпичика
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks)==0:
            # Если все кирпичики разбиты - уровень пройдиен
            font = pygame.font.Font(None, 74)
            text = font.render("Уровень пройден", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Стоп игра
            playing=False

    screen.fill(BLUE)
    pygame.draw.line(screen, LIGHTBLUE, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Очков: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Попыток: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    sprites.draw(screen)

    pygame.display.flip()

    # 60 кадров в секунду
    clock.tick(60)

pygame.quit()