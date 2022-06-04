def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print('Error!!! Enter try number')
        return
    if x < 0 or y > 0:
        print('Error!!! Enter try number x>0, y<0')
        return
    return x ** y

def main():
    num = (my_func(int(input('Enter first number: ')),
                  int(input('Enter second number: '))))
    print(round(num, 40))


if __name__ == '__main__':
    main()

#Вариант без **
def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print('Error!!! Enter try number')
        return
    if x < 0 or y > 0:
        print('Error!!! Enter try number x>0, y<0')
        return
    result = 1
    for _ in range(abs(y)):
       result /= x
    return result

def main():
    num = (my_func(int(input('Enter first number: ')),
                  int(input('Enter second number: '))))
    print(round(float(num), 5))


if __name__ == '__main__':
    main()