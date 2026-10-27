#Employee class
class Employee:
    def __init__(self,employee_id,name,role,salary):
        self.employee_id=employee_id
        self.name=name
        self.role=role
        self.salary=float(salary)
    def display_details(self):
        print(f"{self.employee_id}-{self.name}-{self.role}-₹{self.salary:.0f}")

#Function to add employee data into file 
def add_employee(employee):
     with open("employee.txt","a")as file:
         file.write (
             f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n"
         )
#Function to read employee data into file 
def read_employees():
    employees=[]
    try:
        with open("employee.txt","r")as file:
         for line in file:
            data=line.strip().split(",")

            if len(data)== 4:
                emp=Employee(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                )
                employees.append(emp)

    except  FileNotFoundError:
        print("Error:employee.txt file not found! ")

    return employees
#Function to get highest salary
def highest_salary(employees):
      if employees:
        return max(employees,key=lambda emp:emp.salary)
      return None
#Function to find employee by role 
def find_employee_by_role(employees,role):
    return[emp for emp in employees if emp.role.lower()==role.lower()]

#Creating Employees
employees_data=[
    Employee("101","Rahul","Python developer",50000),
    Employee("102","Anjali","Tester",45000),
    Employee("103","John","Developer",60000),
    Employee("104","Priya","Tester",48000)

]

# create a file and store a data
with open("employee.txt","w")as file:
    pass

for emp in employees_data:
    add_employee(emp)

#Read employee data
employees=read_employees()

print("==========Employee details==========\n")

for emp in employees:
    emp.display_details()

print("==========Employees with greater than ₹50000 salary==========\n")

for emp in employees:
    if emp.salary>50000:
        print (f"{emp.name}-₹{emp.salary:.0f}")


highest_paid= highest_salary(employees)

print("\n Highest paid employee:\n")

if highest_paid:
    print(f"{highest_paid.name}-₹{highest_paid.salary:.0f}")

role_count={}

for emp in employees:
    role_count[emp.role]=role_count.get(emp.role,0)+1

print("\nEmployee count by role:\n")

for role, count in role_count.items():
    print(f"{role}: {count}")





        



        