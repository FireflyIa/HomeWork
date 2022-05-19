age = int(input("Сколько вам лет? - "))
x = age % 10
if x >= 5:
    print("Вам", age, "лет")
elif x == 1:
    print("Вам", age, "год")
else:
    print("Вам", age, "года")
name = input("Как Вас зовут? - ")
print("Приятно познакомиться, " + name +"!")
month = input("Какой у Вас," + name + ", месяц рождения? - ")
day = input("Какой у Вас," + name + ", день рождения? - ")
print(name + " , Вы родились " + day + " " + month)
