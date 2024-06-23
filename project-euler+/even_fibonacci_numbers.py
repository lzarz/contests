#!/bin/python3

inputs = int(input().strip())

for i in range(inputs):
    n = int(input().strip())

    a, b = 1, 2
    sum_even = 0

    while a <= n:

        if a % 2 == 0:
            sum_even += a

        a, b = b, a + b

    print(sum_even)
