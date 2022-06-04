def fact_gen(num):
    f_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact_gen(int(input('Factorial number: '))):
    print(el)

