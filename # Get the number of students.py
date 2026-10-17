n = int(input("Enter number of students: "))
students_list = []
for i in range(1, n + 1):
    print(f"\n----ENTER STUDENT DETAILS {i}---")
    name = input("Enter student name: ")
    usn = input("Enter USN: ")
    mark1 = float(input("Enter marks in Course 1: "))
    mark2 = float(input("Enter marks in Course 2: "))
    mark3 = float(input("Enter marks in Course 3: "))
    total = mark1 + mark2 + mark3
    average = total / 3
    students_list.append([name, usn, mark1, mark2, mark3, total, average])
print("\n" + "="*85)
print(f"{'Name':<15} | {'USN':<12} | {'Course 1':<8} | {'Course 2':<8} | {'Course 3':<8} | {'Total':<8} | {'Average':<8}")
print("="*85)

for student in students_list:
    print(f"{student[0]:<15} | {student[1]:<12} | {student[2]:<8.2f} | {student[3]:<8.2f} | {student[4]:<8.2f} | {student[5]:<8.2f} | {student[6]:<8.2f}")

print("="*85)