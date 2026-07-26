name = input("Enter your name:")
marks = int(input("Enter your marks:"))
print("Name:",name)
if marks >= 80:
  print("Grade:","A+")
elif marks >= 70:
  print("Grade","A")
elif marks >= 60:
  print("Grade:","A-")
elif marks >= 50:
  print ("Grade:","B")
else:
  print("Grade:","F")
