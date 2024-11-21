import tokenize as t
import evaluate as e

if __name__ == '__main__':
    line = input() 
    tokens = t.scan(line)
    e.evaluate(tokens)