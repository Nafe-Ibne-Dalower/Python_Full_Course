# print("Hello World😉😉😉")

# Property Decorator: It is used to call a function as an argument...
# Setter: It is used to set the property value...
# Deletter: It is used to delete an attribute from an object...
# Property Decorator...
class hero():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    @property
    def full_name(self):
        return self.fname + " " + self.lname

Naruto = hero("Naruto", "Uzumaki")
print(Naruto.full_name)

# If I want to change the full name...
Naruto.lname = "Namikaze"
print(Naruto.lname)
print(Naruto.full_name)

# Setter...
class hero():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    @property
    def full_name(self):
        return self.fname + " " + self.lname
    @full_name.setter
    def full_name(self, given_name):
        change_name = given_name.split(" ")
        self.fname = change_name[1]
        self.lname = change_name[0]
       
Sasuke = hero("Sasuke", "Uchiha")
Sasuke.full_name = "Sasuke Uchiha"
print(Sasuke.full_name)

# Deletor...
class medical_nin():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    @property
    def full_name(self):
        if self.fname == None:
            return "Fullname Deleted..."
        else:
            return self.fname + " " + self.lname
    @full_name.deleter
    def full_name(self):
        self.fname = None
        self.lname = None
    
Sakura = medical_nin("Sakura","Harurno")
del Sakura.full_name
print(Sakura.full_name)
# <<<---Property Decorator,Setter & Deleter--->>>