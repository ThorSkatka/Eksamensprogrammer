# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:04:33 2021

@author: mdsan
"""

#Exam program

'''
* vi skal lave et program, der registrerer stillingen i sportsbegivenheder.
* programmet bør udformes, så det kan generaliseres til 
    f.eks. nationale fodboldligaer eller andre sportsgrene.
* Elementer og struktur:
    - Registrer deltager ved at indlæse runderne
    - Udfra filerne lave en 2d list:
        > Kolonne 1 er kampene
        > Kolonne 2 er scorene i kampene
    - Automatisk find vinder ud fra scoren
    - Scoreboard display info:
        > Country
        > Games played
        > Games won
        > Games ended in a draw
        > Games lost
        > Total goals scored
        > - 
        > Total goals scored against team
        > Total points
            < 3 points for a win
            < 1 point for a draw
            < 0 points for a loss
'''

# def indlæser runder og opstiller in liste

# def bruger listen til at bestemme games played, drawn, won and lost

'''
> Country
> Games played
> Games won
    
> Games ended in a draw
> Games lost
> Total goals scored
> - 
> Total goals scored against team
> # Total points
    < 3 points for a win
    < 1 point for a draw
    < 0 points for a loss
'''

#Substitute for standings list
standings = [
            ['country1',0,0,0,0,0,0,0],
            ['country2',0,0,0,0,0,0,0]
            ]

#Index of team in standins
country1, country2 = 0,1

#Index of variables in team in standings
team,        g_played = 0,1
g_won,       g_drawn  = 2,3
g_lost,      ttl_scr  = 4,5
ttl_scr_agn, ttl_p    = 6,7



def who_won(l_score,r_score):
    # l_team wins: 0
    if l_score > r_score:
        return 0
    
    # r_team wins: 1
    elif l_score < r_score:
        return 1
    
    # draw: 2
    else:
        return 2

def point_giver(standings, l_team,r_team, l_score,r_score):
    result = who_won(l_score,r_score)
    
    #If left team won, add 3 points to their total points
    if result == 0:
        standings[l_team][ttl_p] =+ 3
        return standings
    
    ##If right team won, add 3 points to their total points
    elif result == 1:
        standings[r_team][ttl_p] =+ 3
        return standings
    
    #If its a draw, add 1 point to each teams total points
    else:
        standings[l_team][ttl_p] =+ 1
        standings[r_team][ttl_p] =+ 1
        return standings

#print(point_giver(standings, country1, country2, 3, 0))

#Adds games played, won, drawn and lost to standings for team
def games_wdl(l_team, r_team):
    if standings(who_won(l_score, r_score)) == 0: 
        standings[l_team][g_won] += 1
        standings[r_team][g_lost] += 1
        return standings
    
    elif standings(who_won(l_score, r_score)) == 1:
        standings[l_team][g_lost] += 1
        standings[r_team][g_won] += 1
        return standings 
    
    else:
        standings[l_team][g_drawn] += 1
        standings[r_team][g_drawn] += 1 
        return standings
        
