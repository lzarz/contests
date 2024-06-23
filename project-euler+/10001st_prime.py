#!/bin/python3

prime_numbers = [2, 3, 5, 7, 11, 13]
inputs = int(input().strip())

for i in range(inputs):
    n = int(input().strip())

    if len(prime_numbers) >= n:
        print(prime_numbers[n - 1])
    else:
        current = prime_numbers[-1] + 2
        while len(prime_numbers) < n:
            prime_flag = True
            sqrt_current = int(current ** 0.5)
            for prime in prime_numbers:
                if prime > sqrt_current:
                    break
                if current % prime == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_numbers.append(current)
            current += 2
        print(prime_numbers[n - 1])
