total = 0
count = 0
i = 1
while i <= 5:
  number = int(input("Enter your number:"))

  total = total + number
  count = count + 1
  i = i+1

average = total / count

print("Average", average)
  