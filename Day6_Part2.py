grid=[]
for i in range(1000):
    col = []
    for j in range(1000):
        col.append(0)
    grid.append(col)

lightsBrightness = 0

with open("Day6Input.txt", 'r') as file:
    instructions = file.read()
    line = instructions.splitlines()
    k = 0
    
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
                    grid[i][j] = grid[i][j] + 1
            
                elif "toggle" in line[k]:
                    grid[i][j] = grid[i][j] + 2
                    
                elif "turn off" in line[k]:
                    grid[i][j] = grid[i][j] -1

                    
                if grid[i][j] < 0:
                        grid[i][j] = 0

        k = k+1

for p in range(0, 1000):
    for l in range(0, 1000):
        lightsBrightness = lightsBrightness + grid[p][l]
    
print(lightsBrightness)
