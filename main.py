import pygame
import sys
import numpy as np

#initialize pygame
pygame.init()

#constraints
BOARD_ROWS = 3
BOARD_COLS = 3
HEIGHT = 600
WIDTH = HEIGHT
SQUARE_SIZE = WIDTH//BOARD_COLS
LINE_WIDTH = 15
CIRCLE_RADIUS = SQUARE_SIZE // BOARD_COLS
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

#Colours
LINE_COLOUR = (0, 128, 128)
BG_COLOUR = (28, 170, 156)
CIRCLE_COLOUR = (239, 231, 200)
CROSS_COLOUR = (66, 66, 66)

#set game background
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOUR )

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def lines(x1, y1, x2, y2):
  pygame.draw.line(screen, LINE_COLOUR,(x1, y1), (x2, y2), LINE_WIDTH)

def draw_lines():
  lines(0, SQUARE_SIZE, WIDTH, SQUARE_SIZE) #1st horizontal line
  lines(0, 2 * SQUARE_SIZE, WIDTH, 2 * SQUARE_SIZE) #2nd horizontal line
  lines(SQUARE_SIZE, 0, SQUARE_SIZE, HEIGHT) #1st verticle line
  lines(2 * SQUARE_SIZE, 0, 2 * SQUARE_SIZE, HEIGHT) #2nd verticle lines

def draw_figures():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 1:
        pygame.draw.circle(screen, CIRCLE_COLOUR, ((col * SQUARE_SIZE + SQUARE_SIZE // 2),(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
      elif board[row][col] == 2:
        pygame.draw.line(screen, CROSS_COLOUR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), ())  

draw_lines()

#mainloop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.update()    