def gradecalculation(avg):
    if avg >=75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 40:
        return 'C'
    else:
        return 'F'

def studentdetails(student):
    print("\n====Student Result====")
    print(f"Student Id:{student['Id']}")
    print(f"Name:{student['Name']}")
    print(f"Total:{student['Total']}")
    print(f"Average:{student['Average']:.2f}")
    print(f"Grade:{student['Grade']}")
    print(f"Result:{student['Result']}")


students=[]
n=int(input("Enter number of students:"))
for i in range(n):
    print(f"\n Enter details of the student {i+1} :")
    studid=input("Enter Student id:")
    studname=input("Enter Student name:")

    python_marks= int(input("Python marks:"))
    sqlmarks= int(input("SQL  marks:"))
    ai_marks=int(input("Ai marks:"))

    total=python_marks+sqlmarks+ai_marks
    average=total/3

    grade=gradecalculation(average)

    if average >=40:
        result="Pass"
    else:
        result="Fail"

    student={
        "Id":studid,
        "Name":studname,
        "Python":python_marks,
        "SQLMarks":sqlmarks,
        "AIMarks":ai_marks,
        "Total":total,
        "Average":average,
        "Grade":grade,
        "Result":result
    }
    students.append(student)

print("\n\n======Student Summary=======")

for student in students:
    studentdetails(student)

highest_student=max(students,key=lambda s: s["Average"])


print("\n-------------------------------------------------------")
print("Highest Scoring Student:",highest_student["Name"])
print("Highest Average",round(highest_student["Average"],2))

top_students=[student["Name"] for student in students
             if student ["Average"]>75]
print("students above 75 average:",",".join(top_students))


    
    