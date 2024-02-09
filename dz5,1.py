stud = {
    "Иван": [8, 10, 6, 8, 10, 6, 8, 10, 6, 8, 10, 6],
    "Мария": [10, 10, 8, 10, 10, 8, 10, 10, 8, 10, 10, 8],
    "Алексей": [6, 8, 6, 6, 8, 6, 6, 8, 6, 6, 8, 6]
}

max = 0
min = 12
for name in stud:
    if max < sum(stud[name])/len(stud[name]): nmax = name; max = sum(stud[name])/len(stud[name])
    if min > sum(stud[name])/len(stud[name]): nmin = name; min = sum(stud[name])/len(stud[name])

the_best = str("Най успішний: " + nmax)
worst = str("Най гірший: " + nmin)

print(the_best,'\n',worst)