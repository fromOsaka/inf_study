k = 0
asd = []
for i in range(312614, 312651+1):
    for d in range(1, int(i**0.5)+1):
        if d != (i // d):
            k += 2
        else:
            k += 1
    if k