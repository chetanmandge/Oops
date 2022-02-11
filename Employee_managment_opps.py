dB = []


class employee_managment():
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def Add_employe(self):
        u_name = input("Enter employee Name :-")
        u_id = input('Enter employee ID :-')
        u_dept = input("Enter employee department :-")

        e2 = employee_managment(u_name, u_id, u_dept)
        dB.append(e2)
        print(f"Employee {u_name} added successfully")

    def display_employee(self):
        for i in range(len(dB)):
            print("Employee name is :-", dB[i].name)
            print("Employee id is :-", dB[i].id)
            print("Employee dept is :-", dB[i].dept)

    def search_employee(self):
        nam = input("enter employee name you want to find :-")
        for i in range(len(dB)):
            if dB[i].name == nam:
                print("found employee in Database")
                return True
            else:
                print("employee not found in dB")
                return False

    def update_employee(self):
        u_name = input("Enter updated employee Name :-")
        u_id = input('Enter  updated employee ID :-')
        u_dept = input("Enter updated employee department :-")

e1 = employee_managment("chetan", 201, 'etc')
dB.append(e1)
obj = employee_managment("", 0, "")
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
        obj.Add_employe()
    elif ch == 2:
        result= obj.search_employee()
        if(result== True):
            obj.update_employee()

    elif ch == 3:
        obj.display_employee()
    elif ch == 4:

        pass
    elif ch == 5:
        obj.search_employee()
    elif ch == 6:
        break
    else:
        print("You have enter invalid input")

    choice = input("Do you want to continue Y/N :-")
    choice.lower()
    if (choice == 'n'):
        break
