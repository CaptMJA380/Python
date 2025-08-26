user_name = input("Enter your name: ")
user_password = input("Enter your password: ")

print("Welcome! to Netflix App")

for i in range(1,4):
  c_username=input("Enter username: ")
  c_password=input("Enter your password: ")
  if c_username == user_name and c_password == user_password:
    print("Login Sucessful!")
    break
  else:
    print("Login failed!")
    print("If you have forgotten your password, please reset it")
    print("If you don't have an account, please sign up")
  
print("Welcome! to Netflix")
print("Choose the plan that suits you best: \n 1. Basic Plan \n 2. Standard Plan \n 3. Preminum Plan")
plan_chaoice = input("Enter the number option of your chosen plan")
if plan_choice=="1":
    print("You have chosen Basic Plan")
elif plan_choice=="2":
    print("You have chosen Standard Plan")
elif plan_choice=="3":
    print("You have chosen Premium Plan")
else:
    print("Enter valid option!")

movies = ["Inception","The Matrix","Interatellar","Fighter","Piku"]
print("available movies: ")
for movie in movies:
  print(f"- {movies}")
  
