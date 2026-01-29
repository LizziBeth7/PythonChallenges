grid=[]
for i in range(1000):
    col = []
    for j in range(1000):
        col.append(False)
    grid.append(col)

lightsOn = 0

with open("Day6Input.txt", 'r') as file:
    instructions = file.read()
    line = instructions.splitlines()
    k = 0
    #print("working")
    for parts in line:
        words = line[k].split()
        numbers = []
        for n in words:
            if "," in n:
                things = n.split(',')
                numbers.append(int(things[0]))
                numbers.append(int(things[1]))
        
        for i in range(numbers[0], numbers[2]+1):
            for j in range(numbers[1], numbers[3]+1):
                if "turn on" in line[k]:
                    grid[i][j] = True
            
                elif "toggle" in line[k]:
                    grid[i][j] = not grid[i][j]
                    
                elif "turn off" in line[k]:
                    grid[i][j] = False

        k = k+1

for p in range(0, 1000):
    for l in range(0, 1000):
        if grid[p][l] == True:
            lightsOn = lightsOn +1
    
print(lightsOn)
