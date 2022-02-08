import pygame
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
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    sys.exit()
                
                # prints coordinate clicked to console
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                self.screen.fill(self.bg_color)

                pygame.display.update()

if __name__ == "__main__":
    set_game=Set()
    set_game.run_game()
