from euclid_algoritm.EuclidsAlgorithm import gcd
import math


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
def factorize(num):
    """
    Factorize a number into its prime factors.

    Args:
        num (int): The number to factorize.

    Returns:
        list: A list of prime factors.
    """
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors
