while 2==2:
    import random
    import string

    alpha = list(string.ascii_uppercase)
    alpha_set = set(alpha)
    # Computer's Choice
    c_a = random.choice(alpha)

    # User's Choice...
    u_a_pre = input("Choose an Alphabet(Uppercase): ") # Input
    u_a = u_a_pre.upper() # Upper

    # Making Set...
    u_a_set = set(u_a)

    # Conditions...w
    if u_a_set.issubset(alpha_set) == False:
        print(f"You guessed {u_a_pre} which isn't alphabet...\nPlease Enter a number...")

    if u_a_set.issubset(alpha_set) != False:
        if c_a == u_a:
            print(f"Nafe guessed {c_a}.\nYou guessed {u_a}.\nYou won😅😅😅-----🤔🤔")
        if c_a != u_a:
            print(f"Nafe guessed {c_a}.\nYou guessed {u_a}.\nYou lost. None can defeat me so easily...😏😏😏")
# <<<---Alphabet Guessing Game--->>>