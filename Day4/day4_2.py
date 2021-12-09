count = 0
rows, columns = (5, 5)
gameboard = [[0]*columns]*rows
gameboardsArray = []
winningBoards = []

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
                    gameBoard[col][row] = "X"
    
def check_for_bingo():
    for gameBoardNum in range(len(gameboardsArray)):
        for col in range(columns):
                #check Horizontal
                if gameboardsArray[gameBoardNum][col].count("X") == 5:
                    winningBoards.append(gameBoardNum)

    for gameBoardNum in range(len(gameboardsArray)):
        for row in range(rows):
            #check vertical
            verticalArray = []
            for col in range(columns):
                verticalArray.append(gameboardsArray[gameBoardNum][col][row])
                if verticalArray.count("X") == 5:
                    winningBoards.append(gameBoardNum)

boardNumber = 0
winningNumber = 0

for num in numbers:
    update_all_boards_with_current_number(num)
    check_for_bingo();
    winningBoards = list(set(winningBoards))
    #Down to one board, so need to find out which one for final calculation
    if len(winningBoards) == (len(gameboardsArray) -1):
        count = 0
        for value in winningBoards:
            if value != count:
                boardNumber = count
                break
            count +=1

    #All Bingos completed, mark the winning number
    if len(winningBoards) == (len(gameboardsArray)):
        winningNumber = num
        break;


sumOfNumbersLeft = 0
winningBoard = gameboardsArray[boardNumber]

for col in range(columns):
    for row in range(rows):
        if winningBoard[col][row] != "X":
            sumOfNumbersLeft += int(winningBoard[col][row])

print("Winning Number: ", winningNumber)
print("Sum of Values left on Winning Board: ",sumOfNumbersLeft)
print("These values Multiplied " + str(sumOfNumbersLeft * int(winningNumber)))



    




                    
        
