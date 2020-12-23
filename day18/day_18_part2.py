def process_expression(expression: str):
    current_operator = ""
    current_result = -1

    hold_left = -1
    hold_operator = ""

    i = 0
    while i < len(expression):
        c = expression[i]
        if c == "(":
            index_of_close_parentheses = find_index_of_close_parentheses(expression[i + 1:]) + i + 1

            if current_result == -1:
                current_result = process_expression(expression[i + 1: index_of_close_parentheses])
            else:
                if current_operator != "":
                    if hold_left == -1:
                        if len(expression) > (index_of_close_parentheses + 2) and expression[
                            index_of_close_parentheses + 2] == "+":
                            hold_left = current_result
                            hold_operator = current_operator
                            current_result = process_expression(expression[i + 1: index_of_close_parentheses])
                        else:
                            current_result = eval(str(current_result) + current_operator + str(
                                process_expression(expression[i + 1: index_of_close_parentheses])))
                    else:
                        if len(expression) > (index_of_close_parentheses + 2) and expression[
                            index_of_close_parentheses + 2] == "+":
                            current_result = eval(str(current_result) + current_operator + str(
                                process_expression(expression[i + 1: index_of_close_parentheses])))
                        else:
                            current_result = eval(str(current_result) + current_operator + str(
                                process_expression(expression[i + 1: index_of_close_parentheses])))
                            current_result = eval(str(hold_left) + hold_operator + str(current_result))
                            hold_left = -1

                else:
                    current_result = process_expression(expression[i + 1: index_of_close_parentheses])
            i = index_of_close_parentheses + 1
        elif c == " ":
            i += 1
        elif c.isdecimal():
            if current_result == -1:  # first number in current expression
                current_result = int(c)
            else:
                if current_operator == "+":
                    if len(expression) > (i + 2) and expression[i + 2] == "+":
                        current_result = eval(str(current_result) + current_operator + str(c))
                    else:
                        if hold_left == -1:
                            current_result = eval(str(current_result) + current_operator + str(c))
                        else:
                            current_result = eval(str(current_result) + current_operator + str(c))
                            current_result = eval(str(hold_left) + hold_operator + str(current_result))
                            hold_left = -1
                elif len(expression) > (i + 2) and expression[i + 2] == "+":  # if next operator is +
                    hold_left = current_result
                    hold_operator = current_operator
                    current_result = int(c)  # current number
                else:
                    # current_operator is * and next is not +
                    if hold_left == -1:
                        current_result = eval(str(current_result) + current_operator + str(c))
                    else:
                        current_result = eval(str(current_result) + current_operator + str(c))
                        current_result = eval(str(hold_left) + hold_operator + str(current_result))
                        hold_left = -1
            i += 1
        else:  # c is operator
            current_operator = c
            i += 1

    return current_result


def find_index_of_close_parentheses(text: str):
    next_close = 1
    for i, c in enumerate(text):
        if c == "(":
            next_close += 1
        elif c == ")":
            if next_close == 1:
                return i
            else:
                next_close -= 1


with open("input.txt") as f:
    result = 0
    for line in f:
        line_res = process_expression(line.rstrip())
        result += line_res
    print(result)
