import time
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
                print("NOT DEFINED YET")
            case _:
                print('Ops! Looks like you typed an incorrect option')
    except KeyboardInterrupt:
        print('\nShutdown...')


def check_prime_number_trial_and_error(n):
    # Record the start time
    start_time = time.time()
    print(PrimeNumberUtils.is_prime_by_trial_error(n))
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    print(f"Time taken to calculate the primality was: {elapsed_time:.6f} seconds")


def check_prime_number_miller_rabin(n):
    # Record the start time
    start_time = time.time()
    is_prime = PrimeNumberUtils.is_prime_by_miller_rabin(n)
    if is_prime:
        print(f"{n} is probably prime.")
    else:
        print(f"{n} is not prime.")
    # Record the end time
    end_time = time.time()
    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time
    print(f"Time taken to calculate the primality was: {elapsed_time:.6f} seconds")


def option_sel():
    print('\n(1) - Check prime number by Trial and Error')
    print('(2) - Check prime number by  Miller-Rabin')
    print('(3) - NOT DEFINED')
    option = input('\nChoose one option: ')
    try:
        if int(option) < 1 or int(option) > 3:
            return invalid_sel()
    except ValueError:
        return invalid_sel()
    return option


def invalid_sel():
    print('\nInvalid option selected, try again!')
    return option_sel()


if __name__ == '__main__':
    main()
