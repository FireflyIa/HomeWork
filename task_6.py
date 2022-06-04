from itertools import count, cycle

for i in count(int(input('С какого числа начать счет: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

