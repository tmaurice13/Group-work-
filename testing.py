import csv

class StudentRegister:
    def __init__(self):
        self.students = {}

    def register_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        self.students[student_id] = {'name': name, 'age': age}

    def display_students(self):
        with open('student_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'Name', 'Age'])
            for student_id, info in sorted(self.students.items(), key=lambda x: x[0]):
                writer.writerow([student_id, info['name'], info['age']])
            print("Student data saved to student_data.csv")

    def edit_student(self):
        student_id = input("Enter the student ID you want to edit: ")
        if student_id in self.students:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            self.students[student_id] = {'name': name, 'age': age}
        else:
            print("Student not found.")

    def delete_student(self):
        student_id = input("Enter the student ID you want to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted.")
        else:
            print("Student not found.")

    def search_student(self):
        student_id = input("Enter the student ID you want to search for: ")
        if student_id in self.students:
            print(f"Student ID: {student_id}, Name: {self.students[student_id]['name']}, Age: {self.students[student_id]['age']}")
        else:
            print("Student not found.")
    
    def run_register(self):
        while True:
            print("\n1. Register student\n2. Display students\n3. Edit student\n4. Delete student\n5. Search student\n6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.register_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.edit_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.search_student()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

register = StudentRegister()
register.run_register()