
# 1 = c,f == 2 *
# 4 = b,c,d,f == 4 *
# 7 = a,c,f == 3 *
# 8 = a,b,c,d,e,f,g == 7 *

# 3 = a,c,d,f,g == 5 ( If 1 is in here, we know its 3) *
# 2 = a,c,d,e,g == 5 last 5 remaining
# 5 = a,b,d,f,g == 5 (if 4 intersect this is > two  we know its 5)



# 9 = a,b,c,d,f,g == 6 ( 4 in here we know its 9) *
# 0 = a,b,c,e,f,g == 6 ( 1 in here we know its 0) *
# 6 = a,b,d,e,f,g == 6 (last 6) *



lines = []
with open('Day8/day8_input.txt') as f:
    lines = f.readlines()

totalSumArray = []

for currentLine in lines:
    array_of_numbers = list(currentLine.split("|")[0].strip().split(" "))
    array_of_output = list(currentLine.split("|")[1].strip().split(" "))
    numbers_dict = dict()

    #Poplate the map with the numbers we know
    for currentString in array_of_numbers:
        lengthOfString = len(currentString)
        if lengthOfString == 2:
            numbers_dict[1] = ''.join(sorted(currentString))
        if lengthOfString == 4:
            numbers_dict[4] = ''.join(sorted(currentString))
        if lengthOfString == 3:
            numbers_dict[7] = ''.join(sorted(currentString))
        if lengthOfString == 7:
            numbers_dict[8] = ''.join(sorted(currentString))       
    

    #Go back over the numbers and populate map based on above rules
    for currentString in array_of_numbers:
        lengthOfString = len(currentString)
        currentStringSorted = ''.join(sorted(currentString))
        if lengthOfString == 6 :
            currentStringArray = set(currentStringSorted);
            numFourArray = set(numbers_dict[4])
            if len(currentStringArray.intersection(numFourArray)) == 4:
                numbers_dict[9] = currentStringSorted
            else:
                numOneArray = set(numbers_dict[1])
                if len(currentStringArray.intersection(numOneArray)) > 1:
                    numbers_dict[0] = currentStringSorted
                else:
                    numbers_dict[6] = currentStringSorted

                
                
        if lengthOfString == 5:
            currentStringArray = set(currentStringSorted);
            numOneArray = set(numbers_dict[1]) 
            if len(currentStringArray.intersection(numOneArray)) == 2:
                numbers_dict[3] = currentStringSorted
            else:
                #convert to set
                numFourArray = set(numbers_dict[4])
                if len(currentStringArray.intersection(numFourArray)) > 2:
                    numbers_dict[5] = currentStringSorted
                else:
                    numbers_dict[2] = currentStringSorted
    

    #finally, loop over output and match up against map
    totalSum = ''
    for currentOut in array_of_output:
        for number, map in numbers_dict.items():
            sortedOutput = ''.join(sorted(currentOut))
            if sortedOutput == map:
                totalSum += str(number)

    totalSumArray.append(totalSum)


totalSumArrayInts = [int(i) for i in totalSumArray]
        

print("Sum of all numbers : ",sum(totalSumArrayInts))




