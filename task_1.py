def user_num(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print('-' * 20)
        print('Cannot be divided by zero')


def main():
    print(user_num(input('Enter your first number: '),
                   input('Enter your second number: ')))


if __name__ == "__main__":
    main()
