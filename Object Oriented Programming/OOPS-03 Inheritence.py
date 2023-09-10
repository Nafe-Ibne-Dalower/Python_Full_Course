print("Hello World!😉😉😉")

# Inheritence:
class student():
    def __init__(self, name, age, sec):
        self.name = name
        self.age = age
        self.sec = sec

Nafe = student("Nafe", 15, "C")

class Passed_Student(student):
    def __init__(self, name, age, sec, Passed_year):
        super().__init__(name, age, sec)
        self.Passed_year = Passed_year

Nafe_Passed = Passed_Student("Nafe", 16, "C", 2022)
print(Nafe_Passed.Passed_year)

# <<<---Inheritence--->>>