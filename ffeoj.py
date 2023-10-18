


import random

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Uzmini skaitli: "))

if number == guess:
    print("Uzminēji skaitli")
elif number > guess:
    print("Pārak mazs skaitlis")
elif number < guess:
    print("Pārāk liels skaitlis")
else:
    print("Kļūda")
