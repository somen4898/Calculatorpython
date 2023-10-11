import re


def is_valid_expression(exp):
    return (exp.count("(") == exp.count(")")) and re.match(r'^[0-9+\-*/() ]*$', exp)


def tokenize(exp):
    tokens = []
    start = 0
    prev_operator = None  # Variable to store the previous operator
    for i, c in enumerate(exp):
        if c in '+-/*()':
            token_value = exp[start:i].strip()
            if token_value:
                tokens.append(token_value)
            # Check if the current operator is the same as the previous one
            if c == prev_operator:
                pass  # Skip consecutive operators of the same type
            else:
                tokens.append(c)
                prev_operator = c  # Update the previous operator
            start = i + 1
    token_value = exp[start:].strip()
    if token_value:
        tokens.append(token_value)
    return [t for t in tokens if t != ""]



def evaluate_parentheses(tokens):
    stack = []
    for i, token in enumerate(tokens):
        if token == "(":
            stack.append(i)
        elif token == ")":
            start_index = stack.pop()
            result_inside_parentheses = calculate(tokens[start_index + 1:i])
            result_tokens = [t for t in result_inside_parentheses if t != ""]
            tokens = tokens[:start_index] + result_tokens + tokens[i + 1:]
            return evaluate_parentheses(tokens)
    return tokens


def multiply_and_divide(tokens):
    new_token = []
    skip_token = False
    for i, token in enumerate(tokens):
        if skip_token:
            skip_token = False
            continue
        if token == "*":
            new_token.append(float(new_token.pop()) * float(tokens[i + 1]))
            skip_token = True
        elif token == "/":
            if float(tokens[i + 1]) == 0:
                return None
            else:
                new_token.append(float(new_token.pop()) / float(tokens[i + 1]))
                skip_token = True
        else:
            new_token.append(token)
    return new_token


def add_and_sub(tokens):
    new_token = []
    skip_token = False
    for i, token in enumerate(tokens):
        if skip_token:
            skip_token = False
            continue
        if token == '+':
            new_token.append(float(new_token.pop()) + float(tokens[i + 1]))
            skip_token = True
        elif token == "-":
            new_token.append(float(new_token.pop()) - float(tokens[i + 1]))
            skip_token = True
        else:
            new_token.append(token)
    return new_token


def calculate(tokens):
    tokens = evaluate_parentheses(tokens)
    tokens = multiply_and_divide(tokens)
    if tokens is None:
        print("Value divided by zero is invalid. NAN")
        return
    tokens = add_and_sub(tokens)
    return tokens


while True:
    exp = input("Enter string with operands +,-,*,/ or type 'stop' to stop: \n")
    if exp.lower() == 'stop':
        break
    if is_valid_expression(exp):
        tokens = tokenize(exp)
        answer = calculate(tokens)
        print(answer)
    else:
        print("NAN")