# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:14:50 2021

@author: andre
"""
highest = 0
h_index = 0
for i in range(len(player_names)):
    if player_names[i] > highest:
        highest = player_names[i]
        h_index = i

print(highest)
print(h_index)
print(f'Player {h_index} has won the game!')
