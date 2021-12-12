lines = []
with open('Day6/day6_input.txt') as f:
    lines = f.readlines()

lines = lines[0].split(",")

starting_fish = [int(numeric_string) for numeric_string in lines]


keys = [0,1,2,3,4,5,6,7,8]
values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fish_count_map = dict(zip(keys, values))

#populate the dictionary with existing keys
for fish in starting_fish :
    if fish in fish_count_map.keys():
        fish_count_map[fish] +=1
    else:
        fish_count_map[fish] = 1


totalDays = 256

for currentDay in range(totalDays):
    fish_count_map_updated = dict(zip(keys, values))
    for key, value in fish_count_map.items():
        if key == 0:
            fish_count_map_updated[6] = value
            fish_count_map_updated[8] = value
        else:
            fish_count_map_updated[key - 1] += fish_count_map[key]
    fish_count_map.update(fish_count_map_updated)
    
        

print("Total fish after 256 Days : ", sum(fish_count_map.values()))
    
    

