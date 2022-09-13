list = []
limst = []
nlist = []
for i in range(10):
    list.append(i)
print(list[:4])
print(list[5:])
print(list[::2])
for i in range(len(list)):
    if list[i]%2 != 0:
        limst.append(list[i])
print(limst[:])
i = 1
while i < len(list)+1:
    i += 1
    nlist.append(list[1-i])

print(nlist[:])
print(nlist[:5])
print(nlist[5:])