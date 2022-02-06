import pygame, sys, time
from pygame.locals import *
import random
from set_deck import Card, Deck
from game_board import Board


pygame.init()
mainClock = pygame.time.Clock()

CARDHEIGHT=100
CARDWIDTH=200
GUTTER=CARDWIDTH/10
ROWS=4
COLUMNS=4

deck = Deck()
deck.shuffle()

hand = [deck.deal_card() for i in range(0,16)]

# create 2d array of card upper left corner coordinates
board=Board(CARDWIDTH, CARDHEIGHT, GUTTER, ROWS, COLUMNS)

WINDOWWIDTH=((CARDWIDTH+GUTTER)*4 + GUTTER)
WINDOWHEIGHT=((CARDHEIGHT+GUTTER)*4 + GUTTER)

windowSurface = pygame.display.set_mode((board.total_width, board.total_height), 0, 32)
pygame.display.set_caption('SET')

def make_card_image(card_obj):
#the first set of values here should be x and y position to render the card at
    #creates a rect object with appropriate
    card = pygame.Rect(GUTTER, GUTTER, CARDWIDTH, CARDHEIGHT)
    cardImage = pygame.image.load(card_obj.image_uri)
    cardImageStretched = pygame.transform.scale(cardImage, (CARDWIDTH, CARDHEIGHT))
    return cardImageStretched

for row in board.board:
    for point in row:
        windowSurface.blit(make_card_image(hand.pop()), pygame.Rect(point[0],point[1], CARDWIDTH, CARDHEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def end_game():
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('You win!', True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

pygame.display.update()

# run the game loop
game_over = False
while game_over == False:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            pass
        
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

   # windowSurface.fill(WHITE)
   
   # pygame.display.update()
   # mainClock.tick(40)

