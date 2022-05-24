rating = [1, 3, 5, 6, 7, 8]
for _ in range(3):
    i = int(input("Ввеите число до 10 - "))
    flag = False
    for j in range(len(rating)):
        if rating[j] > i:
            rating.insert(j, i)
            flag = True
            break
    if not flag:
        rating.append(i)
    print(*rating)
