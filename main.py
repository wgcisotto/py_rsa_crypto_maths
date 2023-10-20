import time

from composite_factor.CompositeFactors import pollards_rho, factorize
from euclid_algoritm.EuclidsAlgorithm import euclid_hcf
from prime_utils.PrimeNumberUtils import PrimeNumberUtils
from decimal import Decimal


def main():
    try:
        print('\nWelcome to RSA Algorithm Program')
        option = option_sel()
        match option:
            case "1":
                n = input('\nType the number: ')
                check_prime_number_trial_and_error(Decimal(n))
            case "2":
                n = input('\nType the number: ')
                if len(n) > 14:
                    print("Too big!! Please type a number up to 14 digits.")
                    return
                check_prime_number_miller_rabin(Decimal(n))
            case "3":
                n = input('\nType the number: ')
                deterministic_factors_of(Decimal(n))
            case "4":
                n = input('\nType the number: ')
                probabilistic_factors_of(Decimal(n))
            case "5":
                a = input('\nType the number One: ')
                b = input('\nType the number Two: ')
                hcf(Decimal(a), Decimal(b))
            case _:
                print('Ops! Looks like you typed an incorrect option')
    except KeyboardInterrupt:
        print('\nShutdown...')


def check_prime_number_trial_and_error(n):
    # Record the start time
    start_time = time.time()
    is_prime = PrimeNumberUtils.is_prime_by_trial_error(n)
    if is_prime:
        print(f"\n{n} is prime.")
    else:
        print(f"\n{n} is not prime.")
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    print(f"\nTime taken to calculate the primality was: {elapsed_time:.6f} seconds")


def check_prime_number_miller_rabin(n):
    # Record the start time
    start_time = time.time()
    is_prime = PrimeNumberUtils.is_prime_by_miller_rabin(n)
    if is_prime:
        print(f"\n{n} is probably prime.")
    else:
        print(f"\n{n} is not prime.")
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    print(f"\nTime taken to calculate the primality was: {elapsed_time:.10f} seconds")
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    print(f"\nTime taken to calculate the primality was: {elapsed_time:.6f} seconds")


def deterministic_factors_of(n):
    # Record the start time
    start_time = time.time()
    factors = factorize(n)
    print(f"Factors of {n}: {factors}")
    # Record the end time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTime taken to find the composite factors was: {elapsed_time:.6f} seconds")


def probabilistic_factors_of(n):
    # Record the start time
    start_time = time.time()
    factors = pollards_rho(n)
    print(f"Factors of {n}: {factors}")
    # Record the end time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTime taken to find the composite factors was: {elapsed_time:.6f} seconds")


def hcf(a, b):
    # Record the start time
    # perf_counter provides more accurate timing measurements for very short computations.
    start_time = time.perf_counter()
    result = euclid_hcf(a, b)
    print(f"HCF of {a} and {b}: {result}")
    # Record the end time
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\nTime taken to compute was: {elapsed_time:.6f} milliseconds")


def option_sel():
    print('\n(1) - Check prime number by Trial and Error. (Deterministic)')
    print('(2) - Check prime number by Miller-Rabin. (Probabilistic)')
    print('(3) - Factorisation of composite number. (Deterministic)')
    print('(4) - Factorisation of composite number by  Pollard`s Rho algorithm. (Probabilistic)')
    print('(5) - highest common factor (HCF) - Euclid`s Algorithm ')
    option = input('\nChoose one option: ')
    try:
        if int(option) < 1 or int(option) > 5:
            return invalid_sel()
    except ValueError:
        return invalid_sel()
    return option


def invalid_sel():
    print('\nInvalid option selected, try again!')
    return option_sel()


if __name__ == '__main__':
    main()
