def my_func(a, b, c):
    return (a + b + c) - min(a, b, c)


print(my_func(int(input('Enter a: ')),
              int(input('Enter b: ')),
              int(input('Enter c: '))))


