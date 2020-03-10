a = list(map(int, input().split(' ')))

if a == sorted(a):
    print("YES")
else:
    print("NO")
