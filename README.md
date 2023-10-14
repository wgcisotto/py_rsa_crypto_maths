# The RSA Algorithm

## Content

* [Introduction](#Introduction)
* [Exercises](#Exercises)
  * [Exercise 1](#Exercise-1)
  * [Exercise 2](#Exercise-2)
  * [Exercise 3](#Exercise-3)
  * [Exercise 4](#Exercise-4)
  * [Exercise 5](#Exercise-5)
  * [Exercise 6](#Exercise-6)
  * [Exercise 7](#Exercise-7)
* [Resolution](#Resolution)

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

# Exercises

## Exercise 1

A number p is defined as prime if and only if it is divisible by itself (and 1). Implement a method
from scratch that allows to test primality of a number using trial and error method.

## Exercise 2

The technique that you used in the previous question is a bit a slow if you consider a big enough
number (e.g. 10-digits). Can you think of any other way to improve it? Implement the new one.

## Exercise 3

Based on the function built in Question 2, implement a function that returns the factorisation of
any composite number.

## Exercise 4

Implement Euclid’s algorithm and compute

a) hcf(499017086208, 676126714752)

b) hcf(5988737349, 578354589)

## Exercise 5

Explain how Euclid’s algorithm might help you to find multiplicative inverses and implement it.
Solve for x the linear congruence 342952340x=1 mod4230493243

## Exercise 6

Write a program to convert an encrypted number c = (mod n) into me the original m = cd
(modn), where 0 < m < n is some integer. Pick any plaintext you would like to encrypt it
using the public key (937513, 638471) and then check correctness of the algorithm.

## Exercise 7

Can you describe how question 5 might be used to break RSA algorithm and recover the
secret key?

# Resolution

