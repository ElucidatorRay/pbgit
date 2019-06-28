import pygame
import time
import math
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
ball_image = pygame.image.load('ball.png')
ball_image = pygame.transform.scale(ball_image,(40,40))
ball_X = random.randint(0,760)
ball_Y = random.randint(0,560)
ball_Vx = random.uniform(-6,6)
ball_Vy = (20**2 - ball_Vx**2)**(1/2)
ball_rect = pygame.Rect(ball_X,ball_Y,40,40)
screen.blit(ball_image,(ball_X,ball_Y))

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	ball_X += ball_Vx
	ball_Y += ball_Vy
	if ball_X < 0 or ball_X > 760:
		ball_Vx *= -1
	if ball_Y < 0 or ball_Y > 560:
		ball_Vy *= -1
	screen.fill((0,0,0))
	screen.blit(ball_image,(ball_X,ball_Y))
	ball_rect.topleft = (ball_X,ball_Y)
	
	pygame.display.flip()
	clock.tick(60)