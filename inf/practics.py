from fnmatch import fnmatch
for num in range(0, 3 * 10 ** 8, 1323):
    if (num % 780 == 0) and fnmatch(str(num), '*[0,2,4,6,8]32??'):
        print(num)