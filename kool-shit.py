import string
from os import system
from time import sleep
system('cls')

#! not using string.printable cuz i need to get whitespace and letters asap
alpha = " " + string.ascii_letters + string.digits + string.punctuation

# text = str(input("Enter a string: "))
text = "yo yo yo 148 3 to the 3 to the 6 to the 9. Representing ABQ, what up BIATCH!! Leave at the tone"
final = []

for each in text:
    for each2 in alpha:
        final.append(each2)
        sleep(0.01)
        # system('cls') #* You can comment this line if you want
        print(*final, sep="")
        if each2 != each:
            final.pop()
        else:
            break