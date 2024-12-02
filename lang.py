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
            # try to resolve existing identifier
            if token.isalpha():
                if not token in names:
                    raise KeyError
                else:
                    stack.append(names[token])
            else:
                stack.append(int(token))

    return stack.pop()

def eval(lines, names={}):

    pc = 0

    while pc < len(lines):

        line = lines[pc].strip()

        # skip evaluation for blank lines and comments, but include in line count
        if not len(line.strip()) or line.strip().startswith('#'):
            pc += 1
            continue

        # TODO: re-think parsing an assignment, here you're treating it as an alternative
        # to evaluating an expression, but an assignment line has 'name =' then an expression.
        # try 

        # assignment line
        if len(line.split('=', maxsplit=1)) == 2:

            name, expr = [ segment.strip() for segment in line.split('=', maxsplit=1) ]

            try:
                names[name] = eval_expr(expr, names)
            except KeyError:
                print(f"{name} is undefined on line {pc + 1}")
                exit(1)
        else:
            if line.startswith('while'):

                while_start = pc
                while not lines[pc].startswith('end'):
                    pc += 1
                while_end = pc
                while_code_lines = lines[while_start + 1: while_end] 

                pc = while_start + 1
                while pc < while_end:

                    if len(lines[pc].split('=', maxsplit=1)) == 2:

                        name, expr = [ segment.strip() for segment in lines[pc].split('=', maxsplit=1) ]
                        try:
                            names[name] = eval_expr(expr, names)
                        except KeyError:
                            print(f"{name} is undefined on line {pc + 1}")
                            exit(1)
                    else:
                        try:
                            eval_expr(lines[pc], names)
                        except KeyError:
                            print(f"{line} is undefined on line {pc + 1}")

                    pc += 1



            '''
            try:
                eval_expr(line, names)
            except KeyError:
                print(f"{line} is undefined on line {pc + 1}")
            '''

        pc += 1

    print('names: ', names)


if __name__ == '__main__':

    src = open('main.alex').readlines()

    eval(src, {})
