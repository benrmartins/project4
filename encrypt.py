import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept n (int) and e (int) as command-line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get the number of bits per character (call it width) needed for encryption, ie, number of bits needed to encode n
    width = rsa.bitLength(n)

    # Accept message to encrypt from standard input.
    message = stdio.readAll()

    for i in range(len(message)):
        # Use the built-in function ord() to turn c into an integer x.
        x = ord(message[i])
        # encrypt the ninput
        y = rsa.encrypt(x, n, e)
        encrypt = rsa.dec2bin(y, width)
        # Displayed the encrypted input
        stdio.write(binary)
    stdio.writeln()


if __name__ == '__main__':
    main()
