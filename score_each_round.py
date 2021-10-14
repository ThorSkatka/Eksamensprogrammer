'''
Første eksamens opgave i IPD: Sports resultater

@authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen
'''

import io #Package for reading "æ, ø and å"

# Substitute for standings list
standings = []

# Index of team in standings
country1, country2 = 0,1

# Index of variables in team in standings
team,        g_played = 0,1
g_won,       g_drawn  = 2,3
g_lost,      ttl_gls  = 4,5
ttl_gls_c,   ttl_p    = 6,7

for j in range(1,7): #Run the program for every file
    filepath1 = r'C:\Users\ericv\OneDrive - Aalborg Universitet\DV\Programmering\Eksamens_programmer\Eksamensprogrammer\round'+str(j)+'.txt'
    
    r1_file = io.open(filepath1,mode="r",encoding="utf-8") #Open file, read (r) and encoding is UTF-8 (æ, ø, å)
    
    matches1 = r1_file.read() #Take strings from file
    
    matchlist = matches1.split('\n') #Create a list where we split file content by newline
    
    typelist = [] #Prepare a list split by goals and nations
    
    for item in matchlist: #Take every list from matchlist
        i = item.split('\t') #Split it by "tab" (large space) - Creates new lists
        typelist.append(i) #Add new lists to the typelist
    
    splitlist = [] #List that splits nations and scores into seperate lists by match
    
    for types in typelist:
        a = types[0].split(" - ") #Split the list with nations into items by " - " - Changes an item into more items [Danmark-Skotland] becomes [Danmark,Skotland]
        b = types[1].split(" - ") #Split the list of scores into items by " - " - Changes an item into more items [0-2] becomes [0,2]
        splitlist.append([a ,b]) #Append the new lists

    for match in splitlist: #Take values for nations and scores individually
        leftteam = match[0][0] #Values to be extracted to standings
        rightteam = match[0][1] #First index is either country or score, next index is left or right
        leftscore = match[1][0]
        rightscore = match[1][1]
        print(leftteam+' - '+rightteam+' : '+leftscore+' - '+rightscore)