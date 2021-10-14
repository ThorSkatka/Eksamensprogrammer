# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:04:33 2021

@author: mdsan, ericv
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

# Substitute for standings list
standings = [
            ['country1',0,0,0,0,0,0,0],
            ['country2',0,0,0,0,0,0,0]
            ]

# Index of team in standings
country1, country2 = 0,1

# Index of variables in team in standings
team,        g_played = 0,1
g_won,       g_drawn  = 2,3
g_lost,      ttl_gls  = 4,5
ttl_gls_c,   ttl_p    = 6,7


# Stores who won or a tie as result
def who_won(l_score,r_score):
    # l_team wins = 0
    if l_score > r_score:
        return 0
    
    # r_team wins = 1
    elif l_score < r_score:
        return 1
    
    # Tie = 2
    else:
        return 2


# Adds games played, won, tied and lost to standings for both teams
def games_wdl(standings, l_team,r_team, result):
    # Games played incremented by 1 
    standings[l_team][1] += 1
    standings[r_team][1] += 1
    
    # Adds 1 win and 1 loss to left team and right team respectively
    # Adds 3 points for left team
    if result == 0: 
        standings[l_team][g_won] += 1
        standings[r_team][g_lost] += 1
        
        standings[l_team][ttl_p] =+ 3
        
        return standings
    
    # Adds 1 win and 1 loss to right team and left team respectively
    # Adds 3 points for right team
    elif result == 1:
        standings[l_team][g_lost] += 1
        standings[r_team][g_won] += 1
        
        standings[r_team][ttl_p] =+ 3
        
        return standings
    
    # Adds 1 draw to both teams
    # Adds 1 point for both teams
    else:
        standings[l_team][g_drawn] += 1
        standings[r_team][g_drawn] += 1
        
        standings[l_team][ttl_p] =+ 1
        standings[r_team][ttl_p] =+ 1
        
        return standings


# Total goals scored and total goals conceded 
def goal_giver(standings,l_team,r_team,l_score,r_score):
    # Adds goals scored and goals conceded for left team 
    standings[l_team][ttl_gls] += l_score
    standings[l_team][ttl_gls_c] += r_score
    
    # Adds goals scored and goals conceded for right team
    standings[r_team][ttl_gls] += r_score
    standings[r_team][ttl_gls_c] += l_score
    
    return standings 


# Calls all functions and returns standings
def add_standings(standings,l_team,r_team,l_score,r_score):
    # Sets who_won as result for this match
    result = who_won(l_score, r_score)
    
    # Adds a win, draw or loss and points for both teams
    games_wdl(standings, l_team, r_team, result)
    
    # Adds the given goals scored to both teams
    goal_giver(standings, l_team, r_team, l_score, r_score)
    
    return standings


print(add_standings(standings, country1, country2, 4, 2))



'''
def point_giver(standings, l_team,r_team, result):
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
'''