def game(a,n=0):
    if n > 4:
        return False
    if a >= 36:
        if a <= 60:
            return n in [2,4]
        else:
            return n in [1,3]
    if n % 2 == 0:
        return game(a+1,n+1) and game(a*2,n+1) and game(a*3,n+1)
    else:
         return game(a+1,n+1) or game(a*2,n+1) or game(a*3,n+1)

print('hi git, i made this repository for my inf consp')
