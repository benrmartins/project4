import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    width = rsa.bitLength(n)
    text = stdio.readAll()

    for letter in text:
        i = ord(letter)
        y = rsa.encrypt(i, n, e)
        en = rsa.dec2bin(y, width)

    stdio.writeln(en)


if __name__ == '__main__':
    main()
