lines = []
with open('Day3/day3_input.txt') as f:
    lines = f.readlines()

oxygenArray = lines
c02Array = lines

def create_new_array(elementToKeep,arrayToIterate):
    return [binaryItem for binaryItem in arrayToIterate if binaryItem[count] == elementToKeep]

def does_list_have_more_zeros(stringToCheck):
    countZeros = currentIndexBits.count("0");
    return (len(currentIndexBits) - countZeros) >= countZeros



count = 0
while len(oxygenArray) > 1:
    currentIndexBits =  [x[count] for x in oxygenArray];
    if(does_list_have_more_zeros(currentIndexBits)):
        #create new array with only one bit in current index
        oxygenArray = create_new_array("1",oxygenArray)
    else:
        #create new array with only zero bit in current index
        oxygenArray = create_new_array("0",oxygenArray)
    count+=1


count = 0
while len(c02Array) > 1:
    currentIndexBits =  [x[count] for x in c02Array];
    if(does_list_have_more_zeros(currentIndexBits)):
        #create new array with only zero bit in current index
        c02Array = create_new_array("0",c02Array)
    else:
        #create new array with only one bit in current index
        c02Array = create_new_array("1",c02Array)
    count+=1


oxegenDec = int(oxygenArray[0],2)
c02LevelsDec = int(c02Array[0],2)

print("OxegenLevelsBin : " + oxygenArray[0] + "OxegenLevelsBinDec : " + str(oxegenDec))
print("c02LevelsBin : " + c02Array[0] + " c02LevelsDec : " + str(c02LevelsDec))

print("Power Consumption : " + str(oxegenDec * c02LevelsDec))
    



