def toPostfix(tokens:list):
    output = []
    operators = []
    for token in tokens:
        if token['type'] == 'op':
            while len(operators) > 0 and operators[len(operators)-1]['precedence'] < token['precedence']:
                top = operators.pop()
                if top['type'] == 'op':output.append(top)
            operators.append(token)

        if token['type'] == 'par':
            if token['val'] == '(': operators.append(token)
            elif token['val'] == ')':
                while len(operators) > 0 and operators[len(operators)-1]['precedence'] < token['precedence']:
                    top = operators.pop()
                    if top['type'] == 'op':output.append(top)
                operators.pop()

        if token['type'] == 'num':
            output.append(token)
    
    while len(operators) > 0:
        output.append(operators.pop())

    return output

# 2 * 3 + 1  ==> 2 3 * 1 +
# 1 + 2 * 3  ==> 1 2 3 * +