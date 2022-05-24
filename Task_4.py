line = input("Введите любое предложение: ").split()
for i, word in enumerate(line, 1):
    print(f'{i} {word[:10]}')
