import pygame
import random


pygame.display.set_caption("PyPong")
WIDTH = 800
HEIGHT = 600
FPS = 60
pygame.init()
pygame.font.init
BLACK = (50,50,50)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
ball = pygame.image.load("dengi_da_1.png")
player1 = pygame.image.load("blue_1.png")
player2 = pygame.image.load("red_1.png")
y_1 = HEIGHT // 2 - 50
y_2 = HEIGHT // 2 - 50
y_1_change = 0
y_2_change = 0



ball_dx = random.randrange(-5,5)
ball_dy = random.randrange(-5,5)

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

score_1 = 0
score_2 = 0

myfont = pygame.font.SysFont('Comic Sans MS', 30)
counter1 = myfont.render(str(score_1), False, (0,0,0))
counter2 = myfont.render(str(score_2), False, (0,0,0))




running = True
while running:
    clock.tick(FPS)
    # Ввод события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_2_change += 5
            if event.key == pygame.K_UP:
                y_2_change -= 5
            if event.key == pygame.K_w:
                y_1_change -= 5
            if event.key == pygame.K_s:
                y_1_change += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 y_2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                 y_1_change = 0
    if ball_y <= 0 or ball_y >= HEIGHT - 80:
        ball_dy = -ball_dy
    if ball_x <= 0:
        ball_dx = random.randrange(-5,5)
        ball_dy = random.randrange(-5,5)
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        score_2 += 1
        counter2 = myfont.render(str(score_2), False, (0,0,0))

    if ball_x + ball.get_width() >= WIDTH:
        ball_dx = random.randrange(-5,5)
        ball_dy = random.randrange(-5,5)
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        score_1 += 1
        counter1 = myfont.render(str(score_1), False, (0,0,0))

    if (ball_x <= player1.get_width() and ball_y >= y_1 and y_1 + player1.get_height () > ball_y + ball.get_height() ):
        ball_dx = abs(ball_dx)
    if (ball_x + ball.get_width() >= WIDTH - 25 and ball_y >= y_2 and y_2 + player2.get_height () > ball_y + ball.get_height() ):
        ball_dx = -abs(ball_dx) 


    y_2 += y_2_change
    if y_2 <= 0:
        y_2 = 0
    elif y_2 >= HEIGHT - 170:
        y_2 = HEIGHT - 170

    y_1 += y_1_change
    if y_1 <= 0:
        y_1 = 0
    elif y_1 >= HEIGHT - 170:
        y_1 = HEIGHT - 170


    ball_x += ball_dx
    ball_y += ball_dy


              
            
    screen.fill((255,255,255))
    screen.blit(ball, (ball_x - 2 , ball_y - 2))
    screen.blit(player1, (0, y_1))
    screen.blit(player2, (WIDTH - 25, y_2))
    screen.blit(counter1, (WIDTH*0.4, HEIGHT*0.1))
    screen.blit(counter2, (WIDTH*0.6, HEIGHT*0.1))
    pygame.display.flip()

pygame.quit()