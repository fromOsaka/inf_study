text = open('244-2.txt').read()
statis = {}
for i in range(2,len(text)-1):
    if text[i-2] == text[i-1]:
        if text[i] not in statis:
            statis[text[i]] = 1
        else:
            statis[text[i]] += 1
print(statis)
result = [(statis[letter],letter) for letter in statis]
result.sort()
print(result)
