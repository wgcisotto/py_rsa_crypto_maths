import random
from decimal import Decimal


# Prime Numbers Checker Util Class
class PrimeNumberUtils:

    """
    A utility class for checking if a number is prime.
    """

    @staticmethod
    def is_prime_by_trial_error(n):
        """
        Checks if a number is prime using the trial division method.

        Args:
            n: The number to check.

        Returns:
            True if the number is prime, False otherwise.
        """

        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True

    @staticmethod
    def is_prime_by_miller_rabin(n):
        """
        Checks if a number is prime using the Miller-Rabin primality test.

        Args:
            n: The number to check.

        Returns:
            True if the number is prime, False otherwise.
        """

        return PrimeNumberUtils.is_prime(n)

    @staticmethod
    def is_prime(n, k=10):
        """
        Checks if a number is prime using the Miller-Rabin primality test with a given number of iterations.

        Args:
            n: The number to check.
            k: The number of iterations to use in the Miller-Rabin test.

        Returns:
            True if the number is prime, False otherwise.
        """

        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        d = n - 1
        while d % 2 == 0:
            d //= 2

        for i in range(k):
            if not PrimeNumberUtils.miller_test(d, n):
                return False

        return True

    @staticmethod
    def miller_test(d, n):
        """
        Performs a single iteration of the Miller-Rabin primality test.

        Args:
            d: The odd part of the number to be tested.
            n: The number to be tested.

        Returns:
            True if the number passes the Miller-Rabin test, False otherwise.
        """

        a = Decimal(random.randint(2, int(n) - 2))
        x = PrimeNumberUtils.power(a, d, n)

        if x == 1 or x == n - 1:
            return True

        while d != n - 1:
            x = (x * x) % n
            d *= 2

            if x == 1:
                return False

            if x == n - 1:
                return True

        return False

    @staticmethod
    def power(x, y, p):
        """
        Computes the modular exponentiation of a number.

        Args:
            x: The base.
            y: The exponent.
            p: The modulus.

        Returns:
            The result of the modular exponentiation.
        """

        res = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % p
            y = y // 2
            x = (x * x) % p
        return res

    @staticmethod
    def generate_random_prime_number():
        """
        Generates a random prime number.

        Returns:
            A random prime number.
        """

        # Generate a random number.
        random_number = random.randint(2, 1000)

        # Check if the number is prime.
        if PrimeNumberUtils.is_prime(random_number):
            return random_number
        else:
            # If the number is not prime, generate a new one.
            return PrimeNumberUtils.generate_random_prime_number()
