name = input("Enter your name:")
bmi = float(input("Enter your BMI:"))

print("====== BMI REPORT ======")
print("Name:", name)
print("BMI:", bmi)
if bmi >= 25:
  print("Category:", "Overweight")
elif bmi >= 18.5:
  print("Category:", "Normal")
else:
  print("Category:", "Unerweight")
print("========================")