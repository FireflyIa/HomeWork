with open('text_2.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    for index, value in enumerate(line, 1):
        words = len(value.split())
        print(f'Строка {index} содержит {words} слов')
