lines = []
with open('Day2/day2_1_input.txt') as f:
    lines = f.readlines()


horizontalPos = 0;
depthPos = 0;
aimPos  = 0;

for line in lines:
    currentLine = line.split();

    direction = currentLine[0];
    distance = int(currentLine[1]);

    if (direction == "forward"):
        horizontalPos += distance;
        depthPos += (aimPos * distance)
    elif (direction == "down"):
        aimPos += distance
    else:
        aimPos -= distance;

print("Horizontal Position : " + str(horizontalPos))
print("Depth Position : " + str(depthPos))
print("Multiplied together : " + str(depthPos * horizontalPos))
