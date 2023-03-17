import pygame
import sys
import time
import random

difficulty = 10  # количество кадров в секунду

frame_size_x = 720  # размер окна по х
frame_size_y = 480  # размер окна по y
pygame.display.set_caption('Snake')  # Название игры - отображается вверху окна
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))  # Создаем игровое окно в соответствии с размерами

let_x = [[random.randrange(1, (frame_size_x // 10)) * 10], [random.randrange(1, (frame_size_x // 10)) * 10], [random.randrange(1, (frame_size_x // 10)) * 10]]
let_y = [[random.randrange(1, (frame_size_y // 10)) * 10], [random.randrange(1, (frame_size_y // 10)) * 10], [random.randrange(1, (frame_size_y // 10)) * 10]]

#Задаем цвета используемые для игры
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
puple = pygame.Color(160, 32, 240)
fps_controller = pygame.time.Clock()

snake_pos = [100, 50] # начальные координаты в пикселях головы змейки
snake_body = [[100, 50], [90, 50], [80, 50]] # координаты и размер тела змейки

# Создаем еду
food_pos1 = [random.randrange(1, (frame_size_x // 10)), random.randrange(1, (frame_size_y // 10))]
food_pos2 = [random.randrange(1, (frame_size_x // 10)), random.randrange(1, (frame_size_y // 10))]
food_pos3 = [random.randrange(1, (frame_size_x // 10)), random.randrange(1, (frame_size_y // 10))]
food_spawn1 = False
food_spawn2 = False
food_spawn3 = False

direction = 'RIGHT' # задаем направление змейки
change_to = direction

score = 0  # количество очков
pygame.init()

def let(x,y):
    let = [x, y]
    let_body = []
    m = 0
    for i in range(5):
        let_body.append([])
        for j in range(1):
            let_body[i] = [let[0], let[1] + m]
            m += 10
    return let_body

def game_over(): # функция выхода из игры
    my_font = pygame.font.SysFont('arial', 90)  # задаем шрифт
    my_font_score = pygame.font.SysFont('arial', 30)  # задаем шрифт
    game_over_surfase = my_font.render('GAME OVER', True, red)  # формируем отображаемую надпись
    game_over_score = my_font_score.render('SCORE = ' + str(score), True, yellow)
    game_over_rect = game_over_surfase.get_rect()  #  создаем прямоугольную область надписи GAME OVER относительно размеров шрифта
    game_over_rect_score = game_over_score.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)  #  задаем расположение надписи GAME OVER
    game_over_rect_score.midtop = (frame_size_x / 2, (frame_size_y / 4) + 100)
    game_window.fill(black)  #  заливаем окно черным цветом
    game_window.blit(game_over_surfase, game_over_rect)  #  отображаем надпись GAME OVER
    game_window.blit(game_over_score, game_over_rect_score)
    pygame.display.flip()  #  обновляем экран
    time.sleep(3)  #  ждем 3 секунды
    pygame.quit()  #  выходим из игры
    sys.exit()  #  выходим из игры

def game_score():
    score_font = pygame.font.SysFont('arial', 20)
    score_surface = score_font.render('Score = ' + str(score), True, green)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (0, 0)
    game_window.blit(score_surface, score_rect)

while True:
    for event in pygame.event.get():  # событие выхода
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #  статус клавиш
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('r'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('l'):
                change_to = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10 # Отсчет с верхнего левого угла (поэтому "-")
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10

    snake_body.insert(0, list(snake_pos))  # записываем новую позицию головы

    if snake_pos[0] == food_pos1[0] and snake_pos[1] == food_pos1[1]:
        score += 1
        food_spawn1 = False
        difficulty += 0.5
    elif snake_pos[0] == food_pos2[0] and snake_pos[1] == food_pos2[1]:
        score += 1
        food_spawn2 = False
        difficulty += 0.5
    elif snake_pos[0] == food_pos3[0] and snake_pos[1] == food_pos3[1]:
        score += 1
        food_spawn3 = False
        difficulty += 0.5
    else:
        snake_body.pop()

    if not food_spawn1:
        food_pos1 = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn1 = True
    if not food_spawn2:
        food_pos2 = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn2 = True
    if not food_spawn3:
        food_pos3 = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn3 = True

    game_window.fill(black)
    pygame.draw.rect(game_window, blue, pygame.Rect(food_pos1[0], food_pos1[1], 10, 10))
    pygame.draw.rect(game_window, puple, pygame.Rect(food_pos2[0], food_pos2[1], 10, 10))
    pygame.draw.rect(game_window, yellow, pygame.Rect(food_pos3[0], food_pos3[1], 10, 10))
    game_score()

    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

    for pos in let(let_x[0][0], let_y[0][0]):
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 10, 10))
        for block in let(let_x[0][0], let_y[0][0]):
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
    for pos in let(let_x[1][0], let_y[1][0]):
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 10, 10))
        for block in let(let_x[1][0], let_y[1][0]):
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
    for pos in let(let_x[2][0], let_y[2][0]):
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 10, 10))
        for block in let(let_x[2][0], let_y[2][0]):
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()


    if snake_pos[0] < 0:
        snake_pos[0] = frame_size_x - 10
    if snake_pos[0] > frame_size_x - 10:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = frame_size_y
    if snake_pos[1] > frame_size_y:
        snake_pos[1] = -10

    for block in snake_body[3::]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
    fps_controller.tick(difficulty)








