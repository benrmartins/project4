import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    width = rsa.bitLength(n)
    text = stdio.readAll()

    for i in range(0, len(text) - 1, width):
        n = text[i: i + width]
        x = rsa.bin2dec(n)
        dec = rsa.decrypt(x, n, d)

    stdio.writeln(dec)


if __name__ == '__main__':
    main()
