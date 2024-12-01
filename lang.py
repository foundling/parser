def eval_expr(expr, line_no, names):

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
                try:
                    stack.append(names[token])
                except KeyError:
                    print(f"{line_no}: token not defined: {token}")
                    exit(1)
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
            names[name.strip()] = eval_expr(expr, pc, names)
        else:
            eval_expr(line_no, line, names)

        pc += 1

    print(names)
    

if __name__ == '__main__':

    f = [ 
         line for line
         in open('main.alex').readlines()
         if len(line.strip()) 
         and not line.strip().startswith('#') ]

    eval(f)
