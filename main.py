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
        pygame.draw.line(screen, CROSS_COLOUR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col*SQUARE_SIZE+SQUARE_SIZE-SPACE, row*SQUARE_SIZE+SPACE), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOUR, (col*SQUARE_SIZE+SPACE, row*SQUARE_SIZE+SPACE), (col*SQUARE_SIZE+SQUARE_SIZE-SPACE, row*SQUARE_SIZE+SQUARE_SIZE-SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
  board[row][col] == 1  


def available_square(row, col):
  return board[row][col] == 0


def is_board_full():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 0:
        return False
  return True


def check_win(player):
  #vertical win check
  for col in range(BOARD_COLS):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player :
      draw_vertical_winning_line(col, player)
      return True

  #horizontal win check
  for row in range(BOARD_ROWS):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      draw_horizontal_winning_line(row, player)
      return True

  #asc diagonal win check
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    draw_asc_diagonal()
    return True

  #desc diagonal win check
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    draw_desc_diagonal()
    return True

  return False


def color_win(player):
  if player == 1:
    return CIRCLE_COLOUR
  elif player == 2:
    return CROSS_COLOUR
 

def draw_vertical_winning_line(col, player):
  posX = col*SQUARE_SIZE+SQUARE_SIZE//2
  color = color_win(player)

  pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), 15)


def draw_horizontal_winning_line(row, player):
  posY = row*SQUARE_SIZE+SQUARE_SIZE//2
  color = color_win(player)

  pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), 15)


def draw_asc_diagonal(player):
  color = color_win(player)
  pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15 , 15), 15)
  

def draw_desc_diagonal(player):
  color = color_win(player)
  pygame.draw.line(screen, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)


def restart():
  screen.fill( BG_COLOUR )
  draw_lines()
  player = 1

  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      board[row][col] = 0


draw_lines()
player = 1
game_over = False


#mainloop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  if event.type == pyagame.MOUSEBUTTONDOWN and not game_over:
    mouseX = event.pos[0]
    mouseY = event.pos[1]
    
    
  pygame.display.update()    