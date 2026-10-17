n=int(input("enter number of students:"))
for i in range(1, n+1):
    print(f"\n----ENTER STUDENT DETAILS {i}---")
    
    name = input("Enter student name: ")
    usn = input("Enter USN: ")
    mark1 = float(input("Enter marks in Course 1: "))
    mark2 = float(input("Enter marks in Course 2: "))
    mark3 = float(input("Enter marks in Course 3: "))
    total = mark1 + mark2 + mark3
    average = total /3
    