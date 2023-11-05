from euclid_algoritm.EuclidsAlgorithm import gcd


def is_coprime(a, b):
    # Check if 'a' and 'b' are relatively prime
    return gcd(a, b) == 1  # Return True if the gcd of a and b is 1, indicating that they are relatively prime


def mod_inverse(a, m):
    # Calculate the modular multiplicative inverse of 'a' modulo 'm'
    for x in range(1, m):  # Iterate through all possible values of x from 1 to m - 1
        if (a * x) % m == 1:  # Check if (a * x) % m is equal to 1
            return x  # If so, return x as the modular multiplicative inverse
    return None  # If no modular multiplicative inverse is found, return None

# Prints a transposition table for an affine cipher.

def encrypt(a: int, b: int, s: str):
    import string
    print('Starting encryption!')
    D = dict(enumerate(string.ascii_lowercase, start=0))  # Create a dictionary mapping lowercase letters to their corresponding indices
    E = {v: k for k,v in D.items()}  # Create a dictionary mapping indices to their corresponding lowercase letters
    print(D)
    print(E)
    size = len(string.ascii_lowercase)  # Get the size of the alphabet (26)
    ret = ""  # Initialize an empty string to store the encrypted text
    print(size)
    for c in s:  # Iterate through each character in the plaintext string
        N = E[c]  # Get the index of the current character
        val = a * N + b  # Calculate the encrypted value
        val = val % size  # Modulo the encrypted value by the alphabet size to keep it within the range of 0 to 25
        print(f"{c}({N}) -> {D[val]}({val})")  # Print the mapping between the plaintext character and its encrypted counterpart
        ret += D[val]  # Append the encrypted character to the encrypted text string
    return ret  # Return the encrypted text string


def decrypt(a: int, b: int, s: str):
    import string
    print('Starting decryption!')
    D = dict(enumerate(string.ascii_lowercase, start=0))  # Create a dictionary mapping lowercase letters to their corresponding indices
    E = {v: k for k,v in D.items()}  # Create a dictionary mapping indices to their corresponding lowercase letters
    size = len(string.ascii_lowercase)  # Get the size of the alphabet (26)
    ret = ""  # Initialize an empty string to store the decrypted text
    print(size)
    for c in s:  # Iterate through each character in the ciphertext string
        N = E[c]  # Get the index of the current character
        val = mod_inverse(a, size) * (N - b)  # Calculate the decrypted value using the modular multiplicative inverse
        val = val % size  # Modulo the decrypted value by the alphabet size to keep it within the range of 0 to 25
        print(f"{c}({N}) -> {D[val]}({val})")  # Print the mapping between the ciphertext character and its decrypted counterpart
        ret += D[val]  # Append the decrypted character to the decrypted text string
    return ret  # Return the decrypted text string


if __name__ == "__main__":
    # Example usage:
    a = 5  # Replace with your choice of 'a' (must be relatively prime to 26)
    b = 8  # Replace with your choice of 'b'

    plain_text = "affinecipher"
    encrypted_text = encrypt(a, b, plain_text)
    decrypted_text = decrypt(a, b, encrypted_text)

    print("Original text: ", plain_text)
    print("Encrypted text: ", encrypted_text)
    print("Decrypted text: ", decrypted_text)

