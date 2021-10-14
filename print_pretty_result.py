#import random #Used for testing

import io #Package for reading "æ, ø and å"

filepath = r'C:\Users\danie\Desktop\Alt\Skole\AAU\1. semester\Indledende Programmering for Datavidenskab\Lektion 7 - Eksamens 1 - Fodbold\nations.txt'

teamfile = io.open(filepath,mode="r",encoding="utf-8") #Open file, read (r) and encoding is UTF-8 (æ, ø, å)

teams = []
standings = []

def teamlist():
    for item in teamfile: #For each country + newline, add to the list
        teams.append(item.rstrip("\n")) #rstrip to strip "\n" from the right side of the string
    return teams


teamlist() #Add items to nations

for team in teamlist(): #Create lists within lists for every nation
    a = [team,0,0,0,0,0,0,0] #New list with nation and 7 zeros
    standings.append(a)


def pretty(text, spaces): #Formula to format the text from the list
    text = str(text) #Ensure type is str
    return text+((spaces-len(text))*" ") #Make sure the returns a value


#for i in standings: #Set index 7 to a random number for testing
#    i[7] = random.randint(0,20)
          

#Create sorted list based on index 7 (points)
#Lambda is an anonymous function, takes x as and argument and x[7] as an expression
#"key=" creates a new list to sort over - Lambda defines which elements are in the new list
#Lambda creates a functions, runs it and destroys it again
sorted_standings = sorted(standings, key = lambda x : x[7],reverse=True)

for item in sorted_standings: #Unmakes standings list, prints each item in list
    team = pretty(item[0],10) #For every list in standings, run the function
    plays = pretty(item[1],3)
    wins = pretty(item[2],2)
    draws = pretty(item[3],2)
    losses = pretty(item[4],3)
    goals = pretty(item[5],2)
    g_against = pretty(item[6],3)
    points = pretty(item[7],1)
    result = team + plays + wins + draws + losses + goals + "- " + g_against + points
    print(result)
