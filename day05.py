bangla = float(input("Enter your Bangla number: "))
english = float(input("Enter your English number: "))
math = float(input("Enter your Math number: "))
science = float(input("Enter your Science number: "))
ict = float(input("Enter your ICT number: "))

obtaind_all_subject_mark_tot = (bangla + english + math + science + ict )

average_marks = (obtaind_all_subject_mark_tot / 5 )

percentage = (obtaind_all_subject_mark_tot / 500) *100

print("Total Marks: ", obtaind_all_subject_mark_tot)

print("Average Marks: ",average_marks )

print("Percentage: ", percentage, "%")

