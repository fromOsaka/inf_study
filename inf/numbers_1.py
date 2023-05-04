
#for number in range(128, 255):         код для решения номера 5 в егэ
#    code = bin(number)[2:]
#   code += str(code.count("1") % 2)
#    code += str(code.count("1") % 2)
#    print(int(code, 2 ))

#for number in range(76, 90):
#    print(number, bin(number)[2:])

#print("a b c d")                       примерный код для номера 2 ЕГЭ
#for a in 0, 1:
#    for b in 0, 1:
#        for c in 0, 1:
#           for d in 0, 1:
#                f = ((not a and not b)) or (b == c) or d
#                if f == False:
#                    print(a, b, c, d)

#for number in range(43, 50):
    #print(number, bin(number)[2:])
    #перевод из двоичной в десятичную
#print(int('1100', 2))
#print(3 % 2)

#for n in range(1, 100000):                  #один из видов решения номера 5
#    b = bin(n)[2:]
#    if b.count('1') % 2 == 0:
#        r = '10' + b[2:] + '0'
#    else:
#        r = '11' + b[2:] +'1'
#    if int(r, 2) > 40:
#        print(n,b,r)
#        break

'''''
                                         #примерный код для решения 6го номера егэ

from turtle import Turtle    #подключаем библиотеку для работы с черепашкой (библиотека по умолчанию)
from time import sleep       #функция ожидание, чтобы окно не закрывалось сразу (библиотека по умолчанию)
robot = Turtle()    #создаем черепашку в переменной робот
s = 40              #задаем масштаб
robot.speed(0)         #скорость выполнения кода
for i in range(4):   #повторить n раз
    robot.forward(10 * s)
    robot.right(60)
    robot.forward(10 * s)
    robot.right(120)        #robot.forward - идти вперед robot.right - поворот направо
robot.penup()           #поднимаем перо (после выполнения блока движения, задаем команду, чтобы пропал след от пути)
for x in range(0, 20):     #перебираем различные координаты x,y
    for y in range(-15, 5):
        robot.goto(x * s, y * s)         #перемещаем черепаху в эту позицию (умножаем на масштаб)
        robot.dot(3 , "red")          #команда отвечающая за постановку точек (ось координат)
sleep(15)             #функция из библиотеки time, не дает окну закрыться сразу


from itertools import permutations
count = 0
glas = 'ЕАИ'
sogl = 'ГРСМ'
for comb in permutations('ГЕРАСИМ', 7):
    word = ''.join(comb)
    t = True
    for i in range(len(word)-1):
        if (word[i] in glas) and (word[i+1] in glas):
            t = False
        if (word[i] in sogl) and (word[i + 1] in sogl):
            t = False
    if t:
        count += 1
print(count)

 
#from itertools import permutations                         код для одного из видов 8го номераЧ
#count = 0                                                          
#for comb in permutations('ТИМОФЕЙ', 7):
#    word = ''.join(comb)
#    if (word[0] != "Й") and (word[5] != "Й"):
#        count += 1
#print(count, comb[:-2])


from itertools import product                   код для одного из видов 8го номера
count = 0
for comb in product("АКРУ", repeat = 5):
    word = ''.join(comb)
    count += 1
    if word == "РУКАА":
        print(count, word)


from itertools import product             код для одного из видов 8го номера 
count = 0                
glas = "А"
for comb in product("АБВГ", repeat = 6):
    word = ''.join(comb)
    if (word[0] not in glas) and ('АА' not in word) and ('ББ' not in word) and ('ВВ' not in word) and ('ГГ' not in word):
        count += 1
print(count)'''

'''for a in range(1,1000):
    check = True
    for x in range(1,1000):
        for y in range(1,1000):
            f = ((x < a) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= a))
            if not f:
                check = False
        if check == False:
            break
    if check == True:
        print(a)'''
"""def f(num):
    if num < 3:
        return 1
    if (num > 2) and (num % 2 == 0):
        return f(num - 2) - f(num -1)
    else:
        return f(num-2) - f(num -3)

print(f(50))"""

'''from turtle import Turtle,tracer,done            6й номер ( не надо ждать отрисовку)
robot = Turtle()
m = 30
tracer(0)
for i in range(4):
    robot.forward(10*m)
    robot.right(60)
    robot.forward(10*m)
    robot.right(120)
robot.penup()
for x in range(0,16):
    for y in range(-10,5):
        robot.goto(x * m, y * m)
        robot.dot(5, 'red')
done()'''

"""file = op
en('17.txt')
numbers = []
for line in file:
    numbers.append(int(line))
count = max = 0
for i in range(len(numbers)):
    first = numbers[i]
    for j in range(i+1, len(numbers)):
        second = numbers[j]
        if (abs(first - second) % 45 == 0) and ((first % 18 == 0) or (second % 18 == 0)):
            count += 1
            if (first - second) > max:
                max = first + second
print(count, max)"""


"""file = open('17 (1).txt')
numbers = []
for line in file:
    numbers.append(int(line))
count = max = 0
for i in range(len(numbers)):
    first = numbers[i]
    for j in range(i+1, len(numbers)):
        second = numbers[j]
        if ((first + second) % 7 == 0):
            count += 1
            if (first + second) > max:
                max = first + second
print(count, max)"""


