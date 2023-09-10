while 2==2:
    import random
    c_n = int(random.randint(1,1000))
    u_n = int(input("Enter the number(1 to 1000): "))

    if c_n == u_n:
        print(f"Nafe guessed {c_n}.\nYou guessed {u_n}.\nYou won😅😅😅-----🤔🤔")

    if c_n != u_n:
        print(f"Nafe guessed {c_n}.\nYou guessed {u_n}.\nYou lost. None can defeat me so easily...😏😏😏")
# <<<---Number Guessing Game--->>>