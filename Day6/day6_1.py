lines = []
with open('Day6/day6_input.txt') as f:
    lines = f.readlines()

lines = lines[0].split(",")

array_of_fish = [int(numeric_string) for numeric_string in lines]

totalDays = 80

for currentDay in range(totalDays):
    updated_array_of_fish = []
    for idx, fish in enumerate(array_of_fish):
        if fish == 0:
            array_of_fish[idx] = 6;
            updated_array_of_fish.append(8)
        else:
            array_of_fish[idx] -=1
    updated_array_of_fish.extend(array_of_fish)
    array_of_fish = updated_array_of_fish

print("Total fish after 80 Days : ", len(array_of_fish))
        
    
    

