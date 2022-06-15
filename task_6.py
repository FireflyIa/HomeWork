with open('text_6.txt', encoding='utf-8') as f:
    a = f.readlines()
    for s in a:
        n_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        n2_str = [int(i) for i in n_str.split()]
        print(f'{s.split()[0]} {sum(n2_str)}')
