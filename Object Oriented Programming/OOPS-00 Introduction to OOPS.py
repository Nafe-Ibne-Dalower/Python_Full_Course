print("Hello World!😉😉😉")
# ✨✨✨Object Oriented Programming
# Witout OOPS--- 12 Lines
class student():
    pass
Nafe = student()
Jimam = student()
print(Nafe, Jimam)

# Nafe
Nafe.name = "Nafe"
Nafe.sec = "C"
Nafe.age = 15

# Jimam
Jimam.name = "Jimam"
Jimam.age = 10
Jimam.sec = "A"

print(Nafe.name , Jimam.name)

# With OOPS--- 9 Lines
class student(): # Class = Student---Template
    def __init__(self, name, age, sec):
        self.name = name
        self.age = age
        self.sec = sec

Nafe = student("Nafe", 15, "C") # Nafe is an Object
Jimam = student("Jimam", 10, "A") # Jimam is an Object

print(Nafe.name, Nafe.age, Nafe.sec)
print(Jimam.name, Jimam.age, Jimam,sec)

# <<<---Object Oriented Programming--->>>