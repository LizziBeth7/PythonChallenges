nice = 0

strings = input("Enter the strings")
line = strings.split()

for x in line:
    double = False
    space = False
    prevletter = "."
    twoLettersAgo = "."
    doublesStore = ["  "]
    
    for y in x:
        pair = y + prevletter
        i = 0
        length = len(doublesStore)
        for z in doublesStore:
            #make sure its not matching the the previous added pair (so no overlap allowed)
            if(pair == doublesStore[i] and i != length-1):
                double = True
            i = i+1
        if(double == False):
            doublesStore.append(pair) 
            
        if(y == twoLettersAgo):
            space = True

        twoLettersAgo = prevletter
        prevletter = y

    if(double == True and space == True):
        nice = nice + 1
    
print(nice)
