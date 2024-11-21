# evaluation for postfix operations

stack = []
error = False

def operate(x):
    operations = {
        '+': lambda a,b: a+b,  
        '-': lambda a,b: a-b,  
        '*': lambda a,b: a*b,  
        '/': lambda a,b: a/b,  
    }
    if not x in operations : 
        global error
        error = True
        return
    b = stack.pop() 
    a = stack.pop()

    stack.append(operations[x](a,b))

def evaluate(instructions: list):
    for instruction in instructions:
       if (instruction["type"] == 'num'): stack.append(int(instruction["val"])) 
       else: operate(instruction["val"])

    print(stack[0])
