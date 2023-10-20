import random


def gcd(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    while b:
        a, b = b, a % b
    return a


def pollards_rho(n):
    if n <= 1:
        return [n]

    # Define the pollard's rho function
    def rho(x, c):
        # The rho function takes a value x and a random constant c and returns a new value modulo n.
        return (x ** 2 + c) % n

    x, y, d = 2, 2, 1

    while d == 1:
        # Generate x and y values using the rho function
        x = rho(x, 1)
        y = rho(rho(y, 1), 1)

        # Calculate the GCD of the absolute difference between x and y and the original number n
        d = gcd(abs(x - y), n)

    if d == n:
        # If no factor is found, return the number itself
        return [n]

    # Recursively factor the divisors
    factors = pollards_rho(d) + pollards_rho(n // d)
    return factors


# Deterministic approach
def factorize(n):
    factors = []
    div = 2  # Start with the smallest prime factor, which is 2

    while n > 1:
        while n % div == 0:
            factors.append(div)
            n //= div
        div += 1

    return factors
