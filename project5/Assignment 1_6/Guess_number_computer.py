def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    input("Enter The number: ")
    low = 1
    high = 100
    feedback = ''
    attempts = 0

    while feedback != 'c':
        guess = (low + high) // 2
        print(f"My guess is {guess}")
        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

        while feedback not in ['h', 'l', 'c']:
            feedback = input("Please enter 'h' (high), 'l' (low), or 'c' (correct): ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        attempts += 1

    print(f"Yay! I guessed your number in {attempts} tries!")


computer_guess()
