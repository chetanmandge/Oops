print('hello')


class Students:
    company_name='Flash electronics'
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"student name is {self.name} marks is {self.marks} and roll number is {self.roll}")


s1 = Students('chetan',3,56)
s1.display()
print(Students.company_name)

s2 = Students('nilu',34,99)
s2.display()