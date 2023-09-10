print("Hello World!😉😉😉")
# ✨✨✨Object Oriented Programming

# Class is a template...
# object is an instance of the class...
# Class & Object:
class student(): # Class = Student---Template
    pass
Nafe = student() # Here "Nafe" is an Object...
Jimam = student() # Here "Nafe" is an Object...
print(Nafe, Jimam)

# Nafe
Nafe.name = "Nafe"
Nafe.age = 15
Nafe.sec = "C"

# Jimam
Jimam.name = "Jimam"
Jimam.age = 10
Jimam.sec = "A"

print(Nafe.name , Jimam.name)

# Instance & Constructor:
class student(): 
    def __init__(self, name, age, sec): # Constructor
        self.name = name # Instance
        self.age = age # Instance
        self.sec = sec # Instance

Nafe = student("Nafe", 15, "C")
Jimam = student("Jimam", 10, "A")

print(Nafe.name, Nafe.age, Nafe.sec)
print(Jimam.name, Jimam.age, Jimam,sec)
 
# <<<---Class, Object,Instance & Constructors--->>>