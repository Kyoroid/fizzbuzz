def fizzbuzz(n):

    def _fizzbuzz(x):
        out = list()
        if x % 3 == 0:
            out.append("Fizz")
        if x % 5 == 0:
            out.append("Buzz")
        if len(out) == 0:
            out.append(str(x))
        return "".join(out)

    return [_fizzbuzz(i) for i in range(1, n+1)]


def main(args=None):
    import argparse

    description = 'FizzBuzz'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('number', help='Number of turns')
    args = parser.parse_args(args)

    if args.number is not None:
        out = fizzbuzz(int(args.number))
        print(" ".join(out))

if __name__ == "__main__":
    main()