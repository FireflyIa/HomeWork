def my_func():
    sum = 0
    f = True
    while f:
        list_user = input('Enter a number by a space or click Q for exit:\n')
        for i in list_user:
            if i == 'Q':
                f = False
                break
            try:
                sum += int(i)
            except ValueError:
                pass
        print(f'Sum enter numbers: {sum}')

my_func()