import random


a = random.randint(1, 6)
b = int(input("крутите барабан!(от 1 до 6): "))
def pognali():
    if b == a:
        print("вы умерли")
    else:
        print("вам повезло!")

pognali()
print(a)