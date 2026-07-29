print("===== Student Result System =====")
count = 0
while True :
  name = input("Enter student name:")
  Id = input("Enter student ID:")

  count = count + 1

  bangla = int(input("Enter bangla mark:"))
  english = int(input("Enter english mark:"))
  physics = int(input("Enter physics mark:"))
  chemistry = int(input("Enter chemistry mark:"))
  math = int(input("Enter math mark:"))
  total = bangla + english + physics + chemistry + math
  average = total / 5
  print("Student Name:", name)
  print("Student ID:", Id)

  print()

  print("Bangla:", bangla)
  print("English:", english)
  print("Physics:", physics)
  print("Chemistry:", chemistry)
  print("Math:", math)

  print()

  print("Total:", total)
  print("Average:", average)

  print()

  if average >= 80:
    print("Grade:", "A+")
    print("Result:", "Pass")
  elif average >= 70:
    print("Grade:", "A")
    print("Result:", "Pass")
  elif average >= 60:
    print("Grade:", "A-")
    print("Result:", "Pass")
  elif average >= 50:
    print("Grade:", "B")
    print("Result:", "Pass")
  elif average >= 40:
    print("Grade:", "C")
    print("Result:", "Pass")
  elif average >= 33:
    print("Grade:", "D")
    print("Result:", "Pass")
  else:
    print("Grade:", "F")
    print("Result:", "Fail")

  choice = input("Add another student? (yes/no): ")
  if choice == "no":
    break

print("Total Student:", count)