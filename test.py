import pygame
import time
import math
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
ball_image = pygame.image.load('ball.png')
ball_image = pygame.transform.scale(ball_image,(15,15))
ball_X = random.randint(0,785)
ball_Y = random.randint(0,585)
ball_Vx = random.uniform(-6,6)
ball_Vy = (7**2 - ball_Vx**2)**(1/2)
ball_rect = pygame.Rect(ball_X,ball_Y,15,15)


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	
	pygame.display.flip()
	clock.tick(60)