# The RSA Algorithm

## Content

* [Introduction](#Introduction)
  * [Executing the program](#Using-the-program)
* [Exercises](#Exercises)
  * [Exercise 1](#Exercise-1)
    * [Solution 1](#Solution-1)
  * [Exercise 2](#Exercise-2)
    * [Solution 2](#Solution-2)
  * [Exercise 3](#Exercise-3)
    * [Solution 3](#Solution-3)
  * [Exercise 4](#Exercise-4)
    * [Solution 4](#Solution-4)
      * [a) hcf(499017086208, 676126714752)]()
      * [b) hcf(5988737349, 578354589)]()
  * [Exercise 5](#Exercise-5)
    * [Solution 5](#Solution-5)
  * [Exercise 6](#Exercise-6)
    * [Solution 6](#Solution-6)
  * [Exercise 7](#Exercise-7)
    * [Solution 7](#Solution-7)

## Introduction

The RSA algorithm belongs to the family of public key encryption algorithms and stands for Ron Rivest, Adi Shamir and Leonard Adleman, who first publicly described it in 1978. 
A user of RSA creates and then publishes the product of two large prime numbers, along with an auxiliary value, as their public key. 
The prime factors must be kept secret. Anyone can use the public key to encrypt a message, but with currently published methods, if the public key is large enough, only someone with knowledge of the prime factors can feasibly
decode the message. This construction improves upon the complexity introduced in case of using symmetric encryption algorithms as the parties that wish to communicate have to share a
priori the public keys. This complexity of key management grows quadratic in terms of the number of participants in a network.

In the RSA system, encryption works as follows.

a) Choose two large primes p and q and compute n = pq.

b) Choose a number e < n which is co-prime to φ(n) = (p−1)(q−1).

c) Find a number d such that ed ≡ 1 (mod φ(n)).

Then, the public key is the pair (n, e) and the private key is (n, d). 

A message m sent to a person would be encrypted as c = me (mod n). The individual for whom the message was intended would decrypt c as m = cd (mod n).

The RSA algorithm works because it is feasible for a user to find a couple of 100-digit numbers which are almost certainly prime, 
but it is thought to be impossible to factorize a 200-digit number in a reasonable time. 
Factorization of n would enable an enemy to find d from e in just the same way that the user did. 
There are other possible attacks, but they appear to be (though are not proved to be) as difficult as factorization.

### Using the program

#### Requirements 

requires Python 3.10 or a compatible version. 

#### To start 

run:

```shell
python main.py 
```

Then:

````
Welcome to RSA Algorithm Program

(1) - Check if a number is prime using Trial and Error (Deterministic)
(2) - Check if a number is prime using the Miller-Rabin algorithm (Probabilistic)
(3) - Factor a composite number into its prime factors (Deterministic)
(4) - Factor a composite number using Pollard`s Rho algorithm (Probabilistic)
(5) - Find the highest common factor (HCF) using Euclid`s Algorithm
(6) - Solve for x in a linear congruence Ax ≡ 1 (mod B)
(7) - Perform RSA Encryption and Decryption
````

# Exercises

## Exercise 1

A number p is defined as prime if and only if it is divisible by itself (and 1). Implement a method
from scratch that allows to test primality of a number using trial and error method.

### Solution 1

In this solution, I employ a primality test that relies on trial and error. 
This method follows a deterministic approach, but it's notably slower when dealing with large numbers compared to other more efficient methods.  

See: [Prime Number Utils](prime_utils/PrimeNumberUtils.py#L11) 

> Select option 1

````
(1) - Check if a number is prime using Trial and Error (Deterministic)

Choose one option: 1

Type the number: 68340297256331

68340297256331 is prime.

Time taken to calculate the primality was: 0.845800 seconds
````

## Exercise 2

The technique that you used in the previous question is a bit a slow if you consider a big enough
number (e.g. 10-digits). Can you think of any other way to improve it? Implement the new one.

### Solution 2 

In this solution, I've incorporated the [Miller-Rabin algorithm](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#:~:text=The%20Miller%E2%80%93Rabin%20primality%20test,the%20Solovay%E2%80%93Strassen%20primality%20test.), 
a probabilistic method that introduces randomness to determine whether a given number is prime. 
The algorithm conducts multiple rounds of testing using random values, enhancing accuracy while retaining a small margin of uncertainty due to its probabilistic nature. 
The algorithm achieves a balance between computational efficiency and reliability, making it a practical choice for prime number verification in various applications.

> Select option 2

````
(2) - Check if a number is prime using the Miller-Rabin algorithm (Probabilistic)

Choose one option: 2

Type the number: 38277351233831

38277351233831 is probably prime.

Time taken to calculate the primality was: 0.0010116100 seconds

````


## Exercise 3

Based on the function built in Question 2, implement a function that returns the factorisation of
any composite number.

### Solution 3

Based on [Solution 2](#Solution-2) I've developed a probabilistic function to factorize composite numbers. 
The function leverages the [Pollard's Rho algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm), 
a powerful probabilistic method. Although it operates with some randomness, this algorithm excels in efficiently factoring numbers, 
particularly those with large prime factors. It provides a reliable and efficient solution for this task, 
despite its probabilistic nature.

> Select option 4

````
(4) - Factor a composite number using Pollard`s Rho algorithm (Probabilistic)

Choose one option: 4

Type the number: 937513221145

Factors of 937513221145: [Decimal('5'), Decimal('73'), Decimal('28499'), Decimal('90127')]

Time taken to compute was: 1.758000 milliseconds
````

## Exercise 4

Implement Euclid’s algorithm and compute

a) hcf(499017086208, 676126714752)

b) hcf(5988737349, 578354589)

### Solution 4

describe

> Select option 5

#### a) hcf(499017086208, 676126714752)

````
(5) - Find the highest common factor (HCF) using Euclid`s Algorit

Choose one option: 5

Type the number One: 499017086208

Type the number Two: 676126714752

HCF of 499017086208 and 676126714752: 93312

Time taken to compute was: 0.303200 milliseconds
````

#### b) hcf(5988737349, 578354589)

````
(5) - Find the highest common factor (HCF) using Euclid`s Algorit

Choose one option: 5

Type the number One: 5988737349

Type the number Two: 578354589

HCF of 5988737349 and 578354589: 9

Time taken to compute was: 0.229000 milliseconds
````

## Exercise 5

Explain how Euclid’s algorithm might help you find multiplicative inverses and implement it.
Solve for x the linear congruence 342952340x ≡ 1 (mod 4230493243)

### Solution 5

Euclid's algorithm plays a pivotal role in finding multiplicative inverses, 
a crucial concept in number theory and modular arithmetic. In the context of solving linear congruences, 
it is an invaluable tool.

To solve X in `342952340x ≡ 1 (mod 4230493243)`

We use  Euclid's algorithm to find the greatest common divisor (GCD) between the coefficients of 'x' (342952340) and the modulus (4230493243). 

Once the GCD is determined, we check if it equals 1. If it does, it implies that a multiplicative inverse exists, and 'x' can be found using modular arithmetic. 
Specifically, we can use the extended Euclidean algorithm to compute 'x.' This process will yield the unique solution that satisfies the given linear congruence, 
allowing us to find the multiplicative inverse efficiently.

> Select option 6

````
(6) - Solve for x in a linear congruence Ax ≡ 1 (mod B)

Choose one option: 6

Type the number A (Integer): 342952340

Type the number B (Modulo): 4230493243

The multiplicative inverse of 342952340 modulo 4230493243 is 583739113.

````

## Exercise 6

Write a program to convert an encrypted number c = m^e (mod n) into me the original m = c^d (mod n), where 0 < m < n is some integer. 
Pick any plaintext you would like to encrypt it using the public key (937513, 638471) and then check correctness of the algorithm.

### Solution 6

In this solution, I have implemented the RSA encryption and decryption algorithm. 

I began with the provided public key values, N (937513) and E (638471), and my primary objective was to compute the private key, denoted as 'D'. 

The private key is a vital component of the RSA system, and it is typically calculated using mathematical properties and modular arithmetic. 

In the context of RSA, 'D' is the modular multiplicative inverse of 'E' modulo the totient (ϕ) of 'N'.

To find 'D,' I employed the 'generate_private_key' which:

1. Start with the public keys: N = 937513 and E = 638471.
2. Then, 'factorize(n)' is called to find the prime factors 'P' and 'Q' of 'N.' This is done by the 'factorize' function, and in this case, it results in 'P' = 1069 and 'Q' = 877.
3. Next, compute the modular inverse 'D' using the 'mod_inverse(e, (q - 1) * (p - 1))' function. 'E' remains the same, and I calculate (q - 1) * (p - 1) as (877 - 1) * (1069 - 1) = 876 * 1068 = 937488.
4. Using 'mod_inverse(e, 937488),' you find that 'D' = 229703 is the modular multiplicative inverse of 'E' modulo 937488.

To see it working: 

> Select option 7

````
(7) - Perform RSA Encryption and Decryption

Choose one option: 7

Type the Public key numbers

Type the number (n): 937513
Type the number(e): 638471

Type the message (m): The RSA Algorithm

Public key is (n=937513, e=638471)
Private key is (229703, 937513)

Encrypted message is: [534554, 926459, 345782, 49486, 516330, 3073, 162202, 49486, 162202, 208115, 512040, 282487, 19263, 300201, 497824, 926459, 157064]
Decrypted message is: The RSA Algorithm

It worked!
````

## Exercise 7

Can you describe how question 5 might be used to break RSA algorithm and recover the
secret key?

### Solution 6

Breaking RSA by factoring N
If an attacker can factor N to obtain p and q, then he or she can compute ϕ(N) and use the extended euclidean algorithm to compute 
the private exponent d = e^−1modϕ(N). Since it is easy for a brute force search algorithm to find small factors of any integer by trial division, it is clear that p and q should be taken of roughly equal size.


Refs:

- https://www.nku.edu/~christensen/Mathematical%20attack%20on%20RSA.pdf
- https://github.com/kaushikthedeveloper/GeeksforGeeks-python/blob/master/Scripts/RSA%20Algorithm%20(%20Encryption%20-%20Decryption%20).py#L47
- https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/