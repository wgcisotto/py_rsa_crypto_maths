def gcd(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# TODO: organize this explanation
# Euclid's algorithm can help find the multiplicative inverse in a modular arithmetic context. To solve for the multiplicative inverse of 342952340 modulo 4230493243, you can use the extended Euclidean algorithm. Here's a step-by-step explanation of the process:
#
# Apply the extended Euclidean algorithm to find the greatest common divisor (GCD) of 342952340 and 4230493243.
#
# The algorithm involves iteratively dividing the larger number by the smaller number and updating variables until the remainder becomes 0. Keep track of intermediate values during this process.
#
# You'll have something like:
# GCD(342952340, 4230493243) = 1 = 342952340 * x + 4230493243 * y
#
# The goal is to find 'x,' which is the multiplicative inverse of 342952340 modulo 4230493243.
#
# Once you've run the extended Euclidean algorithm, 'x' will be your multiplicative inverse.