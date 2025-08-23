name=input("WELCOME! Please enter your name: ")
print("Hello"+" "+ name)
weight =input("Enter your weight in Kgs: ")
height =input("Enter your heights in meters: ")
BMI = float(weight)/float(height)**2
print(BMI)
if BMI<=18.5:
    print(name + "You are Under weight")
elif BMI<24.9:
    print(name+" " + "You are healthy")
elif BMI<29:
       print(name +" " + "You are overweight")
elif BMI<35:
     print(name+" " + "Your are Obese")
elif print(name+" " + "Your are HIGHLY Obese"):
     print("Enter valid values")
