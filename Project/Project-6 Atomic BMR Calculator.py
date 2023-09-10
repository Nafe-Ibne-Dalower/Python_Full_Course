# First time BMR Calculating...
try:
    while 1==1:
        G = input("Your Gender: ")
        if G == "Male" or G == "male":
            x = float(input("Enter Your Weigth(kg): " ))
            y = float(input("Enter Your Age: " ))
            z1 = float(input("Enter Your heigth(Foot): " ))
            z2 = float(input("Enter Your heigth(Inch-If Remains): " ))
            z = (z1*30.48) + (z2*2.54)
            BMRM = 66 + (13.7*x) + (6.8*y) + (5*z)
            print(f"Your BMR is {BMRM}")

        if G == "Female" or G == "female":
            x = float(input("Enter Your Weigth(kg):" ))
            y = float(input("Enter Your Age:" ))
            z1 = float(input("Enter Your heigth(Foot):" ))
            z2 = float(input("Enter Your heigth(Inch-If Remains):" ))
            z = (z1*30.48) + (z2*2.54)
            BMRF = 655 + (9.6*x) + (4.7*y) + (1.8*z)
            print(f"Your BMR is {BMRF}")
except Exception as e:
    print(f"Failed to Calculate Your BMR Because of {e}")

