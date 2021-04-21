import pygame
import sys
import numpy as np


pygame.init()

LINE_WIDTH = 15
LINE_COLOUR = (0, 128, 128)
BOARD_ROWS = 3
BOARD_COLS = 3

WIDTH = 600
HEIGHT = 600
BG_COLOUR = (28, 170, 156)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOUR )

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def lines(x1, y1, x2, y2):
  pygame.draw.line(screen, LINE_COLOUR,(x1, y1), (x2, y2), LINE_WIDTH)

def draw_lines():
  lines(50, 200, 550, 200) #1st horizontal line
  lines(50, 400, 550, 400) #2nd horizontal line
  lines(200, 50, 200, 550) #1st verticle line
  lines(400, 50, 400, 550)  

draw_lines()

#mainloop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.update()    