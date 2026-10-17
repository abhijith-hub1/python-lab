students = []

n = int(input(&quot;Enter the number of students: &quot;))

# Accept details of all students
for i in range(n):
print(f&quot;\nEnter details of Student {i + 1}&quot;)

name = input(&quot;Enter student name: &quot;)
usn = input(&quot;Enter USN: &quot;)

mark1 = float(input(&quot;Enter marks in Course 1: &quot;))
mark2 = float(input(&quot;Enter marks in Course 2: &quot;))
mark3 = float(input(&quot;Enter marks in Course 3: &quot;))

total = mark1 + mark2 + mark3
average = total / 3

# Store student details in a list
students.append([name, usn, mark1, mark2,
mark3, total, average])

# Display table after accepting all inputs
print(&quot;\n&quot; + &quot;=&quot; * 94)
print(&quot; STUDENT MARKS REPORT&quot;)
print(&quot;=&quot; * 94)

print(f&quot;{&#39;Name&#39;:&lt;15} {&#39;USN&#39;:&lt;15} {&#39;Course 1&#39;:&gt;10} &quot;
f&quot;{&#39;Course 2&#39;:&gt;10} {&#39;Course 3&#39;:&gt;10} &quot;
f&quot;{&#39;Total&#39;:&gt;10} {&#39;Average&#39;:&gt;10}&quot;)

print(&quot;-&quot; * 94)

for student in students:
name, usn, m1, m2, m3, total, avg = student

print(f&quot;{name:&lt;15} {usn:&lt;15} {m1:&gt;10.2f} &quot;
f&quot;{m2:&gt;10.2f} {m3:&gt;10.2f} &quot;
f&quot;{total:&gt;10.2f} {avg:&gt;10.2f}&quot;)

print(&quot;=&quot; * 94)