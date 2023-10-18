class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students_ascending(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa)
    return sorted_students

# Example usage:
students = [
    Student("vel", "A123", 3.5),
    Student("antho", "B456", 3.8),
    Student("thiru", "C789", 3.2),
    Student("lokesh", "D234", 3.9),
]

sorted_students_ascending = sort_students_ascending(students)

print("Sorted Students by CGPA (Ascending Order):")
for student in sorted_students_ascending:
    print(student)