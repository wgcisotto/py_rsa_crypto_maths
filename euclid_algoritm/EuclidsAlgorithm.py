def euclid_hcf(a, b):
    while b:
        a, b = b, a % b
    return a
