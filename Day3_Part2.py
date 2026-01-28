NS = 0
EW = 0
NSrobot = 0
EWrobot = 0
visited = "false"

turn = 0;

houses = ["0,0"]

directions = input("Enter the directions ")
for x in directions:
    if(turn == 0):
        # santa 
        if(x == "^"):
            NS = NS+1
        elif(x == "v"):
            NS = NS-1
        elif(x == ">"):
            EW = EW + 1
        elif(x == "<"):
            EW = EW - 1
        newCo = str(NS) +","+ str(EW)

        i = 0;
        for y in houses:
            if(newCo == houses[i]):
                visited = "true"
            i = i+1
    
        if(visited == "false"):
            houses.append(newCo)
        visited = "false"
        turn = 1

    #robot santa
    elif(turn == 1):
        if(x == "^"):
            NSrobot = NSrobot+1
        elif(x == "v"):
            NSrobot = NSrobot-1
            
        elif(x == ">"):
            EWrobot = EWrobot + 1
        elif(x == "<"):
            EWrobot = EWrobot - 1
        newCo = str(NSrobot) +","+ str(EWrobot)

        i = 0;
        for y in houses:
            if(newCo == houses[i]):
                visited = "true"
            i = i+1
    
        if(visited == "false"):
            houses.append(newCo)
        visited = "false"
        turn = 0

#count houses
h = 0
for z in houses:
    h = h+1

print(h)
