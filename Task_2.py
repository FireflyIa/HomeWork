usrList = input("Введите цифры через пробел: ").split()
for i in range(1, len(usrList), 2):
    usrList[i - 1], usrList[i] = usrList[i], usrList[i - 1]
print(usrList)
