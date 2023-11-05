from euclid_algoritm.EuclidsAlgorithm import gcd


def phi(n):
    """
    Calculate Euler's Totient function (phi) for a positive integer 'n'.

    Euler's Totient function, denoted as φ(n), calculates the count of positive integers less than 'n' that are
    coprime (relatively prime) to 'n'. In other words, it finds the number of positive integers less than 'n' that
    do not share any common factors with 'n'.

    Args:
        n (int): The positive integer for which Euler's Totient function is to be calculated.

    Returns:
        int: The value of φ(n) for the given integer 'n'.

    Example:
    >>> phi(12)
    4
    >>> phi(35)
    24
    >>> phi(19)
    18

    Reference:
    - Euler's Totient function: Named after the Swiss mathematician Leonhard Euler, Euler's Totient function
    is an important concept in number theory and is used in various mathematical and cryptographic applications.
    """
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            print(i, " - Is relatively prime to ", 26)
            result += 1
    return result


if __name__ == "__main__":
    n = 26
    print("φ(", n, ") = phi(", n, ") = ", phi(n))
