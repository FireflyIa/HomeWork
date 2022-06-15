d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4_1.txt', 'w', encoding='utf-8') as f1:
        for line in f:
            en, *num = line.split()
            ru = d[en]
            f1.write(' '.join([ru] + num) + '\n')

