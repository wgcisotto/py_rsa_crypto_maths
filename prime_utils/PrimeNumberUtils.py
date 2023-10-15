from decimal import Decimal
import random

from decimal import Decimal, getcontext


# Prime Numbers Checker Util Class
class PrimeNumberUtils:

    @staticmethod
    def is_prime_by_trial_error(n):
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
        return PrimeNumberUtils.is_prime(n)

    @staticmethod
    def is_prime(n, k=10):
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
        res = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % p
            y = y // 2
            x = (x * x) % p
        return res