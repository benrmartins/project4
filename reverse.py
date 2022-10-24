import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a[:-1]:
        stdio.writef('%s ', v)
    stdio.writeln(a[-1])


# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    for i in range(...):
        # Iterate over half of the list a...

        # Exchange element at i in a with the element at len(a) - i - 1.
        ...


if __name__ == '__main__':
    main()
