# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:08:29 2021

@author: danie
"""
import random


class Card:
    """Dette er hvert individuelt kort"""
    def __init__(self, suit = "",rank = 0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        if self.rank == 0:
            return ""
        else:
            return str(self.rank) + " of " + self.suit
    def __lt__(self,other):
        return (self.suit,self.rank)<(other.suit,other.rank)


suit = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
rank =       {2:2,
             3:3,
             4:4,
             5:5,
             6:6,
             7:7,
             8:8,
             9:9,
             10:10,
             11: 'Jack',
             12: 'Queen',
             13: 'King',
             14: 'Ace'}

card = Card(suit=suit[random.randint(0,3)], rank=rank[random.randint(2,14)])

print(card)
