import time

from composite_factor.CompositeFactors import pollards_rho, factorize
from euclid_algoritm.EuclidsAlgorithm import gcd, extended_gcd
from prime_utils.PrimeNumberUtils import PrimeNumberUtils
from decimal import Decimal

from rsa.rsa import encrypt, decrypt, generate_private_key


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
            case "6":
                a = input('\nType the number A (Integer): ')
                b = input('\nType the number B (Modulo): ')
                find_multiplicative_inverse(Decimal(a), Decimal(b))
            case "7":
                print('\nType the Public key numbers')
                n = int(input('\nType the number (n): '))
                e = int(input('Type the number(e): '))
                message = input('\nType the message (m): ')
                rsa_encryptor(n, e, message)
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


def deterministic_factors_of(n):
    # Record the start time
    start_time = time.perf_counter()
    factors = factorize(n)
    print(f"\nFactors of {n}: {factors}")
    # Record the end time
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\nTime taken to compute was: {elapsed_time:.6f} milliseconds")


def probabilistic_factors_of(n):
    # Record the start time
    start_time = time.perf_counter()
    factors = pollards_rho(n)
    print(f"\nFactors of {n}: {factors}")
    # Record the end time
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\nTime taken to compute was: {elapsed_time:.6f} milliseconds")


def hcf(a, b):
    # Record the start time
    # perf_counter provides more accurate timing measurements for very short computations.
    start_time = time.perf_counter()
    result = gcd(a, b)
    print(f"\nHCF of {a} and {b}: {result}")
    # Record the end time
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    print(f"\nTime taken to compute was: {elapsed_time:.6f} milliseconds")


def find_multiplicative_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        print("\nNo multiplicative inverse exists.")
    else:
        # Ensure x is positive and within the modulo m
        x = (x % m + m) % m
        print(f"\nThe multiplicative inverse of {a} modulo {m} is {x}.")


def rsa_encryptor(n, e, message):
    public_key, private_key = generate_private_key(n, e)
    print("\nPublic key is (n={}, e={})".format(public_key[1], public_key[0]))
    print("Private key is", private_key)
    ciphertext = encrypt(public_key, message)
    print("\nEncrypted message is:", ciphertext)
    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message is:", decrypted_message)
    if decrypted_message == message:
        print("\nIt worked!")


def option_sel():
    print('\n(1) - Check if a number is prime using Trial and Error (Deterministic)')
    print('(2) - Check if a number is prime using the Miller-Rabin algorithm (Probabilistic)')
    print('(3) - Factor a composite number into its prime factors (Deterministic)')
    print('(4) - Factor a composite number using Pollard`s Rho algorithm (Probabilistic)')
    print('(5) - Find the highest common factor (HCF) using Euclid`s Algorithm')
    print('(6) - Solve for x in a linear congruence Ax ≡ 1 (mod B)')
    print('(7) - Perform RSA Encryption and Decryption')

    option = input('\nChoose one option: ')
    try:
        if int(option) < 1 or int(option) > 7:
            return invalid_sel()
    except ValueError:
        return invalid_sel()
    return option


def invalid_sel():
    print('\nInvalid option selected, try again!')
    return option_sel()


if __name__ == '__main__':
    main()
