import json

def to_top(r, s, answer):
    global was_found
    global cont
    print(answer)
    if answer:
        if r > 0 and dataJ[r - 1][0][s] == answer[0]:
            word.append((r - 1, s))
            findword(r - 1, s, answer[1:])
        elif s > 0 and dataJ[r][0][s - 1] == answer[0]:
            word.append((r, s - 1))
            findword(r, s - 1, answer[1:])
        elif s < LENROW - 1 and dataJ[r][0][s + 1] == answer[0]:
            word.append((r, s + 1))
            findword(r, s + 1, answer[1:])
        else:
            cont = True
    else:
        was_found = True

def to_bottom(r, s, answer):
    global was_found
    global cont
    print(answer)
    if answer:
        if r < QUENTITYROW - 1 and dataJ[r+1][0][s] == answer[0]:
            word.append((r+1, s))
            to_bottom(r+1, s, answer[1:])
        elif s > 0 and dataJ[r][0][s-1] == answer[0]:
            word.append((r, s-1))
            to_right(r, s-1, answer[1:])
        elif s < LENROW-1 and dataJ[r][0][s+1] == answer[0]:
            word.append((r, s+1))
            to_left(r, s+1, answer[1:])
        else:
            cont = True
    else:
        was_found = True

def to_right(r, s, answer):
    global was_found
    global cont
    print(answer)
    if answer:
        if r > 0 and dataJ[r-1][0][s] == answer[0]:
            word.append((r-1, s))
            to_top(r-1, s, answer[1:])
        elif r < QUENTITYROW - 1 and dataJ[r+1][0][s] == answer[0]:
            word.append((r+1, s))
            to_bottom(r+1, s, answer[1:])
        elif s < LENROW - 1 and dataJ[r][0][s + 1] == answer[0]:
            word.append((r, s+1))
            to_left(r, s+1, answer[1:])
        else:
            cont = True
    else:
        was_found = True

def to_left(r, s, answer):
    global was_found
    global cont
    print(answer)
    if answer:
        if r > 0 and dataJ[r-1][0][s] == answer[0]:
            word.append((r-1, s))
            to_top(r-1, s, answer[1:])
        elif r < QUENTITYROW - 1 and dataJ[r+1][0][s] == answer[0]:
            word.append((r+1, s))
            to_bottom(r+1, s, answer[1:])
        elif s > 0 and dataJ[r][0][s - 1] == answer[0]:
            word.append((r, s-1))
            to_right(r, s-1, answer[1:])
        else:
            cont = True
    else:
        was_found = True

def findword(r, s, answer):
    global was_found
    global cont
    print(answer)
    if answer:
        if r > 0 and dataJ[r-1][0][s] == answer[0]:
            word.append((r-1, s))
            to_top(r-1, s, answer[1:])
        elif r < QUENTITYROW - 1 and dataJ[r+1][0][s] == answer[0]:
            word.append((r+1, s))
            to_bottom(r+1, s, answer[1:])
        elif s > 0 and dataJ[r][0][s-1] == answer[0]:
            word.append((r, s-1))
            to_left(r, s-1, answer[1:])
        elif s < LENROW-1 and dataJ[r][0][s+1] == answer[0]:
            word.append((r, s+1))
            to_right(r, s+1, answer[1:])
        else:
            cont = True
    else:
        was_found = True

with open('data/data.json', 'r') as f:
    data = f.read()

dataJ = json.loads(data)
with open('data/answers.json', 'r') as f:
    answers = f.read()
answersJ = json.loads(answers)

QUENTITYROW = len(dataJ) #Кол-во строк
LENROW = len(dataJ[0][0]) #Длинна строки (кол-во букв в строке)

for answer in answersJ:
    print(answer)
    r = 0
    for row in dataJ:
        s = 0
        was_found = False
        cont = False
        for el in row[0]:
            word = []
            if el == answer[0]:
                word.append((r, s))
                findword(r, s, answer[1:])
                print(word)
            if was_found:
                break
            if cont:
                continue
            s += 1
        if was_found:
            break
        r += 1
    # print(word)