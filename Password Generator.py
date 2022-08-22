import random 
import string

try:
    User_Len = int(input("How many characters would you like your password to be in length? "))
except:
    print("Please enter an integer")

for i in range(User_Len):
    n = random.randint(0,2)
    if n == 0:
        print(random.randint(0,99), end="")
    elif n == 1:
        print(random.choice(string.ascii_letters), end="")
    elif n == 2:
        print(random.choice(string.punctuation), end="")