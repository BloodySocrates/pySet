import random
import pygame

class Card:
    def __init__(self, number, pattern, color, shape, set_game):
        self.number = number
        self.pattern = pattern
        self.color = color
        self.shape = shape
        self.selected = False
        self.image_uri = self.get_image_uri()
        self.grayscale_uri = self.get_grayscale()
                  
        self.set_game = set_game
        # initialize the card and set its starting position
        self.screen = set_game.screen
        self.screen_rect = set_game.screen.get_rect()
        # loads an image  
        self.image_stretched = self.load_image() 
        self.rect = self.image_stretched.get_rect()

 
    def load_image(self):
        # get image uri based on concatenated name prop
        if self.selected == True:
            image = pygame.image.load(self.grayscale_uri)
        else:
            image = pygame.image.load(self.image_uri)
        image_stretched = pygame.transform.scale(image, (self.set_game.board.cardwidth, self.set_game.board.cardheight))
        return image_stretched

    def select(self):
        self.selected = not(self.selected)
        self.image_stretched = self.load_image()

    def blit_me(self, coords):
        self.coords = coords
        self.rect.x=coords[0]
        self.rect.y=coords[1]
        self.screen.blit(self.image_stretched, self.rect)

    def __str__(self):
        if self.number == "two" or self.number == "three":
            return f"{self.number} {self.pattern} {self.color} {self.shape}s"
        else:
            return f"{self.number} {self.pattern} {self.color} {self.shape}"
    
    def get_grayscale(self):
        if self.number == "two" or self.number == "three":
            return f"grayscale/{self.number}_{self.pattern}_{self.color}_{self.shape}s.png"
        else:
            return f"grayscale/{self.number}_{self.pattern}_{self.color}_{self.shape}.png"

    def get_image_uri(self):
        if self.number == "two" or self.number == "three":
            return f"cards/{self.number}_{self.pattern}_{self.color}_{self.shape}s.png"
        else:
            return f"cards/{self.number}_{self.pattern}_{self.color}_{self.shape}.png"

    
class Deck:
    def __init__(self, set_game):
        self.set_game = set_game
        self.cards=[]
        self.build()

    def build(self):
        for number in ["one","two","three"]:
            for pattern in ["empty","striped","solid"]:
                for color in ["red","green","purple"]:
                    for shape in ["diamond","pill","squiggle"]:
                        card = Card(number, pattern, color, shape, self.set_game)
                        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return (self.cards.pop())

