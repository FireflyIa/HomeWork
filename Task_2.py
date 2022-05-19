x = int(input("Введите секунды, я подсчитаю сколько это часов и минут - "))
minuts = x//60
hours = minuts//60
second = x % 60
if second >= 60:
    minuts = minuts + 1
if minuts >= 60:
    minuts = minuts % 60
print("Время ",f"{hours:02d}",":",f"{minuts:02d}",":",f"{second:02d}")
