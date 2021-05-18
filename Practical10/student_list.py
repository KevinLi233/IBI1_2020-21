#set a new class student
class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.programme = ""
    #set first name
    def set_first_name(self, firstname):
        self.first_name = firstname
    #set last name
    def set_last_name(self, lastname):
        self.last_name = lastname
    #set programme
    def set_programme(self, pro):
        self.programme = pro

    def print_data(self):
        print(self.first_name + " " + self.last_name + "'s undergraduate programme is " + self.programme)

# example
stu = Student()
stu.set_first_name("Silver")
stu.set_last_name("Ash")
stu.set_programme("BMI")
stu.print_data()