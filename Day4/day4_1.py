count = 0
rows, columns = (5, 5)
gameboard = [[0]*columns]*rows
gameboardsArray = []

lines = []
with open('Day4/day4_input.txt') as f:
    lines = f.readlines()


#Extract Bingo Numbers
numbers = list(filter(None, lines[0].strip().split(',')))
#Remove Bingo numbers and first empty line from array
lines.pop(0)
lines.pop(0)

#Covert the array into a list of 2D array / gameboards
for line in lines: 
    #We know this is an empty line  
    if len(line) != 1:
        #split the row into individual units / Filter out the emptys / convert to integers
        row = list(filter(None, line.strip().split(' ')))
        gameboard[count] = row
        count +=1
        if count > 4:
            gameboardsArray.append(gameboard)
            gameboard = [[0]*columns]*rows
            count = 0

def update_all_boards_with_current_number(currentNumber):
    for gameBoard in gameboardsArray:
        for col in range(columns):
            for row in range(rows):
                if gameBoard[col][row] == currentNumber:
                    gameBoard[col][row] = "-1"
    

def check_for_bingo():
    for gameBoardNum in range(len(gameboardsArray)):
        for col in range(columns):
                #check Horizontal
                if gameboardsArray[gameBoardNum][col].count("-1") == 5:
                    return gameBoardNum

    for gameBoardNum in range(len(gameboardsArray)):
        for row in range(rows):
            #new Array of Vertical and check
            verticalArray = []
            for col in range(columns):
                verticalArray.append(gameboardsArray[gameBoardNum][col][row])
            if verticalArray.count("-1") == 5:
                return gameBoardNum


boardNumber = 0
winningNumber = 0

for num in numbers:
    update_all_boards_with_current_number(num)
    winBingo = check_for_bingo();
    if winBingo is not None:
        boardNumber = winBingo
        winningNumber = num
        break

sumOfNumbersLeft = 0
winningBoard = gameboardsArray[boardNumber]

for col in range(columns):
    for row in range(rows):
        if winningBoard[col][row] != "-1":
            sumOfNumbersLeft += int(winningBoard[col][row])

print("Winning Number: ", winningNumber)
print("Sum of Values left on Winning Board: ",sumOfNumbersLeft)
print("These values Multiplied " + str(sumOfNumbersLeft * int(winningNumber)))



    




                    
        
