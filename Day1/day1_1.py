lines = []
with open('Day1/day1_1_input.txt') as f:
    lines = f.readlines()

current = 0;
previous = 0;
first = True;
totalCount = 0
for line in lines:
    if(first):
        current = int(line);
        first = False;
    else:
        previous = current;
        current = int(line)
        if(current > previous):
            totalCount += 1;

print("Total increments : " + str(totalCount));