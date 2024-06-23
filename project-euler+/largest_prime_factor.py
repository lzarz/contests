#!/bin/python3

import math

inputs = int(input().strip())

for i in range(inputs):
    n = int(input().strip())

    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i

    if n > 2:
        max_prime = n

    print(max_prime)
