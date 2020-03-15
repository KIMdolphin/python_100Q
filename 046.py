st = ""
for i in range(1,101):
    st = st + str(i)
stl = list(st)
for j in range(len(stl)):
    stl[j] = int(stl[j])
print(sum(stl))
