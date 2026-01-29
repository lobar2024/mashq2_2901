
# 2
#1
roy1 = [2, 6, 3]
roy2 = [4, 2, 6]
birlaw = roy1 + roy2
yangi = set(birlaw)
print(yangi)

#2
roy = [1, 2, 3, 4, 5, 6, 7, 8]
juftt = []
tooq = []
for i in range(len(roy)):
    if i % 2 == 0:
        juftt.append(roy[i])
    else:
        tooq.append(roy[i])

print(f'Juft indeksdagi sonlar: {juftt}')
print(f'Toq indeksdaki sonlar: {tooq}' )

#3
roy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(roy)
orta = f'Royxatdsaki eng katta son: {max(roy)}, Eng kicik son: {min(roy)} Ularning orasidagi farqi: {max((roy)) - min(roy)} '
print(orta)

#4
roy = [3, -5, 0, 7, -2, 0, 4, -1]
ress = []

for x in roy:
    if x > 0:
        ress.append(-x)
    elif x < 0:
        ress.append(-x)
    else:
        ress.append(0)

print(ress)

#5
roy = [1, 2, 2, 3, 1, 4, 2, 3, 1]
print({x: roy.count(x) for x in roy})
