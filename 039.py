a = list(input())
b = ''.join(a)
a = b.replace('q', 'e', a.count('q'))
print(a)

#간단하게
n = input()
print(n.replace("q", "e"))
