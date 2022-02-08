import pygame
import sys
from pygame.locals import *
from set_deck import Card, Deck
from game_board import Board

class Set():
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.bg_color = (0, 100, 0)
        self.card_coords = self.board.get_coords()         
        
        self.screen = pygame.display.set_mode((self.board.total_width, self.board.total_height))
        pygame.display.set_caption("Set")
        
        self.deck = Deck(self)
        self.deck.shuffle()
        self.hand = [self.deck.deal_card() for i in range(0, 16)] 
        print(self.hand)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    sys.exit()
                
                # prints coordinate clicked to console
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                    # for each card that has been dealt, check if 
                    # the player clicked 
                    for card in self.hand:
                        if card.rect.collidepoint(event.pos):
                            card.select() == True
                            print(card.image_uri, card.selected)
                            card.load_image()

                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                self.screen.fill(self.bg_color)
               
                for index, card in enumerate(self.hand):
                    card.blit_me(self.card_coords[index])
               
                
                pygame.display.update()

if __name__ == "__main__":
    set_game=Set()
    set_game.run_game()
