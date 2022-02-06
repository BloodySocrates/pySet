import pygame, sys, time
from pygame.locals import *
import random
from set_deck import Card, Deck

pygame.init()
mainClock = pygame.time.Clock()

deck = Deck()

CARDHEIGHT=100
CARDWIDTH=200
GUTTER=CARDWIDTH/10

def make_row(y_value):
    row=[]
    for i in range(0,4):
        cardx=GUTTER+(CARDWIDTH+GUTTER)*i
        cardy=y_value
        row.append((cardx, cardy))
    return row

row1=make_row(20)
print(row1)

def make_coords_array(y_values):
    coords_array=[]
    for y in y_values:
        row = make_row(y)
        coords_array.append(row)
    return coords_array

y_values=[GUTTER+(CARDHEIGHT+GUTTER)*i for i in range(0,4)]

coords_array = make_coords_array(y_values)
print(coords_array)

WINDOWWIDTH=((CARDWIDTH+GUTTER)*4 + GUTTER)
WINDOWHEIGHT=((CARDHEIGHT+GUTTER)*4 + GUTTER)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('SET')

#the first set of values here should be x and y position to render the card at
card = pygame.Rect(GUTTER, GUTTER, CARDWIDTH, CARDHEIGHT)
cardImage = pygame.image.load('./cards/one_striped_red_pill.png')
cardImageStretched = pygame.transform.scale(cardImage, (CARDWIDTH, CARDHEIGHT))

for row in coords_array:
    for point in row:
        windowSurface.blit(cardImageStretched, pygame.Rect(point[0],point[1], CARDWIDTH, CARDHEIGHT))

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
        
        windowSurface.blit(cardImageStretched, card)
        
        pygame.display.update()


        if event.type == MOUSEBUTTONUP:
            pass
    

   # windowSurface.fill(WHITE)
   
   # pygame.display.update()
   # mainClock.tick(40)

