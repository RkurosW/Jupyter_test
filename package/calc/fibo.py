def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    # fib(int(sys.argv[1]))
    # print(fib2(int(sys.argv[1])))
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    fib(num)
    print(fib2(num))