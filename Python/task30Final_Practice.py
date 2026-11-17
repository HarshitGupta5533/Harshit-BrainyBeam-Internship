
# Student Performance Analysis

students = [
    {"name": "Aarav", "age": 21, "course": "Python", "marks": 90},
    {"name": "Priya", "age": 20, "course": "Data Science", "marks": 76},
    {"name": "Rahul", "age": 22, "course": "Java", "marks": 95},
    {"name": "Neha", "age": 19, "course": "Python", "marks": 60},
    {"name": "Karan", "age": 23, "course": "Data Science", "marks": 82},
    {"name": "Sneha", "age": 21, "course": "Java", "marks": 68}
]

def total_students():
    print("Total Students:", len(students))

def average_marks():
    total = 0

    for s in students:
        total = total + s["marks"]

    average = total / len(students)
    print("Average Marks:", round(average, 2))



def highest_marks():
    marks = []

    for s in students:
        marks.append(s["marks"])

    print("Highest Marks:", max(marks))



def lowest_marks():
    marks = []

    for s in students:
        marks.append(s["marks"])

    print("Lowest Marks:", min(marks))



def passed_students():
    count = 0

    for s in students:
        if s["marks"] >= 75:
            count = count + 1

    print("Passed Students:", count)



def failed_students():
    count = 0

    for s in students:
        if s["marks"] < 75:
            count = count + 1

    print("Failed Students:", count)



def above_75():
    print("Students Above 75:")

    for s in students:
        if s["marks"] > 75:
            print(s["name"], s["marks"])



def highest_student():
    highest = students[0]

    for s in students:
        if s["marks"] > highest["marks"]:
            highest = s

    print("Highest Student:", highest["name"], highest["marks"])



def lowest_student():
    lowest = students[0]

    for s in students:
        if s["marks"] < lowest["marks"]:
            lowest = s

    print("Lowest Student:", lowest["name"], lowest["marks"])


def display_students():
    print("All Student Records:")

    for s in students:
        print(s["name"], s["age"], s["course"], s["marks"])



total_students()
average_marks()
highest_marks()
lowest_marks()
passed_students()
failed_students()
above_75()
highest_student()
lowest_student()
display_students()
