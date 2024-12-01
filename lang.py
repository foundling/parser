def eval_exp(line):

    stack = []
    tokens = line.strip().split()

    for token in tokens:

        if token == '-':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(lhs - rhs)

        elif token == '+':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(lhs + rhs)

        elif token == '/':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(lhs / rhs)

        elif token == '*':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(lhs * rhs)

        else:
            stack.append(int(token))

    return stack.pop()

def eval(lines):

    pc = 0

    while pc < len(lines):

        line = lines[pc]
        v = eval_exp(line)

        pc += 1

if __name__ == '__main__':
    f = [ line for line in open('main.alex').readlines() if line.strip() ]
    eval(f)
