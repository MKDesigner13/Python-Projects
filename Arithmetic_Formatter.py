def arithmetic_arranger(problems, show_answers=False):
    #Check for amount of problems Error
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #Base variables
    dict_count = 1
    problem_dict = {}
    problem_string = ''
    four_space = '    '
    top_operands = []
    operands = []
    bottom_operands = []
    top_length_set = []
    top_string = ''
    operand_string = ''
    bottom_string = ''
    base_dashes = '------'
    dash_string = ''
    answer_string = ''
    answer_set = []

    #Add problems to problem dictionary
    for prob in problems:
        problem_dict[dict_count] = prob.split(' ')
        dict_count += 1

    #Iterate over problem dictionary
    for key, value in problem_dict.items():

        #Find longest operand
        top_length = 0
        if len(value[0]) >= len(value[2]):
            top_length = len(value[0])
        else:
            top_length = len(value[2])
        problem_dict[key].append(top_length)

        #Check for number length Error
        if top_length > 4:
            return 'Error: Numbers cannot be more than four digits.'

        #Append operation pieces to lists
        top_operands.append(value[0])
        operands.append(value[1])
        bottom_operands.append(value[2])
        top_length_set.append(value[3])

        #Check for wrong operator Error
        if value[1] != '+' and value[1] != '-':
            return "Error: Operator must be '+' or '-'."

        #Check for only digits Error
        if not value[0].isdigit() or not value[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        #Append answer to answer list
        if value[1] == '+':
            answer_set.append(int(value[0]) + int(value[2]))
        else:
            answer_set.append(int(value[0]) - int(value[2]))
    
    count = 0
    while count < len(problems):

        #Append values to string levels
        top_string += top_operands[count].rjust(top_length_set[count] + 2) + four_space

        #Combine operand and bottom string onto 1 line
        tmp_op_str = operands[count].ljust(top_length_set[count] + 2)
        tmp_op_str = tmp_op_str[:-len(bottom_operands[count])] + bottom_operands[count] + four_space

        operand_string += tmp_op_str
        dash_string += base_dashes[:top_length_set[count] + 2] + four_space

        answer_string += str(answer_set[count]).rjust(top_length_set[count] + 2) + four_space

        count += 1
                

    #Combine strings into problem_string
    top_string = top_string[:-4]
    operand_string = operand_string[:-4]
    dash_string = dash_string[:-4]
    problem_string += top_string + "\n" + operand_string + "\n" + dash_string

    #set problems to problem_string
    problems = problem_string

    #Check to show answers
    if show_answers:
        answer_string = answer_string[:-4]
        problems += "\n" + answer_string

    #Return statement
    return problems

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

