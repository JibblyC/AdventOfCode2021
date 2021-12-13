lines = []
with open('Day7/day7_input.txt') as f:
    lines = f.readlines()

lines = lines[0].split(",")

all_hor_positions = [int(numeric_string) for numeric_string in lines]

array_of_sums = []

for index in range(max(all_hor_positions)):
    currentTotal = 0
    for current_pos in all_hor_positions:
        currentTotal += abs(index - current_pos);
    array_of_sums.append(currentTotal)


print("Minimum Fuel = " , min(array_of_sums))