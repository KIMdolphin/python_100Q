a = list(map(int, input().split(' ')))
k = 0
for i in range(3):
    k += a.count(max(a))
    for j in range(a.count(max(a))):
        a.remove(max(a))
print(k)
