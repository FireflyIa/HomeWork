line = [1, 2, 'Hello', False, [3, 4], {1: 'one'}, 'False']
for i, item in enumerate(line, 1):
    print(f'{i}) {item} - this {type(item)}')

