import matplotlib.pyplot as plt


# Define a class StudentRegister to encapsulate functionalities related to student registration
class StudentRegister:
    # Constructor method to initialize the class with an empty dictionary for storing student information
    def __init__(self):
        self.students = {}

    # Method to register a new student by taking user input for student ID, name, and age
    def register_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        
        # Store the entered student information in the 'students' dictionary
        self.students[student_id] = {'name': name, 'age': age}

    # Method to display the list of registered students
    def display_students(self):
        for student_id, info in self.students.items():
            # Print the student ID, name, and age for each student in the 'students' dictionary
            print(f"Student ID: {student_id}, Name: {info['name']}, Age: {info['age']}")

    # Method to edit a student's information based on the provided student ID
    def edit_student(self):
        student_id = input("Enter the student ID you want to edit: ")
        
        if student_id in self.students:
            # Take user input for new name and age, and update the student information in the 'students' dictionary
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            self.students[student_id] = {'name': name, 'age': age}
        else:
            # Print message if student ID is not found in the 'students' dictionary
            print("Student not found.")

    # Method to delete a student's information based on the provided student ID
    def delete_student(self):
        student_id = input("Enter the student ID you want to delete: ")
    
        if student_id in self.students:
            # Remove the student information from the 'students' dictionary
            del self.students[student_id]
        else:
            # Print message if student ID is not found in the 'students' dictionary
            print("Student not found.")

    # Method to search for a student by student ID
    def search_student(self):
        student_id = input("Enter the student ID you want to search for: ")
        
        if student_id in self.students:
            # Display the student information (name and age) for the provided student ID
            print(f"Student ID: {student_id}, Name: {self.students[student_id]['name']}, Age: {self.students[student_id]['age']}")
        else:
            # Print message if student ID is not found in the 'students' dictionary
            print("Student not found.")


    def gardes(self):
        labels=['2022','2023']
        sizes = [30,40]
        colors = ['gold', 'yellowgreen']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

        plt.axis('equal') 
        plt.title('past first grades')
        plt.show()



    # Method to run the student register program by continuously prompting the user for actions
    def run_register(self):
        # Display menu options for user interaction
        while True:
            print("\n1. Register student\n2. Display students\n3. Edit student\n4. Delete student\n5. Search student\n6. Past year grades \n7. Exit")
            # Prompt user for input choice
            choice = input("Enter your choice: ")
            
            # Perform actions based on user choice
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
                self.gardes()
            elif choice == '7':
                break
            else:
                # Print message for invalid user choice
                print("Invalid choice. Please try again.")

# Create an instance of the StudentRegister class
register = StudentRegister()
# Invoke the run_register method to start the program
register.run_register()



labels=['2021','2022','2023']
sizes = [30,40,20]
colors = ['gold', 'red','orange']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal') 
plt.title('past first grades')
plt.show()