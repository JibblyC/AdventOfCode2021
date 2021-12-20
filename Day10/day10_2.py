array_of_chunks = []
open_brackets = ['(','{','[','<']
valid_brack_combos = [['(',')'],['{','}'],['[',']'],['<','>']]


with open('Day10/day10_input.txt') as f:
    for line in f:
        line = line.strip()
        array_of_chunks.append(line)

def check_valid_bracket_combo(openedBracket,closingBracket):
     for bracket_compare in valid_brack_combos:
                if closingBracket == bracket_compare[1]:
                    if openedBracket == bracket_compare[0]:
                        return True
                    else:
                        return False

def calculate_value_of_bracket(bracket_to_calculate):

    if bracket_to_calculate == "(":
        return 1
    elif bracket_to_calculate == "[":
        return 2
    elif bracket_to_calculate == "{":
        return 3
    else:
        return 4

array_of_scores = []
for chunk in array_of_chunks:
    array_of_brackets = []
    valid_array = True
    for bracket in chunk:
        if bracket in open_brackets:
            array_of_brackets.append(bracket)
        else:
            open_bracket = array_of_brackets.pop()
            if not check_valid_bracket_combo(open_bracket,bracket):
                valid_array = False
                break;
    if valid_array:
        currentScore = 0
        for current_bracket in reversed(array_of_brackets):
            currentScore = ( currentScore * 5 ) + calculate_value_of_bracket(current_bracket)
        array_of_scores.append(currentScore)

array_of_scores.sort()
middle_of_array =  int(len(array_of_scores) / 2)


                       
print("Middle of scores : ", array_of_scores[middle_of_array])
        

