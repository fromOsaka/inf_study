def  f(a,b,m=0):            #номер 23 из  кегэ
    if a > b:
        return 0
    if a == b:
        if m <= 15:
            return 1 
        else:
            return 0 
    if a % 2 == 0:
        return f(a+2,b,m+1) + f(a+3,b,m+1) + f(a*2+1,b,m+1)
    if a % 2 != 0:
        return f(a+2,b,m) + f(a+3,b,m) + f(a*2+1,b,m)
    
print(f(1,55))
