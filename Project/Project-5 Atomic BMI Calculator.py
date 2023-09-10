# BMI Calculator
try:
    while 10==10:
        x = float(input("Enter Your Weigth(kg):" ))
        y1 = float(input("Enter Your heigth(Foot):" ))
        y2 = float(input("Enter Your heigth(Inch-If remains):" ))
        
        y = (y1*0.3048) + (y2*0.0254)
        BMI = x/(y*y)
        print(f"Your BMI is {BMI}")
except Exception as e:
    print(f"Failed to Calculate Your BMI because of {e}")
