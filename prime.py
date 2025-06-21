"""
prime.py -- Write the application code here
"""

def generate_prime_factors(x):
    if not isinstance(x, int):
        raise ValueError
    from math import sqrt
    prime_factor = []
    limit = int(sqrt(x)) + 1
    check = 2
    num = x
    if x == 0 or x == 1: return ' '
    for check in range(2, limit):
        while num % check == 0:
            prime_factor.append(check)
            num /= check
    if num > 1:
        prime_factor.append(int(num))
    return prime_factor

print(generate_prime_factors(6))

