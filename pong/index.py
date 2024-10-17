import pygame
from board import Board 
from ball import Ball

pygame.init()
clock = pygame.time.Clock()
play = True

height = 720
width = 1080
windows = pygame.display.set_mode((width, height))

score_player1, score_player2 = 0, 0
font = pygame.font.Font(None, 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player1 = Board(100, height // 2, 10, 100, WHITE, 8)
player2 = Board(width - 100, height // 2, 10, 100, WHITE, 8)
ball = Ball(width//2, height//2, 15, 15, WHITE, 5, 5)

while play:
    delta_time = clock.tick(60) / 1000.0 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    windows.fill((BLACK))

    player1.move(pygame.K_z, pygame.K_s, height)
    player2.move(pygame.K_UP, pygame.K_DOWN, height)
    ball.move()

    player1.draw(windows)
    player2.draw(windows)
    ball.draw(windows)
    
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.velocity_x = -ball.velocity_x
    if ball.rect.x < 0:
        score_player2 += 1
        ball.rect.x = width//2
        ball.rect.y = height//2
        ball.velocity_x = -ball.velocity_x
    if ball.rect.x > width:
        score_player1 += 1
        ball.rect.x = width//2
        ball.rect.y = height//2
        ball.velocity_x = -ball.velocity_x

    score_text = font.render(f"{score_player1}", True, WHITE)
    lives_text = font.render(f"{score_player2}", True, WHITE)

    windows.blit(score_text, (50, 50))  
    windows.blit(lives_text, (width - 100, 50)) 

    pygame.display.update()

pygame.quit() 
