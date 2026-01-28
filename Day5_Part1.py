nice = 0
substring1 = "ab"
substring2 = "cd"
substring3 = "pq"
substring4 = "xy"

strings = input("Enter the strings")
line = strings.split()

for x in line:
    double = False
    vowels = 0
    prevletter = "."
    NoBadParts = True

    if substring1 in x or substring2 in x or substring3 in x or substring4 in x:
        NoBadParts = False
    
    for y in x:
        if(y == "u" or y== "a" or y == "e" or y=="i" or y=="o"):
            vowels = vowels +1
        if(y == prevletter):
            double = True
        prevletter = y

    if(double == True and vowels >= 3 and NoBadParts == True):
        nice = nice + 1

    
print(nice)
