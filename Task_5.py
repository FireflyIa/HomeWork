profit = float(input("Введите значение выручки в рублях: "))
outlay = float(input("Введите значение расходов в рублях: "))
gain = profit - outlay
if gain > 0:
    print("У Вас прибыльное предприятие, Ваша прибыль ", round(gain, 2), ("RUB"))
else:
    print("У Вас убыточное предприятие, Ваши потери ", round(gain, 2), ("RUB"))
if gain > 0:
    margin = profit / outlay
    man = int(input("Введите количество сотрудников на предприятии: "))
    mangain = round(profit) / man
    print("Ваша маржа за текущий период: ", round(margin), ("%"))
    print("Эффективность одного сторудника на предприятии: ", round(mangain, 2), ("RUB"))
