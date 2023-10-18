import random

repeat = True

number = random.randint(1, 100)
guess = 0
tries = 0

while guess != number:
    if guess < number:
        print("pameegiini lielaaku skaitli")
    else:
        print("pameegini mazaaku skaitli")
        
    guess = int(input("uzminiu skaitli: "))
    tries += 1
else:
    if tries < 4:
        print(f"uzmineeji tikai peec {tries} reizēm")
    elif tries<7:
        print(f"nav slikti bet uzzmineeji pēc {tries} reizēm")
    else:
        print(f"uzzmineeji peec {tries} reizēm")
    print(f"tu uzminēji pēc {tries} reizēm! noob L")
    
    
    
response = input("vai tu gribi turpināt y/n?")
if response == "y":
    repeat = True
elif response == "n":
    repeat = False
    print("paldies par spēli")
else:
    repeat = False
    print("paldies par spēli")
