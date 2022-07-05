import  sys

def factorial(n):
    b = 1
    for i in range(n):
        b *= i+1
    return b

T = int(sys.stdin.readline())
for j in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(factorial(M) // (factorial(N) * factorial(M - N)))