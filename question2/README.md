Employee Management System
1. Problem Statement

Develop a Python program to manage employee information, including employee ID, name, role, and salary.

The program should:

Store employee details in a text file named employee.txt.
Read employee records from the file and display employee details.
Display employees whose salary is greater than ₹50,000.
Identify the employee with the highest salary.
Count the number of employees in each role.

The objective is to demonstrate employee data management using Python classes, file handling, functions, lists, and dictionaries.

2. Approach and Logic Used
Create Employee Class: Define an Employee class with employee ID, name, role, and salary as attributes. Use the display_details() method to display employee information.
Add Employee Data: Use the add_employee() function to write employee details into employee.txt in comma-separated format.
Read Employee Data: Use the read_employees() function to read records from the file, split each line into individual fields, create Employee objects, and store them in a list.
Display Employee Details: Iterate through the employee list and call display_details() to display each employee's information, including salary in Indian rupees.
Filter Employees by Salary: Use a for loop and an if condition to display employees whose salary is greater than ₹50,000.
Find the Highest-Paid Employee: Use the highest_salary() function with the built-in max() function and a lambda expression to identify the employee earning the highest salary.
Count Employees by Role: Use a dictionary to count employees in each role. The get() method updates the count for each role.
Handle File Errors: Use try-except to handle the FileNotFoundError exception when the employee file is unavailable.
3. How to Run the Program
Prerequisites
Python 3 must be installed on your system.
A code editor or terminal to execute the Python program.
Execution Steps
Save the program in a file named employee.py.
Open a terminal or command prompt in the folder where the file is saved.
Execute the following command:
bash
python main.py

The program creates or clears employee.txt and writes the predefined employee records to the file.
The program reads the records and displays employee details, employees earning above ₹50,000, the highest-paid employee, and employee counts by role.

Note: The current program uses write mode ("w") to clear the existing file each time it runs. It then writes the four predefined employee records into the file.

4. Sample Input

The program uses predefined employee data, so no manual input is required.

python
employees_data = [
    Employee("101", "Rahul", "Python developer", 50000),
    Employee("102", "Anjali", "Tester", 45000),
    Employee("103", "John", "Developer", 60000),
    Employee("104", "Priya", "Tester", 48000)
]


The employee records are stored in employee.txt in the following format:

text
101,Rahul,Python developer,50000.0
102,Anjali,Tester,45000.0
103,John,Developer,60000.0
104,Priya,Tester,48000.0

5. Sample Output
text
==========Employee details==========

101-Rahul-Python developer-₹50000
102-Anjali-Tester-₹45000
103-John-Developer-₹60000
104-Priya-Tester-₹48000

==========Employees with greater than ₹50000 salary==========

John-₹60000

 Highest paid employee:

John-₹60000

Employee count by role:

Python developer: 1
Tester: 2
Developer: 1

6. Python Concepts Used
Classes and Objects: The Employee class represents employee records, and individual employees are created as objects.
Constructor (__init__): Initializes employee attributes when an object is created.
Instance Methods: The display_details() method displays employee information.
Functions: Functions such as add_employee(), read_employees(), and highest_salary() perform specific tasks.
File Handling: Uses open() with "w", "a", and "r" modes to write, append, and read employee data.
Exception Handling: Uses try-except to handle missing files.
Lists: Stores employee objects and supports iteration over employee records.
Lambda Functions: Uses lambda emp: emp.salary to select the employee with the highest salary.
List Comprehension: The find_employee_by_role() function uses list comprehension to filter employees by role.
Dictionaries: Uses role_count to count employees in each role.
Dictionary Methods: Uses get() to retrieve and update role counts.
Conditional Statements: Uses if to filter employees earning more than ₹50,000.
For Loops: Iterates through employee records and role counts.
String Methods: Uses strip(), split(), and lower() to process file data and compare roles.
Formatted Strings (f-strings): Displays employee details and salary values in a readable format.
Type Conversion: Uses float() to store salary as a numeric value.
