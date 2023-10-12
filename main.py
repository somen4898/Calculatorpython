import re


def has_invalid_combinations(expression):
    invalid_combinations = ['-+', '*+', '/+', '-/', '*/', '+/', '-*', '+*', '/*']
    for combination in invalid_combinations:
        if combination in expression:
            return True
    return False


def clean_expression(expression):
    # Use regular expression to remove consecutive / and - operators
    cleaned_expression = re.sub(r'([/])\1+', r'\1', expression)
    cleaned_expression = re.sub(r'([-])\1+', r'\1', cleaned_expression)
    cleaned_expression = re.sub(r'([*])\1+', r'\1', cleaned_expression)
    cleaned_expression = re.sub(r'([+])\1+', r'\1', cleaned_expression)
    while has_invalid_combinations(cleaned_expression):
        cleaned_expression = re.sub(r'\*\+', '+', cleaned_expression)
        cleaned_expression = re.sub(r'\/\+', '+', cleaned_expression)
        cleaned_expression = re.sub(r'-\+', '+', cleaned_expression)
        cleaned_expression = re.sub(r'\/\*', '*', cleaned_expression)
        cleaned_expression = re.sub(r'\+\*', '*', cleaned_expression)
        cleaned_expression = re.sub(r'\-\*', '*', cleaned_expression)
        cleaned_expression = re.sub(r'\+\/', '/', cleaned_expression)
        cleaned_expression = re.sub(r'\-\/', '/', cleaned_expression)
        cleaned_expression = re.sub(r'\*\/', '/', cleaned_expression)

    return cleaned_expression


def calculate(expression):
    try:
        cleaned_expression = clean_expression(expression)
        # Evaluate the cleaned expression and return the result
        result = eval(cleaned_expression)
        return result
    except Exception as e:
        return str(e)


while True:
    expression = input("Enter an expression (or 'stop' to exit):\n")
    if expression == "stop":
        break
    result = calculate(expression)
    print(result)
