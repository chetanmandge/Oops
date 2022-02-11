dB = []


class employee_managment():
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept


e1 = employee_managment("chetan", 201, 'etc')
dB.append(e1)

while 1:
    print("             Welcome to employee management system ")
    print('''   
                            ||Menu||
                            1.Add employee
                            2.Update 
                            3.Display
                            4.delete
                            5.Search
                            6.Exit            
            ''')
    ch = int(input("Enter your choice for employee :-"))
    if ch == 1:
        pass
    elif ch == 2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch== 5:
        pass
    elif ch == 6:
        break
    else:
        print("You have enter invalid input")

    choice = input("Do you want to continue Y/N :-")
    choice.lower()
    if(choice == 'n'):
        break