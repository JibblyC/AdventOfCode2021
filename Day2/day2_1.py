lines = []
with open('Day2/day2_input.txt') as f:
    lines = f.readlines()


horizontalPos = 0;
depthPos = 0;

for line in lines:
    currentLine = line.split();

    direction = currentLine[0];
    distance = int(currentLine[1]);

    if (direction == "forward"):
        horizontalPos += distance;
    elif (direction == "down"):
        depthPos += distance;
    else:
        depthPos -= distance;

print("Horizontal Position : " + str(horizontalPos))
print("Depth Position : " + str(depthPos))
print("Multiplied together : " + str(depthPos * horizontalPos))
