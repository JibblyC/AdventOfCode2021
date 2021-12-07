lines = []
with open('Day3/day3_input.txt') as f:
    lines = f.readlines()

stringArray = [""] * len(lines[0].strip())
print(len(stringArray))

for line in lines:
    count = 0
    for character in line:
        if(character.isdigit()) :
            stringArray[count] += character
            count += 1
            

gammaBinary = ""
epsilonBinary = ""
for newString in stringArray:
    countZeros = newString.count("0");
    checkRemainder = len(lines) - countZeros
    if(checkRemainder > countZeros):
        gammaBinary = gammaBinary + "1"
        epsilonBinary = epsilonBinary + "0"
    else:
        gammaBinary = gammaBinary + "0"
        epsilonBinary = epsilonBinary + "1"

gammaDec = int(gammaBinary,2)
epsilonDec = int(epsilonBinary,2)

print("GammaBinary : " + gammaBinary + " GammaDec : " + str(gammaDec))
print("EpsilonBinary : " + epsilonBinary + " EpsilonDec : " + str(epsilonDec))

print("Power Consumption : " + str(gammaDec * epsilonDec))