"""numbers = list(map(int, open('17.txt')))
rez_list = []
chet = []
for el in numbers:
    if el % 2 == 0:
        chet.append(el)
avg = sum(chet)/len(chet)
count = max = 0
for i in range(len(numbers) - 1):
    f, s = numbers[i], numbers[i+1]
    if (min(f,s) < avg) and ((f * s) % 3 == 0) :
        count += 1
        if (f + s)> max:
            max = (f+s)
print(count,max)"""

'''def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa
for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2)  # перевод в десятичную систему
    if r > 47:
        print(r)
        break'''

'''from functools import lru_cache

def moves(h):
    return h+1,h+2 , h*3

@lru_cache(None)
def game(h):
    if h>= 46:              одна куча 20й и 21 
        return 'w'
    if any(game(s) == 'w' for s in moves(h)):
        return 'p1'
    if all(game(s) == 'p1' for s in moves(h)):
        return 'v1'
    if any(game(s) == 'v1' for s in moves(h)):
        return 'p2'
    if all(game(s) == 'p2' or game(s) == 'p1' for s in moves(h)):
        return 'v2'

for s in range (1,46):
    print(s,game(s))'''

'''from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1,b) , (a2,b) , (a,b+1), (a,b2)

@lru_cache(None)
def game(h):
    a, b = h             20е и 21 на две кучи 
    if a+b >=117:
        return 'w'
    if any(game(m) == 'w' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'v1'
    if any(game(m) == 'v1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(h)):
        return 'v2'

for s in range (1,104):
    h = 13, s
    if game(h) == 'v2':
        print(s,game(h))'''

'''21 номер на две кучи'''
'''def f(x,y,n=0):
    if x + y >= 79:
        return n == 3
    if n > 3:
        return False
    if n % 2 == 0:
        return f(x+1,y,n+1) or f(x,y+1,n+1) or f(x*3,y,n+1) or f(x,y*3,n+1)  #условие 
    else:
        return f(x+1,y,n+1) and f(x,y+1,n+1) and f(x*3,y,n+1) and f(x,y*3,n+1)
#вместо 79 использовать чило, которое необходимо для выигрыша
#в начальный момент в одной куче было 6 камней
for s in range(1,72+1):
    if f(6,s):
        print(s)'''




'''def game(a,b,n=0):
    if a + b >= 50:
        return n in [2,4]
    if n > 4:
        return False
    if n % 2 == 0:
        return game(a+1,b,n+1) and game(a,b+1,n+1) and game(a*2,b,n+1) and game(a,b*2,n+1)
    else:
        return game(a+1,b,n+1) or game(a,b+1,n+1) or game(a*2,b,n+1) or game(a,b*2,n+1)

for i in range(1,41+1):
    if game(8,i) == True:
        print(i)'''


"""def game(a,b,n=0):
    if a + b <= 20:
        return n in [2,4]
    if n > 4:
        return False
    if n % 2 == 0:
        return game(a-1,b,n+1) and game(a,b-1,n+1) and game(a//2,b,n+1) and game(a,b//2,n+1)
    else:
        return game(a-1,b,n+1) or game(a,b-1,n+1) or game(a//2,b,n+1) or game(a,b//2,n+1)
    
for i in range(10,1000):
    if game(10,i):
        print(i)"""




"""def game(a,b,n=0):
    if a+b >= 44:
        return n == 3
    if n > 3:
        return False
    if n % 2 == 0:
        return game(a+b, b, n+1) or game(a, b + a, n+1)
    else:
        return game(a+b, b, n+1) and game(a, b + a, n+1)
minimal = 100000
for a in range(100):
    for b in range(100):
        if game(a,b):
            if abs(a-b)<= minimal:
                minimal = abs(a-b)
                print(a,b)"""    



'''def  f(a,b,m=0):            #номер 23 из  кегэ
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
    
print(f(1,55))'''

'''file = open('inf_26_04_21_24.txt').readlines()
lines = [line for line in file if line.count('A') < 25]         nO 24
#rint(len(lines))
mx = 0
for line in lines:
    letters = set(line)
    for letter in letters:
        dis = line.rindex(letter) - line.index(letter)
        if dis > mx:
            mx = dis
print(mx)'''


'''
text = open('243.txt').read()
statis = {}
for i in range(1,len(text)-1):
    if text[i-1] == text[i+1]:
        if text[i] not in statis:
            statis[text[i]] = 1
        else:
            statis[text[i]] += 1
print(statis)
result = [(statis[letter],letter) for letter in statis]
result.sort()
print(result)'''

"""file = open('24_demo.txt').read()
cer_len = max_len = 0
for i in range(1,len(file)):
    if file[i] != file[i-1]:
        cer_len += 1
        if cer_len > max_len:
            max_len = cer_len
    else:
        cer_len = 1
print(max_len)"""

"""from fnmatch import fnmatch
for number in range(0, 10**8, 211):
    if fnmatch(str(number),'11??4*56'):
        print(number, number//211)"""

'''from fnmatch import fnmatch
for num in range(0, 3 * 10 ** 8, 1323):
    if (num % 780 == 0) and fnmatch(str(num), '*[0,2,4,6,8]32??'):
        print(num)'''