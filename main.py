def main():
    # Read the number of students
    N = int(input("enter the number of students:"))

    # Initialize an empty list to store student data
    student_data = []

    # Read student names and grades
    for i in range(N):
        name = input()
        grade = float(input())
        student_data.append([name, grade])

    # Find the second lowest grade
    unique_grades = set(grade for _, grade in student_data)
    sorted_grades = sorted(unique_grades)
    second_lowest_grade = sorted_grades[1]

    # Get names of students with the second lowest grade
    second_lowest_students = [name for name, grade in student_data if grade == second_lowest_grade]
    second_lowest_students.sort()  # Sort alphabetically

    # Print the names
    for student in second_lowest_students:
        print(student)

if __name__ == "__main__":
    main()
#This is My first repo. Edit as per you need. 
