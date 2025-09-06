"""Author: -DEREK GERRY- 9-6-25. 'Student Honors'. This Python app will accept student names and GPAs and test if the student qualifies \
    for either the Dean's List or the Honor Roll. Enter, "ZZZ" as the last name to exit the program."""

studentLN = input("Enter the student's last name: ")
if studentLN == "ZZZ":
    print("Exiting the program.")
    exit()
studentFN = input("Enter the student's first name: ")
studentGPA = float(input("Enter the student's GPA: "))      
if studentGPA >= 3.5:
    print(f"{studentFN} {studentLN} has made the Dean's List.")
elif studentGPA >= 3.25:
    print(f"{studentFN} {studentLN} has made the Honor Roll.")
else:
    print(f"{studentFN} {studentLN} has not made the Dean's List or the Honor Roll.")

# End of program

