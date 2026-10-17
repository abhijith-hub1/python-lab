# Student Marks Program
# Reads name, USN, and marks for 3 courses, then displays total and average.

def read_marks(subject_num):
    """Reads and validates marks for a subject."""
    while True:
        try:
            marks = float(input(f"Enter marks for Course {subject_num} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def main():
    # Read student details
    name = input("Enter Student Name: ").strip()
    usn = input("Enter USN: ").strip()

    # Read marks for 3 courses
    marks = [read_marks(i + 1) for i in range(3)]

    # Calculate total and average
    total = sum(marks)
    average = total / 3

    # Display in formatted table
    print("\n" + "=" * 50)
    print(f"{'Student Details':^50}")
    print("=" * 50)
    print(f"{'Name':<15}: {name}")
    print(f"{'USN':<15}: {usn}")
    print("-" * 50)
    print(f"{'Course 1':<15}{'Course 2':<15}{'Course 3':<15}")
    print(f"{marks[0]:<15}{marks[1]:<15}{marks[2]:<15}")
    print("-" * 50)
    print(f"{'Total Marks':<15}: {total:.2f}")



    
    print(f"{'Average Marks':<15}: {average:.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()
