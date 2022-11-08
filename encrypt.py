import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    width = rsa.bitLength(n)
    message = stdio.readAll()

    for i in range(len(message)):
        x = ord(message[i])
        encrypt = rsa.encrypt(x, n, e)
        binary = rsa.dec2bin(encrypt, width)
        stdio.write(binary)
    stdio.writeln()


if __name__ == '__main__':
    main()
