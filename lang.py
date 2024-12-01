def eval_expr(expr, names={}):

    stack = []
    tokens = expr.strip().split()

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
            if token.isalpha():
                if not token in names:
                    raise KeyError
                else:
                    stack.append(names[token])
            else:
                stack.append(int(token))

    return stack.pop()

def eval(lines):

    pc = 0
    names = {}

    while pc < len(lines):

        line = lines[pc]

        if len(line.split('=', maxsplit=1)) == 2:

            name, expr = line.split('=', maxsplit=1)
            try:
                names[name.strip()] = eval_expr(expr, names) 
            except KeyError:
                print(f"{name.strip()} is undefined on line {pc}")
                exit(1)
        else:
            eval_expr(line, names)

        pc += 1

    print(names)
    

if __name__ == '__main__':

    f = [ 
         line for line
         in open('main.alex').readlines()
         if len(line.strip()) 
         and not line.strip().startswith('#') ]

    eval(f)
