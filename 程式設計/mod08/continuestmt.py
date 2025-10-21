# continue stmt
for i in range (0, 7):
    if i % 2 == 1:
        continue
    print(i, end=' ')

print()
for i in range (0, 7):
    if i % 2 == 1:
        break
    print(i, end=' ')
print()
print(7 / 3)
a=7
b=3
print(a == b * (a // b) + (a % b) )