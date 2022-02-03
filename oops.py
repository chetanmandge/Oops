
class Students:
    company_nam e ='Flash electronics'   # this is class/ static variable
    def __init__(self, name, roll, marks): # in init function the number of veriable you have to pass this is called local variable
        self.name = name # self.name,self.roll,self.marks is instance variable
        self.roll = roll
        self.marks = marks
    @classmethod  # class method access by class name only
    def display(cls):
        print(f"company name is {cls.company_name} ")

    @staticmethod
    def add_num(num1 ,num2):
        print(f"addition of {num1} and {num2} is {num2 +num1} ")


s1 = Students('chetan' ,3 ,56)
Students.display()
Students.add_num(1 ,8)

s2 = Students('nilu' ,34 ,99)
