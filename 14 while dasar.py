i = 1
while i <= 10 :
    print(i, end=' ')
    if i == 5 :
        break
    i = i + 1

print('ini diluar while')
print()


for j in range(1,11) :
    if j==5 :
        continue
    print(j, end=' ')
