class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last name: "+self.last_name)
        print("Eye color: "+self.eye_color)
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    # method overriding xuat hien khi class con ton tai method cung ten
    # va cung so luong tham so method cua class cha, o day la show_info
    def show_info(self):
        print("Last name: "+self.last_name)
        print("Eye color: "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))


billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
miley_cyrus.show_info()

