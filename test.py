class UserInfo:
    def __init__(self):
        self.name = []
        self.age = []
        self.former_sch = []
    def Records(self):
        # self.check_profile()
        # self.edit_my_rec()
        # self.registration()
        

        while True:
            print("\nSELECT ONE OPTION:")
            print("A. Registration: ")
            print("B. Check my profile ")
            print("C. Edit my records ")
            print("D. Exit program.")
            print("\n-----------------------")
            choice= input("Enter choice: ")
            if choice == "A" or choice == "a":
                print('Please enter the following infomation,correctly')
                self.registration()
            elif choice == "B" or choice == "b":
                print("Here is a list of our students")
                self.check_profile()

            elif choice == "C" or choice == "c":
                pass
            elif choice == "D" or choice == "d":
                print("Thank you for using our application.")
                break  
            else:
                print("Invalid choice.Please try again.")  

        


    def registration(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.former_sch = str(input("Enter your former school: "))
        self.acquired = str(input("Enter your certificate acquired: "))
        
        print("-----------------------------")
        print(f"User Name: {self.name}")
        print(f'User Age: {self.age}')
        print(f"Former School:{self.former_sch}")
        print(f"Aquired:{self.acquired}")
        print("-----------------------------")
        

    def check_profile(self):
        while True:
            pass
        
        


# class Recod(UserInfo):
#     def __init__(self,name,age,former_school,acquired):
#         self.name=name
#         self.age=age
#         self.former_school=former_school
#         self.acquired=acquired
#     def Record_run(self):
#         print(f'name:{self.name},age:{self.age},Former School:{self.former_school},Aquired:{self.acquired}')


if __name__ == "__main__":
    record = UserInfo()
    record.Records()