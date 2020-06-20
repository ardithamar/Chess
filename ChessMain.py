#User input is handled here

import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512  #Could try 400, higher will make the piece images blurry (they're low res)
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

#Load in images in dictionary. Called once only because calling it everytime will make game lag
def load_images():
    '''Loads in images'''
    pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

#Update graphics and User Input

def main():
    ''' Main '''
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, gs):
    ''' Draws both board and pieces '''
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    ''' Draws the chess board and chooses colors'''
    colors = [p.Color("navajowhite"), p.Color("sandybrown")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row+col)%2)]
            p.draw.rect(screen, color, p.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    ''' Draws pieces'''
    #This code can be instead just added to draw_board and would be more efficient. Only made it separate in 
    #case we wanted to add another drawing in between the board and pieces
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()
