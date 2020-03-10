def one(n):
    def two(k):
        return k**n
    return two

a = one(2)
b = one(3)
c = one(4)
print(a)
print(b)
print(c)
print(a(10))
print(b(10))
print(c(10))
