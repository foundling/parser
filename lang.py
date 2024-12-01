def eval(lines):

    pc = 0

    while pc < len(lines):

        stack = []
        tokens = lines[pc].strip().split()

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

        print(stack.pop())
        pc += 1

f = [ line for line in open('main.alex').readlines() if line.strip() ]

eval(f)
