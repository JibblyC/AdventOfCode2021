#Read file into grid
grid_of_numbers = []
with open('Day9/day9_input.txt') as f:
    for line in f:
        line = line.strip()
        single_line_array = []
        for index in range(len(line)):
            single_line_array.append(line[index])
        grid_of_numbers.append(single_line_array)

def check_number_smaller(number_to_check,array_of_numbers):
    return all(i > number_to_check for i in array_of_numbers)

list_of_smallest_nums = []
for x in range(len(grid_of_numbers)):
    for y in range(len(grid_of_numbers[x])):
        # print("X:",x,"Y:",y)
        currentNumber_to_check = grid_of_numbers[x][y]
        # print(currentNumber_to_check)
        # print("---------------------")
        array_of_numbers_to_check = []
        if x == 0:
            if y == 0:
                array_of_numbers_to_check.append(grid_of_numbers[x + 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y + 1])
            else :
                array_of_numbers_to_check.append(grid_of_numbers[x + 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y - 1])
                if y != len(grid_of_numbers[x]) - 1:
                    array_of_numbers_to_check.append(grid_of_numbers[x][y + 1])
        elif x == len(grid_of_numbers) - 1:
            if y == len(grid_of_numbers[x]) - 1:
                array_of_numbers_to_check.append(grid_of_numbers[x - 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y - 1])
            else :
                array_of_numbers_to_check.append(grid_of_numbers[x - 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y - 1])
                array_of_numbers_to_check.append(grid_of_numbers[x][y + 1])
        elif y == 0:
                array_of_numbers_to_check.append(grid_of_numbers[x  + 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x  - 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y + 1])

        elif y == len(grid_of_numbers[x]) - 1:
                array_of_numbers_to_check.append(grid_of_numbers[x  + 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x  - 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y - 1])
        else:
                array_of_numbers_to_check.append(grid_of_numbers[x  + 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x  - 1][y])
                array_of_numbers_to_check.append(grid_of_numbers[x][y - 1])
                array_of_numbers_to_check.append(grid_of_numbers[x][y + 1])

        if check_number_smaller(currentNumber_to_check,array_of_numbers_to_check):
            list_of_smallest_nums.append(int(currentNumber_to_check) + 1)
    
    array_of_numbers_to_check.clear();


print(sum(list_of_smallest_nums))


        

            







