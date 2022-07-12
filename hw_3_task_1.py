def main():
    def decorator(func):
        d = dict()

        def inner(number):
            if not d.get(number):
                d[number] = func(number)
            return d[number]

        return inner

    @decorator
    def multiplier(number: int):
        return number * 2


if __name__ == '__main__':
    main()
