import random
import pygame

class Card:
    def __init__(self, number, pattern, color, shape, set_game):
        self.number = number
        self.pattern = pattern
        self.color = color
        self.shape = shape
        self.image_uri = self.get_image_uri() 
        self.set_game = set_game

    def __str__(self):
        if self.number == "two" or self.number == "three":
            return f"{self.number} {self.pattern} {self.color} {self.shape}s"
        else:
            return f"{self.number} {self.pattern} {self.color} {self.shape}"

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

