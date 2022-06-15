with open('text_3.txt', 'r', encoding='utf-8') as f:
    d_pers = {pers.split()[0]: float(pers.split()[1]) for pers in f}
    # cash = [float(item) for item in d_pers.values()]
    print(f'Средняя зарплата сотрудников:  {round(sum(d_pers.values()) / len(d_pers), 3)}\n'
          f'{"-"*40}\n'
          f'Сотрудники получающие меньше 20000: {[e[0] for e in d_pers.items() if e[1] < 20000]}')
