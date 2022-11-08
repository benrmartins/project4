import rsa
import stdio
import sys


# Entry point.
def main():
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    key = rsa.keygen(lo, hi)

    for i in range(len(key)):
        stdio.write(str(key[i]) + " ")
    stdio.writeln()


if __name__ == '__main__':
    main()
