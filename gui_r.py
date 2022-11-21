import sys
import pygame
from pygame import *
from math import sqrt as sqrt

import time

WHITE = 255, 255, 255
BLACK = 0, 0, 0
red = 255, 0, 0
blue = 0,0,255
GRAY =  192,192,192
size = width, height = 480, 480
cell_width = (width/4)
cell_height = (height/4)
font_size = 50

def init():        
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(1, 4):
        pygame.draw.line(screen, BLACK, [0, (height/4)*i], [width, ((height/4)*i)], 4)
    # Vertical lines
    for i in range(1, 4):
        pygame.draw.line(screen, BLACK, [(width/4)*i, 0], [((width/4)*i), height], 4)
    
    return screen

def clearScreen(screen):
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(1, 4):
        pygame.draw.line(
            screen, BLACK, [0, (height/4)*i], [width, ((height/4)*i)], 4)
    # Vertical lines
    for i in range(1, 4):
        pygame.draw.line(
            screen, BLACK, [(width/4)*i, 0], [((width/4)*i), height], 4)


def getCell(pos):
    #first row
    if (pos[0] >= 0 and pos[0] < cell_width and pos[1] >= 0 and pos[1] < cell_height):
        return (0,0)
    if (pos[0] >= cell_width and pos[0] < cell_width*2 and pos[1] >= 0 and pos[1] < cell_height):
        return (0,1)
    if (pos[0] >= cell_width*2 and pos[0] < cell_width*3 and pos[1] >= 0 and pos[1] < cell_height):
        return (0,2)
    if (pos[0] >= cell_width*3 and pos[0] < width and pos[1] >= 0 and pos[1] < cell_height):
        return (0, 3)

    #second row
    if (pos[0] >= 0 and pos[0] < cell_width and pos[1] >= cell_height and pos[1] < cell_height*2):
        return (1, 0)
    if (pos[0] >= cell_width and pos[0] < cell_width*2 and pos[1] >= cell_height and pos[1] < cell_height*2):
        return (1, 1)
    if (pos[0] >= cell_width*2 and pos[0] < cell_width*3 and pos[1] >= cell_height and pos[1] < cell_height*2):
        return (1, 2)
    if (pos[0] >= cell_width*3 and pos[0] < width and pos[1] >= cell_height and pos[1] < cell_height*2):
        return (1, 3)

    #third row
    if (pos[0] >= 0 and pos[0] < cell_width and pos[1] >= cell_height*2 and pos[1] < cell_height*3):
        return (2, 0)
    if (pos[0] >= cell_width and pos[0] < cell_width*2 and pos[1] >= cell_height*2 and pos[1] < cell_height*3):
        return (2, 1)        
    if (pos[0] >= cell_width*2 and pos[0] < cell_width*3 and pos[1] >= cell_height*2 and pos[1] < cell_height*3):
        return (2, 2)
    if (pos[0] >= cell_width*3 and pos[0] < width and pos[1] >= cell_height*2 and pos[1] < cell_height*3):
        return (2, 3)

    #fourth row
    if (pos[0] >= 0 and pos[0] < cell_width and pos[1] >= cell_height*3 and pos[1] < height):
        return (3, 0)
    if (pos[0] >= cell_width and pos[0] < cell_width*2 and pos[1] >= cell_height*3 and pos[1] < height):
        return (3, 1)
    if (pos[0] >= cell_width*2 and pos[0] < cell_width*3 and pos[1] >= cell_height*3 and pos[1] < height):
        return (3, 2)
    if (pos[0] >= cell_width*3 and pos[0] < width and pos[1] >= cell_height*3 and pos[1] < height):
        return (3, 3)


def drawSymbole(screen, cell, symbole):  
    if(symbole == "X"):
        x00 = int(((width/4)*cell[1]) + 15)
        y00 = int(((height/4)*cell[0]) + 15)
        x01 = int((((width/4))*cell[1]) + cell_width-15)
        y01 = int(((height/4)*cell[0]) + cell_height-15)

        x10 = int(((width/4)*cell[1]) + cell_width-15)
        y10 = int(((height/4)*cell[0]) + 15)
        x11 = int(((width/4)*cell[1]) + 15)
        y11 = int(((height/4)*cell[0]) + cell_height-15)

        pygame.draw.line(screen, red, (x00, y00), (x01, y01), 4)
        pygame.draw.line(screen, red, (x10, y10), (x11, y11), 4)
    elif(symbole == "O"):
        # Cell[1] for x because it doesn't change on
        # the line
        x = int(((width/4)*cell[1]) + cell_width/2)
        y = int(((height/4)*cell[0]) + cell_height/2)
        pygame.draw.circle(screen, blue, (x, y), int((width/4/2)*0.9), 3)
    
    refresh()

def playerInput(screen):
    running = True
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                cell = getCell(pos)
                print(cell)
                return cell[0], cell[1]
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()  # quits pygame
    sys.exit()

def ask(screen, question, line=2):
    running = True
    # "ask(screen, question) -> answer"
    pygame.font.init()
    writeScreen(screen, question, line=line)
    center_yes_x = width/4
    center_yes_y = height/4
    center_no_x = (width/4)*2
    center_no_y = (height/4)
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                return
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()
    sys.exit()

def writeScreen(screen, txt, line=1):
    
    myfont = pygame.font.SysFont("monospace", font_size, bold= True)

    # render text
    label = myfont.render(txt, 50, (0, 105, 105))
    screen.blit(label, ((width/2)-(font_size/3)*len(txt), (height/4)*line))
    refresh()

def refresh():
    pygame.display.update()
    