print("Welcome,to Diamond High Internation")
def registration():
    Name=input("Enter your name: ")
    Age=input("Enter your age: ")
    former_school=input("Enter your former school: ")
    acquired=input("Enter your certificate acquired: ")
    print(f'\nname:{Name},age:{Age},Former School:{former_school},Aquired:{acquired}')
class Record():
  def __init__(self,name,age,former_school,acquired):
    self.name=name
    self.age=age
    self.former_school=former_school
    self.acquired=acquired
  def Record_run(self):
    print(f'name:{self.name},age:{self.age},Former School:{self.former_school},Aquired:{self.acquired}')
s1=Record("Maurice",18,"BCK","UCE")
s2=Record('Hellen',20,'UMSSN','UCE')
while True:
    print("\nHow can we help you:")
    print("1. Registration: ")
    print("2. Check my profile ")
    print("3.Edit my records ")
    print("4. Exit program.")

    choice=int(input("Enter choice: "))
    if choice==1:
        print('Please enter the following infomation,correctly')
        registration()
    elif choice==2:
      print("Here is a list of our students")
      s1.Record_run()
      s2.Record_run()

    elif choice == 3:
       pass
    elif choice == 4:
      print("Exit program.")
      break  
    else:
       print("Invalid choice.Please try again.")  
