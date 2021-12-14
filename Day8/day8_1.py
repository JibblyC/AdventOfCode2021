lines = []
with open('Day8/day8_input.txt') as f:
    lines = f.readlines()


array_of_scrambled = []
valid_lens = [2,3,4,7]
unique_digit_count = 0
for currentLine in lines:
    array_of_scrambled.append(currentLine.split("|")[1].strip().split(" "))

for current_list in array_of_scrambled:
    for currentDigit in current_list:
        if len(currentDigit) in valid_lens:
            unique_digit_count += 1


print(unique_digit_count)



