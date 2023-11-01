def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

    This function computes the GCD of two integers 'a' and 'b' using Euclid's algorithm, which is an efficient
    method for finding the largest positive integer that divides both 'a' and 'b'.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of 'a' and 'b'.

    Example:
    >>> gcd(12, 18)
    6
    >>> gcd(35, 49)
    7
    >>> gcd(21, 28)
    7

    Reference:
    - Euclid's algorithm: Euclid of Alexandria, a Greek mathematician (circa 300 BCE), described this method for
    finding the GCD in his work "Elements."
    """
    # Calculate the GCD using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    """
    Calculate the extended greatest common divisor (GCD) and Bézout coefficients for two numbers using the extended Euclidean algorithm.

    This function computes the extended GCD of two integers 'a' and 'b' using the extended Euclidean algorithm.
    It not only finds the GCD but also provides Bézout coefficients 'x' and 'y' such that 'ax + by = gcd(a, b)'.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        Tuple[int, int, int]: A tuple containing the GCD of 'a' and 'b' as the first element,
        Bézout coefficient 'x' as the second element, and Bézout coefficient 'y' as the third element.

    Example:
    >>> extended_gcd(12, 18)
    (6, -1, 1)
    >>> extended_gcd(35, 49)
    (7, 1, -1)
    >>> extended_gcd(21, 28)
    (7, -1, 1)

    Reference:
    - Extended Euclidean algorithm: This algorithm is an extension of Euclid's algorithm and is used to find the GCD and Bézout coefficients.
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
