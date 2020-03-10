a = list(map(int, input().split(' ')))
k = 0
for i in range(3):
    k += a.count(max(a))
    list(filter((max(a)).__ne__, a))
print(k)
