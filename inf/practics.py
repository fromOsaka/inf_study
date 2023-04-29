file = open('107_24.txt').read()
file = file.replace("AB", 'x')
file = file.replace("CB",'x')
k = 0
m = 0
for i in range(len(file)):
    if file[i] == 'x':
        k += 1
        m = max(m,k)
    else:
        k = 0
print(m)
