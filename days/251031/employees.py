employees=[]
def adding_employee(employee):
    employees.append(employee)
    print("Employee added")
def search_employee(id):
    I=0
    for i in employees:
        if i[0]==id:
            return I
        I+=1
    return -1
def deleting_employee(id):
    index=search_employee(id)
    if index!=-1:
        employees.pop(index)
        print("Employee Deleted Successfully")
    else:
        print("Employee not found")
def update_employee(id,salary):
    index=search_employee(id)
    if index!=-1:
        employee=employees[index]
        new_employee=(employee[0],employee[1],employee[2],salary)
        employees[index]=new_employee
        print("Employee details updated successfully")
    else:
        print('Employee not found')
adding_employee(101,"lavanya","Consulting Engineer Trainee",33000)
adding_employee(102,"Kiran","Associate ML Data Operations",33000)
adding_employee(103,"Iram","Technical Consulting Engineer Trainee",33000)
adding_employee(104,"Tharun","Software Engineer Trainee",33000)
adding_employee(105,"lavanya","Consulting Engineer Trainee",33000)
search_employee(101)
deleting_employee(105)
update_employeee(101,35000)
