from euclid_algoritm.EuclidsAlgorithm import gcd
import math


def pollards_rho(n):
    """
    Factorizes a positive integer 'n' using Pollard's Rho algorithm.

    This function attempts to find the prime factors of 'n' by iteratively applying Pollard's Rho algorithm,
    which is a probabilistic algorithm for integer factorization. It is particularly efficient for
    factoring large composite numbers.

    Parameters:
    n (int): The positive integer to be factorized.

    Returns:
    List[int]: A list of prime factors of 'n' in ascending order.

    Example:
    >>> pollards_rho(35)
    [5, 7]
    >>> pollards_rho(143)
    [11, 13]
    >>> pollards_rho(19)
    [19]

    Note:
    - The function may return the factors in an arbitrary order.
    - If 'n' is a prime number, the function will return the prime number itself in a list.

    Reference:
    - Pollard, J. M. (1975). "A Monte Carlo method for factorization". BIT Numerical Mathematics, 15(3), 331-334.
    """
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
    Factorizes a positive integer 'num' into its prime factors.

    This function decomposes a positive integer 'num' into its prime factors and returns them in a list.
    It uses a simple trial division method to find the prime factors.

    Args:
        num (int): The number to factorize.

    Returns:
        list: A list of prime factors in ascending order.

    Example:
    >>> factorize(12)
    [2, 2, 3]
    >>> factorize(35)
    [5, 7]
    >>> factorize(143)
    [11, 13]
    >>> factorize(19)
    [19]

    Note:
    - The function may return the prime factors in ascending order.
    - If 'num' is a prime number, the function will return the prime number itself in a list.

    Reference:
    - No specific reference. This is a basic trial division method for factorization.
    """
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors