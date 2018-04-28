def bijiao(a,b):
    if a < b:
        print("%d is too big"%b)
        return False
    if a > b:
        print("%d is too small"%b)
        return False
    if a == b:
        print("bingo!You are right!Again?")
        c = str(input())
        if c in ("Yes","yes","Y","y"):
            again()
        else:
            return True

def again():
    print("Give me a number")
    a = randint(0,1000)
    answer = False
    while answer == False:
        b = int(input())
        answer = bijiao(a,b)
    print("Byebye!")

print("What am I?(1~1000)")
from random import *

1111
