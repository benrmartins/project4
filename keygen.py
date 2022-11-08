import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept lo (int) and hi (int) as command-line arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Get public/private keys as a tuple.
    key = rsa.keygen(lo, hi)

    # looped through the three values in the tuple, separated by a space.
    for i in range(len(key)):
        # printed out the values separated by a space
        stdio.write(str(key[i]) + " ")
    stdio.writeln()


if __name__ == '__main__':
    main()
