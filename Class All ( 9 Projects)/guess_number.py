import random as ra 
computer=ra.randint(1,100)
correct_gusses=0
while True:
    try:
        user=int(input("Enter a number between 1 and 100 :"))
        if user > 100 or user < 1:
            print("Invalid Input")    
    except ValueError as e:
        print(f"Entered value is not an interger \n Error:{e}")
    if computer > user:
        print("Guess Higher")
    elif computer < user:
        print("Guess Lower")
    else:
        print(f"Corect Guess {computer}")
        correct_gusses+=1
        print(f" Score: {correct_gusses}")
    
    
    play=input("Play again (y/n)").lower()
    if play in ["yes","y"] :
        continue
    if play in ["no","n"]:
        break
    else:
        print("Chose from above choices!!")
print("Thanks for playing")