import random

class Card:
    def __init__(self, number, pattern, color, shape):
        self.number = number
        self.pattern = pattern
        self.color = color
        self.shape = shape

    def __str__(self):
        if self.number == 2 or self.number == 3:
            return f"{self.number} {self.pattern} {self.color} {self.shape}s"
        else:
            return f"{self.number} {self.pattern} {self.color} {self.shape}"

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        for number in [1,2,3]:
            for pattern in ["empty","striped","solid"]:
                for color in ["red","green","purple"]:
                    for shape in ["diamond","pill","squiggle"]:
                        card = Card(number, pattern, color, shape)
                        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return (self.cards.pop())

