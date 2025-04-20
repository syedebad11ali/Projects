print("Agreement Bot")

answer = input("Do you agree? (yes/no): ").strip().lower()

if answer in ['yes', 'y']:
    print("Great! You agreed.")
elif answer in ['no', 'n']:
    print("Too bad! Maybe next time.")
else:
    print("Invalid input. Please enter yes or no.")
