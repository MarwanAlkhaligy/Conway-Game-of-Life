import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset, radius):
        self.scale = scale
        
        self.radius = radius
        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
    # to initialize  array with random value 
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
    
                y_pos = y * self.scale
                x_pos = x * self.scale
                
                random_color = (random.randint(10, 255), random.randint(1, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.circle(surface, random_color, (x_pos + self.offset , y_pos + self.offset),self.radius, self.offset)
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    #pygame.draw.circle(surface, off_color, (x_pos ,  y_pos) , self.radius, self.offset)

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):  #  and (random.random() <= 0.8) 
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next

    def HandleMouse(self, x, y):
        _x = (x + self.radius) // self.scale
        _y = (y + self.radius) //self.scale
        
        _x %= self.rows
        _y %= self.columns
        
        if self.grid_array[_x][_y] != None:
            if self.grid_array[_x][_y] == 0:
               self.grid_array[_x][_y] = 1
        

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n) % self.rows
                y_edge = (y+m) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
