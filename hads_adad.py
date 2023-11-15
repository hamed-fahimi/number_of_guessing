import array as array
import random

list = []
# guess = []
# correction = []
for i in range(5):
    num = random.randint(1, 9)
    list.append(num)
for i in range(5):
    list[i] = int(list[i])


def hads():
    guess = input().split()
    for i in range(5):
        guess[i] = int(guess[i])
    return guess


def find(guess):

    correction = []
    for i in range(5):
        if guess[i] == list[i]:
            correction.append('g')
        elif guess[i] != list[i]:
            if guess[i] in list:
                correction.append('b')
            else:
                correction.append('r')
    return correction


def winner_or_loser(correction):
    flag = True
    for k in range(5):
        if correction[k] == 'g':
            flag = True
        else:
            flag = False
            break
    return flag


def controller():
    h = hads()
    print(h)

    correction = find(h)

    print(correction)

    return winner_or_loser(correction)


for i in range(4):
    flag = controller()
    if flag:
        print("you are winner")
        break
    elif i == 3:
        print("you are losser")

