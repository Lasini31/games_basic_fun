from turtle import update
import pygame
from pygame.color import Color

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Loop Game")
clock = pygame.time.Clock()
running = True
dt = 0

green = Color(0, 255, 0)
red = Color(200, 20, 20)

player_pos = pygame.Vector2(30, 30)
player_pos_2 = pygame.Vector2(470, 470)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill("white") 
    
    pygame.draw.circle(screen, green, player_pos, 20)
    pygame.draw.circle(screen, red , player_pos_2, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if player_pos.x < 0:
        player_pos.x = 500
    if player_pos.y < 0:
        player_pos.y = 500
    if player_pos.x > 500:
        player_pos.x = 0
    if player_pos.y > 500:
        player_pos.y = 0

    keys_2 = pygame.key.get_pressed()
    if keys_2[pygame.K_a]:
        player_pos_2.x -= 300 * dt
    if keys_2[pygame.K_d]:
        player_pos_2.x += 300 * dt
    if keys_2[pygame.K_w]:
        player_pos_2.y -= 300 * dt
    if keys_2[pygame.K_s]:
        player_pos_2.y += 300 * dt
    if player_pos_2.x > 500:
        player_pos_2.x = 0
    if player_pos_2.y > 500:
        player_pos_2.y = 0
    if player_pos_2.x < 0:
        player_pos_2.x = 500
    if player_pos_2.y < 0:
        player_pos_2.y = 500

    pygame.display.flip()
    dt = clock.tick(60)/1000

pygame.quit()

