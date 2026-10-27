Student Grade Calculation System
1. Problem Statement

Develop a Python program to calculate student results based on marks obtained in three subjects: Python, SQL, and Artificial Intelligence (AI).

The program should:

Accept the number of students and their details, including student ID, name, and subject marks.
Calculate the total marks and average for each student.
Assign grades based on the average marks.
Determine whether each student has passed or failed.
Display the results of all students.
Identify the highest-scoring student.
Display the names of students whose average is above 75.
Grading Criteria
Average Marks	Grade
75 and above	A
60 to below 75	B
40 to below 60	C
Below 40	F

Pass Criteria: Average marks greater than or equal to 40 indicate a pass; otherwise, the student fails.

2. Approach and Logic Used
Input Student Details: Ask the user to enter the number of students, followed by each student's ID, name, and marks in Python, SQL, and AI.
Calculate Total and Average: Add the marks obtained in the three subjects and divide the total by 3 to calculate the average.
Calculate Grade: Use the gradecalculation() function and conditional statements to assign a grade based on the average.
Determine Result: If the average is greater than or equal to 40, assign the result as Pass; otherwise, assign Fail.
Store Student Records: Store each student's details, marks, total, average, grade, and result in a dictionary. Append each dictionary to the students list.
Display Student Results: Use the studentdetails() function to display each student's result in a structured format.
Find the Highest-Scoring Student: Use the max() function with a lambda expression to identify the student with the highest average.
Find Students Above 75 Average: Use a list comprehension to collect the names of students whose average is strictly greater than 75. Display their names using join().
3. How to Run the Program
Prerequisites
Python 3 must be installed on your system.
A code editor or terminal to execute the Python program.
Execution Steps
Save the program in a file named student_grade.py.
Open a terminal or command prompt in the folder where the file is saved.
Execute the following command:
bash
python main.py

Enter the number of students.
Provide the student ID, name, and marks for each subject when prompted.
View the student results, highest-scoring student, and list of students with an average above 75.
4. Sample Input
text
Enter number of students:3

 Enter details of the student 1 :
Enter Student id:101
Enter Student name:Uma
Python marks:12
SQL  marks:23
Ai marks:45

 Enter details of the student 2 :
Enter Student id:102
Enter Student name:Akshaya
Python marks:78
SQL  marks:67
Ai marks:67 

 Enter details of the student 3 :
Enter Student id:103
Enter Student name:thabi
Python marks:89
SQL  marks:90
Ai marks:80

5. Sample Output
text

======Student Summary=======

====Student Result====
Student Id:101
Name:Uma
Total:80
Average:26.67
Grade:F
Result:Fail

====Student Result====
Student Id:102
Name:Akshaya
Total:212
Average:70.67
Grade:B
Result:Pass

====Student Result====
Student Id:103
Name:thabi
Total:259
Average:86.33
Grade:A
Result:Pass

-------------------------------------------------------
Highest Scoring Student: thabi
Highest Average 86.33
students above 75 average: thabi

6. Python Concepts Used
Functions: Used gradecalculation() to calculate grades and studentdetails() to display student results.
Conditional Statements (if, elif, else): Used to assign grades and determine pass/fail status.
For Loop: Used to collect student details and display the results of all students.
Lists: Used to store multiple student records in the students list.
Dictionaries: Used to store each student's ID, name, subject marks, total, average, grade, and result.
Lambda Function: Used with max() to identify the student with the highest average.
List Comprehension: Used to find students whose average is above 75.
Built-in Functions: Used int(), max(), round(), and join() for input conversion, finding the highest average, rounding values, and formatting names.
Formatted Strings (f-strings): Used to display student details and calculated results.
Arithmetic Operators: Used addition and division to calculate total marks and average.

