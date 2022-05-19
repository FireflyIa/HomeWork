num = int(input("Пользователь, введите число: "))
max_num = num % 10
while num:
    last_num = num % 10
    if max_num < last_num:
        max_num = last_num
        if max_num == 9:
            break
    num = num // 10
print("Наибольшая цифра в числе: ", max_num)
