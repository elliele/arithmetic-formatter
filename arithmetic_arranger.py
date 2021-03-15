# Created by Ellie Le at 3/14/2021

def arithmetic_arranger(problems,solve=''):
    total = 0
    top_line =''
    bottom_line = ''
    sum_line = ''
    dash = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        x = problem.split(' ')
        top, operator, bottom = x
        if not top.isnumeric() or not bottom.isnumeric():
            return 'Error: Numbers must only contain digits.'
        if len(top) > 4 or len(bottom) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == "+":
            total = int(top) + int(bottom)
        elif operator == "-":
            total = int(top) - int(bottom)
        else:
            return "Error: Operator must be '+' or '-'."

        length = max(len(top), len(bottom)) + 2

        if problem != problems[-1]:
            separator = ' '*4
            dash += str('-'*length) + separator
            top_line += top.rjust(length) + separator
            bottom_line += operator + bottom.rjust(length-1) + separator
            sum_line += str(total).rjust(length) + separator
        else:
            dash += str('-' * length)
            top_line += top.rjust(length)
            bottom_line += operator + bottom.rjust(length - 1)
            sum_line += str(total).rjust(length)


    if solve:
        arranged_problems = top_line +'\n'+ bottom_line +'\n' + dash +'\n' + sum_line
    else:
        arranged_problems = top_line +'\n'+ bottom_line +'\n' + dash

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
