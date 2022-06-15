with open('text_1.txt', 'w') as f:
    while True:
        line = input('Enter text or press "Enter" to exit:  ')
        if not line:
            break
        print(line, file=f)

