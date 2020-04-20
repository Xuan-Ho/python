"""
Enter the code and complete the program on the left so that after entering each student name and grade, a table of all
students and grades is output, along with the average grade earned, the highest grade (and who earned it) and the lowest
grade earned (and who earned it). Again, post a screenshot of you with your working output (not the code) to the console.
"""

#init
student = ""
gradebook = {}

print("Enter 'done' to stop entering students.")

#Get students' names and associated grades
while student != "done":
    student = input("Name: ")
    if student != "done":
        grade = int(input("Grade: "))
        gradebook.update({student: grade})
        print("\n", "===Dictionary Results===\n",gradebook, "\n\n")
#

#Sort dictionary and prints the lowest and highest grades with who it belong to

sorted(gradebook)
print("==Low Grade===\n", list(gradebook.items())[0], "\n")
print("==Highest Grade===\n", list(gradebook.items())[-1], "\n")



