#!/bin/python3

inputs = int(input().strip())

for i in range(inputs):
    n = int(input().strip())

    a = (n - 1) // 3
    b = (n - 1) // 5
    c = (n - 1) // 15

    sum_3 = 3 * a * (a + 1) // 2
    sum_5 = 5 * b * (b + 1) // 2
    sum_15 = 15 * c * (c + 1) // 2

    result = sum_3 + sum_5 - sum_15
    print(result)
