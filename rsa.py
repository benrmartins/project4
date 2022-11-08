import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # stores prime numbers between low and high into a list
    prime = _primes(lo, hi)

    # Get 2 random prime numbers from the list
    p, q = _sample(prime, 2)

    # Set n and m to pq and (p − 1)(q − 1)
    n = q * p
    m = (q - 1) * (p - 1)

    # Gets a list primes from the intervals
    prime = _primes(2, m)

    # gets a random prime e from the list such that e does not divide m
    e = _choice(prime)
    while m % e == 0:
        e = _choice(prime)
    d = 1
    # Find a d ∈ [1, m) such that ed mod m = 1
    while d < m:
        # breaks if (e * d) % m is divisible by 1
        if (e * d) % m == 1:
            break
        d += 1

    # returns a tuple of the number
    return (n, e, d)


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # equation to encrypts the value chosen radnomly
    return x ** e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # equation to Decrypts the value chosen radnomly
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # creates a list to store the prime numbers
    prime = []

    # For each p ∈ [lo, hi), if i is a prime, add i to the list
    for i in range(lo, hi):
        # makes sure the value of i is greater than 2
        if i < 2:
            continue
        j = 2
        # loopa through each number
        while i >= j * j:
            # makes sure that the number is prime
            if i % j == 0:
                break
            j += 1
        # adds i to the list of prime numbers
        if i < j*j:
            prime += [i]
    # returns the list
    return prime


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Create a list b that is a copy (not an alias) of a.
    b = a[:]
    # Shuffle the first k elements of b.
    for i in range(k):
        # gets a ramdom nuber from the list
        r = stdrandom.uniformInt(i, len(a))
        # exchanges the varibles with each other by using a temp variable
        temp = b[i]
        b[i] = b[r]
        b[r] = temp

    # Return a list containing the first k elements of b.
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Get a random number r ∈ [0, l), where l is the number of elements in a.
    r = stdrandom.uniformInt(0, len(a))

    # Return the element in a at the index r.
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
