import random
import math

from prime_utils.PrimeNumberUtils import PrimeNumberUtils


def generate_private_key(p1, p2):
    factors = factorize(p1)
    q, p = factors[0], factors[1]
    n = q * p

    e = p2
    inverse = mod_inverse(e, (q - 1) * (p - 1))

    public_key = (e, n)
    private_key = (inverse, n)

    return public_key, private_key


def generate_keypair():
    q = PrimeNumberUtils.generate_random_prime_number()
    p = PrimeNumberUtils.generate_random_prime_number()
    n = q * p

    e = random_select_relatively_prime((q - 1) * (p - 1))

    inverse = mod_inverse(e, (q - 1) * (p - 1))

    public_key = (e, n)
    private_key = (inverse, n)

    return public_key, private_key


def encrypt(publicKey, message):
    # Unpack the key
    e, n = publicKey
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    c = [(ord(char) ** e) % n for char in message]
    return c


def decrypt(privateKey, message):
    # Unpack the key
    d, n = privateKey
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    p = [chr((char ** d) % n) for char in message]
    # Return the array
    return ''.join(p)


def factorize(num):
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors


# TODO: This function could be improved by using a more efficient algorithm for finding a relatively prime number to
#  the given input.
def random_select_relatively_prime(phi):
    while True:
        e = random.randrange(2, phi)
        if math.gcd(e, phi) == 1:  # TODO: change here to use the function implemented before.
            return e


# TODO: this function could be improved by using a more efficient algorithm for finding the modular inverse of a number.
def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
        # Make x positive
    if (x < 0):
        x = x + m0

    return x


if __name__ == "__main__":
    p1 = 937513
    p2 = 638471

    public_key, private_key = generate_private_key(p1, p2)
    print("\nPublic key is (n={}, e={})".format(public_key[1], public_key[0]))
    print("Private key is", private_key)

    message = "public key already provided"
    ciphertext = encrypt(public_key, message)
    print("Encrypted message is:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message is:", decrypted_message)

    print("\nRandom Keys...")

    public_key, private_key = generate_keypair()
    print("\nPublic key is (n={}, e={})".format(public_key[1], public_key[0]))
    print("Private key is", private_key)

    message = "Random keys"
    ciphertext = encrypt(public_key, message)
    print("Encrypted message is:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message is:", decrypted_message)
