import pygame
import time
import math


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	
	
	
	pygame.display.flip()
	clock.tick(60)