name = input("Enter your name:")
age = int(input("Enter your age:"))

print("======Age REPORT======")
print("Name:",name)
if age >= 60:
  print("Category:","Senior Citizen")
elif age >= 18:
  print("Category:","Adult")
elif age >= 13:
  print("Category:","Teenage")
else:
  print("Category:","Child")

print("======================")