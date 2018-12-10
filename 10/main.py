import math
def consume(c, stack):
    if c == " ":
        stack.append(31)
    elif c == ":":
        s = sum(stack)
        stack = [s]
    elif c == "|":
        stack.append(3)
    elif c == "'":
        s1 = stack.pop()
        s2 = stack.pop()
        stack.append(s1 + s2)
    elif c == ".":
        A = stack.pop()
        B = stack.pop()
        stack.append(A-B)
        stack.append(B-A)
    elif c == "_":
        A = stack.pop()
        B = stack.pop()
        stack.append(A*B)
        stack.append(A)
    elif c == "/":
        stack.pop()
    elif c == "i":
        stack.append(stack[-1])
    elif c == "\\":
        A = stack.pop()
        stack.append(A + 1)
    elif c == "*":
        A = stack.pop()
        B = stack.pop()
        stack.append(math.floor(A/B))
    elif c == "]":
        if stack.pop() % 2 == 0:
            stack.append(1)
    elif c == "[":
        if stack.pop() % 2 == 1:
            stack.append(1)
    elif c == "~":
        A = stack.pop()
        B = stack.pop()
        C = stack.pop()
        stack.append(max(A, max(B,C)))
    else:
        print("ERROR", c)
    return stack

def main():
    stack = []
    with open("./input.spp") as f:
        for line in f.read().split("\n"):
            for c in line:
                if c == "K":
                    break
                else:
                    stack = consume(c, stack)

    print(stack)
main()
