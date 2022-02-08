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
        self.selected_cards = []
    
    def is_set(self):
        # put each cards attributes in respective sets. if each sets length is either 3 or 1, it is a set  
        number = set([c.number for c in self.selected_cards])
        pattern = set([c.pattern for c in self.selected_cards])
        color = set([c.color for c in self.selected_cards])
        shape = set([c.shape for c in self.selected_cards])
        sets = []
        sets.extend([len(number), len(pattern),len(color),len(shape)])
        print(sets)
        if 2 not in sets:
            return True
        else:
            return False


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
                    # the player clicked it
                    for card in self.hand:
                        if card.rect.collidepoint(event.pos):
                            card.select() 
                            self.selected_cards.append(card)
                            if len(self.selected_cards) == 3:
                                print(self.is_set())
                                if self.is_set():
                                    self.hand = list(filter(lambda x : x.selected == False, self.hand))
                                    for i in range(0,3):
                                        self.hand.append(self.deck.deal_card())
                                    self.selected_cards = []
                                else:
                                    for card in self.selected_cards:
                                        card.select()
                                    self.selected_cards = []



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
