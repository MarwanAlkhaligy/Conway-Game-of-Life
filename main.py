import pygame
import time
import random
import numpy as np
import os
import grid


os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution

width, height = 1080, 800
size = (width, height)
radius = 15
pygame.init()

pygame.display.set_caption("CONWAY'S GAME OF LIFE")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10

black = (0, 0, 0)
blue = (50, 121, 150)
blue1 = (0,100,71)
white = (255, 255, 255)

scaler = 30
offset = 5

Grid = grid.Grid(width,height, scaler, offset, radius)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)
    
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)
    pygame.display.update()

pygame.quit()
