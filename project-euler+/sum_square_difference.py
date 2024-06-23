#!/bin/python3

inputs = int(input().strip())

for i in range(inputs):
    n = int(input().strip())

    S = n * (n + 1) // 2
    sum_squared = S * S
    squared = n * (n + 1) * (2 * n + 1) // 6
    difference = sum_squared - squared

    print(difference)
