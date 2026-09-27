#   NAME: Denis O. Onduso   
#   ID: 250466BSIT
class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks  
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0.0
        return sum(self.marks) / len(self.marks)
    def get_letter_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
students_list = []
print("=============STUDENT GRADING SYSTEM=======================")
num_students = int(input("How many students do you want to add? "))
for i in range(num_students):
    print(f"\n--- Entering details for Student #{i + 1} ---")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    num_marks = int(input(f"How many subjects does {name} have? "))
    marks = []
    for j in range(num_marks):
        mark = float(input(f"  Enter mark for subject {j + 1}: "))
        marks.append(mark)
    new_student = Student(name, student_id, marks)
    students_list.append(new_student)
print("\n================= STUDENT RESULT REPORT ================")
total_class_average = 0
for student in students_list:
    avg = student.calculate_average()
    grade = student.get_letter_grade()
    print("ID:", student.student_id, "| Name:", student.name, "| Average:", avg, "| Grade:", grade)
    total_class_average = total_class_average + avg
print("---------------------------------")
class_average = total_class_average / len(students_list)
print("Total Students:", len(students_list))
print("Overall Class Average:", class_average)
