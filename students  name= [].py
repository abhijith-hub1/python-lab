students = []
n = int(input("Enter the number of students: "))

# Accept details of all students
for i in range(n):
    print(f"\nEnter details of Student {i + 1}")
    name = input("Enter student name: ")
    usn = input("Enter USN: ")

    mark1 = float(input("Enter marks in Course 1: "))
    mark2 = float(input("Enter marks in Course 2: "))
    mark3 = float(input("Enter marks in Course 3: "))

    total = mark1 + mark2 + mark3
    average = total / 3

    # Store student details in a list
    students.append([name, usn, mark1, mark2, mark3, total, average])

# Display table after accepting all inputs
print("\n" + "=" * 94)
print("                                 STUDENT MARKS REPORT")
print("=" * 94)

print(
    f"{'Name':<15} {'USN':<15} {'Course 1':>10} "
    f"{'Course 2':>10} {'Course 3':>10} "
    f"{'Total':>10} {'Average':>10}"
)

print("-" * 94)

for student in students:
    name, usn, m1, m2, m3, total, avg = student
    print(
        f"{name:<15} {usn:<15} {m1:>10.2f} "
        f"{m2:>10.2f} {m3:>10.2f} "
        f"{total:>10.2f} {avg:>10.2f}"
    )

print("=" * 94)
