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

    if bracket_to_calculate == ")":
        return 3
    elif bracket_to_calculate == "]":
        return 57
    elif bracket_to_calculate == "}":
        return 1197
    else:
        return 25137

final_score_total = 0
for chunk in array_of_chunks:
    array_of_brackets = []
    for bracket in chunk:
        if bracket in open_brackets:
            array_of_brackets.append(bracket)
        else:
            open_bracket = array_of_brackets.pop()
            if not check_valid_bracket_combo(open_bracket,bracket):
                final_score_total += calculate_value_of_bracket(bracket)
                break;

           
                        
print("Final Score based on brackets : ", final_score_total)
        

