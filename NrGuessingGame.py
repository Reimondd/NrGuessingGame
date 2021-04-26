from random import randint
import os
import time
print("Number Guessing game (You only have 3 tries) \n")
def main():
    secretNumber = randint(1, 5)
    gs = 0
    gl = 3
    while gs < gl:
        UIn = int(input("Guess the number in between 1 and 5: "))
        gs += 1
        if UIn == secretNumber:
            print("You guessed the number!")
            time.sleep(2)
            os.system('cls')
            return main()
        elif gs == 3:
            print("You went over the limit :/ ")
            time.sleep(1)
            os.system('cls')
            return main()
        else:
            print("No")


main()
