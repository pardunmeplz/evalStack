import tokenize as t
import evaluate as e
import conversion as c

if __name__ == '__main__':
    line = input() 
    tokens = t.scan(line)
    instructions = c.toPostfix(tokens)
    e.evaluate(instructions)