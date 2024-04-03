import time
import random

allteams = ["Team1","Team2","Team3","Team4","Team5"]

team1scores = 0
team2scores = 0
team3scores = 0
team4scores = 0
team5scores = 0

team1check = int()
team1type = "abc"
team1names = []

allevents = []

def Team2_Get_Info():
    print("team 2 is done")
def Team1_Get_Info():
    print("Welcome in Event")
    time.sleep(0.5)

    print("Teams can be single or with team")
    time.sleep(0.5)
    global allevents
    allevents = ["sports", "technology", "sings", "actors","skills"]
    teamlist = []

    print("\nThe events that can be join are",allevents)
    time.sleep(0.5)

    global team1type
    team1type = input("\n team 1 are you a 'team=t' or a single 'person=p'?")
    print(type(team1type))
    while team1type!="t" and team1type!="p":
        team1type = input("you can choose 't' for team or 'p' for single person.")

    global team1names
    team1names = []
    if team1type == 'p':
        print("team 1 is a person")
        team1names = input("Enter a single name....")
    elif team1type == 't':
        print("team 1 is a team")
        team1names = input("Enter all five names....")
        print("the names are:",team1names)

    global team1check
    team1check = int(input("Are we good to continue,'1' or would you like to make changes,'2'?"))

    while team1check != 1 and team1check != 2:
          team1check = int(input("press '1' to continue or '2' to make a change."))
    if team1check == 2:
        Team1_Get_Info()
    elif team1check == 1:
        Team2_Get_Info()

def Team2_Get_Info():
    print("team 2 is ready...")

Team1_Get_Info()

print("team 1 check value:",team1check,)
print("team 1 Type value:",team1type)
print("team 1 names value:",team1names)
print("Number of events:",len(allevents))
print(allevents)

event1choice = random.randrange(0,len(allevents))
print(event1choice)
print("Event 1 is:",allevents [event1choice])
del allevents [event1choice]


print("All Teams", allteams)
random.shuffle(allteams)
print("All Teams", allteams)
team1scores = allteams.index("Team1")
print("Team1 Score:", team1scores)
team2scores = allteams.index("Team2")
print("Team2 Score:", team2scores)
team3scores = allteams.index("Team3")
print("Team3 Score:", team3scores)
team4scores = allteams.index("Team4")
print("Team4 Score:", team4scores)
team5scores = allteams.index("Team5")
print("Team5 Score:", team5scores)

print(allevents)
print("Number of events:",len(allevents))
