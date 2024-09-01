from collections import deque
from bisect import bisect_left as bis

def primos(n):

    prime = [True] * n
    prime[0] = prime[1] = False

    # Iterate from 2 to sqrt(n)
    for p in range(2, int(n ** 0.5) + 1):
        # If p is a prime, mark as composite all the multiples of p
        if prime[p]:
            for i in range(p * p, n, p):
                prime[i] = False

    # Create a set of prime numbers
    prime_set = {p for p in range(2, n) if prime[p]}

    return prime_set

def encode(a, b):
    org = sorted([a, b])
    return str(org[0]) + "-" + str(org[-1])

grand = 0
nums = deque()

for _ in range(int(input())):
    x = int(input())
    grand = max(x, grand)
    nums.append(x)

primos = primos(grand)

def nms(n):
    global primos
    cont = 0
    dict = set()

    for i in primos:
        complemento = n-i
        if complemento in primos and complemento < n:
            if (encode(i, complemento) not in dict) :
                cont += 1
                dict.add(encode(i, complemento))


    return cont



for i in nums:
    print(nms(i))