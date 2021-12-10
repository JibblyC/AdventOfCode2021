lines = []
with open('Day5/day5_input.txt') as f:
    lines = f.readlines()
completedMap = dict()


p1Array = []
p2Array = []
for line in lines:
    p1Array.append(list(map(int,line.split("->")[0].split(","))))
    p2Array.append(list(map(int,line.strip().split("->")[1].split(","))))

def update_dictionary(point):
    if tuple(point) in completedMap.keys():
        completedMap[tuple(point)] +=1
    else:
        completedMap[tuple(point)] = 1


for index in range(len(p1Array)):
    pointToAdd = []
    #Check Vertical
    if p1Array[index][0] == p2Array[index][0]:
       difference = p1Array[index][1] - p2Array[index][1]
       for subIndex in range(abs(difference) + 1):
            if difference > 0:
                pointToUpdate = [p1Array[index][0],p1Array[index][1] - subIndex]
            else:
                pointToUpdate = [p1Array[index][0],p1Array[index][1] + subIndex]
            update_dictionary(pointToUpdate)
    #Check Horizontal
    elif p1Array[index][1] == p2Array[index][1]:
        difference = p1Array[index][0] - p2Array[index][0]
        for subIndex in range(abs(difference) + 1):
            if difference > 0:
                pointToUpdate = [p1Array[index][0] - subIndex,p1Array[index][1]]
            else:
                pointToUpdate = [p1Array[index][0] + subIndex,p1Array[index][1]]
            update_dictionary(pointToUpdate)

    

totalCrossOvers = sum(value > 1 for value in completedMap.values())
print("Crossovers : ", totalCrossOvers)




