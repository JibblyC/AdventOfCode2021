lines = []
lines_as_ints = []
with open('Day1/day1_1_input.txt') as f:
    lines = f.readlines()


lines_as_ints = [int(x) for x in lines]

currentSum = 0
compareSum = 0
totalCount = 0
counter = 0;
first = True;

while (counter < (len(lines) - 2 )):
    if(first):
        currentSum = lines_as_ints[counter] + lines_as_ints[counter + 1] + lines_as_ints[counter + 2];
        first = False;
    else:
        compareSum = currentSum
        currentSum = lines_as_ints[counter] + lines_as_ints[counter + 1] + lines_as_ints[counter + 2];
        if(currentSum > compareSum):
            totalCount += 1;
    counter += 1;

print("Total increments : " + str(totalCount));
    