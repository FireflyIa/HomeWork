mlist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([j for i, j in enumerate(mlist) if i != 0 and j > mlist[i - 1]])
