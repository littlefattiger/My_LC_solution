# https://leetcode.com/discuss/interview-question/system-design/194663/Design-a-class-that-represents-a-deck-of-cards

class card():
    def __init__(self, color, number):
        self.color = color
        self.number = number
import random
class deck():
    
    def __init__(self):
        self.cards = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cards.append(card(i,j))
        self.number_drawn = 0
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) == 0:
            return None
        return_card = self.cards.pop()
        print("the color is " + str(return_card.color), "the number is " + str(return_card.number))
        self.number_drawn += 1
        if self.number_drawn %4 == 0:
            self.shuffle()
            print("The deck has been shuffled")
deck = deck()
deck.draw()
deck.draw()
deck.draw()
deck.draw()
deck.draw()
deck.draw()
deck.draw()
