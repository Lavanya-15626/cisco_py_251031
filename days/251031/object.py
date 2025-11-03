
Employees = []  
class Employee:
    def __init__(self,id,name,domain,salary):
        self.id=id
        self.name=name
        self.domain=domain
        self.salary=salary
        
def add_employee(id, name, domain, salary):
    employee = Employee(id,name,domain,salary)                
    Employees.append(employee)
    print("Employee Added Successfully")
    print(Employees)

def search_employee(id):
    for i, emp in enumerate(Employees):       
        if emp["id"] == id:                   
            print(f" Index of the Employee in list of Employees is {i}")
            print(emp)
            return i
    print(" Employee not found..")
    return -1

def update_employee():
    id = int(input("Enter Employee Id to update: "))  
    index = search_employee(id)                       

    if index != -1:                                    
        name = input("Enter Updated name: ")
        domain = input("Enter Updated domain: ")
        salary = float(input("Enter Updated salary: "))  

        Employees[index]["name"] = name
        Employees[index]["domain"] = domain
        Employees[index]["salary"] = salary

        print("Employee details updated successfully...")
        print(Employees[index])
    else:
        print("Employee not found..")              

def delete_employee():                                
    id = int(input("Enter Employee Id to delete: "))
    index = search_employee(id)

    if index != -1:
        deleted = Employees.pop(index)                
        print(f"Employee deleted successfully: {deleted['name']}")
        print(Employees)
    else:
        print(" Employee not Found")                 

#Menu Driven
while True:
    print("****** Employee Management System ******")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")              

    if choice == "1":                                  
        id = int(input("Enter Employee Id: "))
        name = input("Enter Employee name: ")
        domain = input("Enter Employee Domain: ")
        salary = float(input("Enter Salary of the Employee: "))
        add_employee(id, name, domain, salary)

    elif choice == "2":
        id = int(input("Enter Employee Id: "))
        search_employee(id)

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank You")
        break
    else:
        print(" Invalid Choice.. Try Again")