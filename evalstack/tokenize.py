# tokenize valid expressions

error = False

def isNumber(x):
    return 48 < ord(x)  < 57

def scan(source: str):
    tokens = []
    num = ''
    for c in source:
        operators = {'+', '-', '*', '/'}
        if isNumber(c):
            num+=c
            continue

        if num!= '':
            tokens.append({
                "type":"num",
                "val": num
            })
            num = ''

        if c in operators:
            tokens.append({
                "type": 'op',
                "val": c 
            })
            continue

        if c == ' ' or c == '\n': continue

        print("Unexpected token " + c)
        error = True
    if num != '':
        tokens.append(num)
    return tokens

