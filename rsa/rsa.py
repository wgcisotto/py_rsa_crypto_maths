import random
import math

from prime_utils.PrimeNumberUtils import PrimeNumberUtils


def generate_private_key(n, e):
    """
    Generate a private key from given values.

    Args:
        n (int): Modulus for the RSA key pair.
        e (int): Public exponent (usually referred to as 'e').

    Returns:
        tuple: A tuple containing the public key (e, n) and private key (d, n).
    """
    factors = factorize(n)
    q, p = factors[0], factors[1]

    d = mod_inverse(e, (q - 1) * (p - 1))

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def generate_keypair():
    """
    Generate a key pair with random prime numbers.

    Returns:
        tuple: A tuple containing the public key (e, n) and private key (d, n).
    """
    q = PrimeNumberUtils.generate_random_prime_number()
    p = PrimeNumberUtils.generate_random_prime_number()
    n = q * p

    e = random_select_relatively_prime((q - 1) * (p - 1))

    inverse = mod_inverse(e, (q - 1) * (p - 1))

    public_key = (e, n)
    private_key = (inverse, n)

    return public_key, private_key


def encrypt(publicKey, message):
    """
    Encrypt a message using a public key.

    Args:
        publicKey (tuple): A tuple containing the public key (e, n).
        message (str): The message to be encrypted.

    Returns:
        list: A list of encrypted characters.
    """
    # Unpack the key
    e, n = publicKey
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    c = [(ord(char) ** e) % n for char in message]
    return c


def decrypt(privateKey, message):
    """
    Decrypt a message using a private key.

    Args:
        privateKey (tuple): A tuple containing the private key (d, n).
        message (list): A list of encrypted characters.

    Returns:
        str: The decrypted message.
    """
    # Unpack the key
    d, n = privateKey
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    p = [chr((char ** d) % n) for char in message]
    # Return the array as a string
    return ''.join(p)


def factorize(num):
    """
    Factorize a number into its prime factors.

    Args:
        num (int): The number to factorize.

    Returns:
        list: A list of prime factors.
    """
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors


def random_select_relatively_prime(phi):
    """
    Select a random number that is relatively prime to the given input.

    Args:
        phi (int): The input value.

    Returns:
        int: A randomly selected number that is relatively prime to phi.
    """
    while True:
        e = random.randrange(2, phi)
        if math.gcd(e, phi) == 1:
            return e


def mod_inverse(a, m):
    """
    Calculate the modular inverse of a number.

    Args:
        a (int): The number for which the modular inverse is calculated.
        m (int): The modulus.

    Returns:
        int: The modular inverse of a with respect to m.
    """
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
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
    if x < 0:
        x = x + m0

    return x


if __name__ == "__main__":
    p1 = 937513
    p2 = 638471

    public_key, private_key = generate_private_key(p1, p2)
    print("\nPublic key is (n={}, e={})".format(public_key[1], public_key[0]))
    print("Private key is (n={}, d={})".format(private_key[1], private_key[0]))

    message = "public key already provided"
    ciphertext = encrypt(public_key, message)
    print("Encrypted message is:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message is:", decrypted_message)

    print("\nRandom Keys...")

    public_key, private_key = generate_keypair()
    print("\nPublic key is (n={}, e={})".format(public_key[1], public_key[0]))
    print("Private key is (n={}, d={})".format(private_key[1], private_key[0]))

    message = "Random keys"
    ciphertext = encrypt(public_key, message)
    print("Encrypted message is:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message is:", decrypted_message)
