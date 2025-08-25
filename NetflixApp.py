print("Welcome! to Netflix App")
c_username=input("Enter username: ")
c_password=input("Enter your password: ")
if c_username == user_name and c_password == user_password:
  print("Login Sucessful!")
  break
else:
  print("Login failed!")
  print("If you have forgotten your password, please reset it")
  print("If you don't have an account, please sign up")
  
