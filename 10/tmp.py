def a(b):
    b.pop()
    b = [3]

def main():
    b = [4]
    a(b)
    print(b)

main()
