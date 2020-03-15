limit = int(input())
friends = []
total = 0
k=-1
for i in range(int(input())):
    friends.append(int(input()))
while total<=limit:
    total += min(friends)
    k += 1
    friends.remove(min(friends))
print(k)
    
    
    
