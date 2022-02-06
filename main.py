import pygame, sys, time
from pygame.locals import *
import random
from set_deck import Card, Deck
from game_board import Board

pygame.init()

CARDHEIGHT=100
CARDWIDTH=200
GUTTER=CARDWIDTH/10
ROWS=4
COLUMNS=4

deck = Deck()
deck.shuffle()

# create board object from config globals above
board=Board(CARDWIDTH, CARDHEIGHT, GUTTER, ROWS, COLUMNS)
windowSurface = pygame.display.set_mode((board.total_width, board.total_height), 0, 32)

# set pygame window caption
pygame.display.set_caption('SET')

def make_card_image(card_obj):
#the first set of values here should be x and y position to render the card at
    #creates a rect object with appropriate
    card = pygame.Rect(GUTTER, GUTTER, CARDWIDTH, CARDHEIGHT)
    cardImage = pygame.image.load(card_obj.image_uri)
    cardImageStretched = pygame.transform.scale(cardImage, (CARDWIDTH, CARDHEIGHT))
    return cardImageStretched

# take the card coordinates array from board object and
# render a card to each until you're out of points
for point in board.board:
    windowSurface.blit(make_card_image(deck.deal_card()), pygame.Rect(point[0],point[1], CARDWIDTH, CARDHEIGHT))

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
        
        # prints coordinate clicked to console
        if event.type == MOUSEBUTTONUP:
            print(event.pos)
        
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

   # windowSurface.fill(WHITE)
   
   # pygame.display.update()

