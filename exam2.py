name = input("Enter your name:")
age = int(input("Enter your age:"))
temperature = float(input("Enter todays temperature:"))

if age >= 18:
  print("You are eligible for NID")

else:
  print("You are not eligible for NID")

if temperature >= 30:
  print("It is HOT")

else:
  print("It is COOL")

print("Thank you,", name)