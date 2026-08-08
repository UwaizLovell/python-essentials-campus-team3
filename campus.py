# =====================================
# Melsoft Campus Manager
# Python Essentials 1 - Capstone Project
# =====================================


# ==========================
# Helper Functions
# ==========================

# Reads and validates a whole number within a given range.
def read_valid_number(prompt, minimum, maximum):

    # Keep asking the user until they enter a valid number
    while True:

        # Ask the user for a value and remove any spaces
        user_input = input(prompt).strip()

        # Try to convert the user's input into an integer
        try:

            # Convert the input into an integer
            number = int(user_input)

            # Check if the number is within the allowed range
            if number >= minimum and number <= maximum:

                # Return the valid number to the calling function
                return number

            # Inform the user that the number is outside the allowed range
            else:
                print(
                    "Please enter a whole number between "
                    + str(minimum)
                    + " and "
                    + str(maximum)
                    + "."
                )

        # Handle anything that cannot be converted into an integer
        except ValueError:

            # Inform the user that the input was not a whole number
            print("Please enter a valid whole number.")


def academy_totals(students):

    # Count the number of students
    total_students = len(students)

    # Start counting enrolments and marks
    total_enrolments = 0
    total_marks = 0

    # Go through every student
    for student_id in students:

        # Go through every course the student is enrolled in
        for course_id in students[student_id]["enrolments"]:

            # Count one enrolment
            total_enrolments += 1

            # Count all marks recorded for this enrolment
            total_marks += len(
                students[student_id]["enrolments"][course_id]
            )

    # Return the totals as a tuple
    return (
        total_students,
        total_enrolments,
        total_marks
    )


def best_course(courses, students):
    
    # Store the best course found so far
    best_course_id = None
    best_average = None

    # Go through every course
    for course_id in courses:

        # Keep track of the total marks and number of marks
        total = 0
        count = 0

        # Check every student
        for student_id in students:

            # Check if the student is enrolled in this course
            if course_id in students[student_id]["enrolments"]:

                # Go through every mark for this course
                for mark in students[student_id]["enrolments"][course_id]:

                    # Add the mark to the total
                    total += mark

                    # Count the mark
                    count += 1

        # Only calculate an average if marks exist
        if count > 0:

            average = total / count

            # Check if this is the highest average so far
            if best_average is None or average > best_average:

                best_average = average
                best_course_id = course_id

    # Return the result as a tuple
    return (best_course_id, best_average)


# Team choice tuple helper
def highest_and_lowest(students, student_id):
    pass


# ==========================
# Course Functions
# ==========================

# Adds a new course to the courses dictionary.
def add_course(courses):

    # Ask the user to enter the course name
    course_name = input("Course name: ").strip()

    # Check if the course name is blank
    if course_name == "":
        print("Course name cannot be blank.")
        return

    # Ask the user to enter the course capacity
    capacity = read_valid_number("Capacity (1-100): ", 1, 100)

    # Ask the user to enter the course pass mark
    pass_mark = read_valid_number("Pass mark (0-100): ", 0, 100)

    # Generate the next course ID
    course_id = "C" + str(len(courses) + 1)

    # Create the new course in the courses dictionary
    courses[course_id] = {
        "name": course_name,
        "capacity": capacity,
        "pass_mark": pass_mark,
        "roster": []
    }

    # Confirm that the course was added successfully
    print(
        "Added "
        + course_id
        + ": "
        + course_name
        + " (capacity "
        + str(capacity)
        + ", pass mark "
        + str(pass_mark)
        + ")"
    )


# Enrols a student into a course
def enrol_student(courses, students):

    # Ask the user for the student ID
    student_id = input("Student ID: ").strip()

    # Ask the user for the course ID
    course_id = input("Course ID: ").strip()

 # Check if the student exists
    if student_id not in students:
        print("Student not found.")
        return

    # Check if the course exists
    if course_id not in courses:
        print("Course not found.")
        return

    # Check if the course has reached its maximum capacity
    if len(courses[course_id]["roster"]) >= courses[course_id]["capacity"]:
        print(
            course_id + ": " +
            courses[course_id]["name"] +
            " is full (" +
            str(len(courses[course_id]["roster"])) +
            "/" +
            str(courses[course_id]["capacity"]) +
            " enrolled)."
        )
        return

    # Check if the student is already enrolled in the course
    if course_id in students[student_id]["enrolments"]:
        print(
            student_id + " " +
            students[student_id]["name"] +
            " is already enrolled in " +
            course_id + ": " +
            courses[course_id]["name"] + "."
        )
        return

    # Add the student to the course roster
    courses[course_id]["roster"].append(student_id)

    # Add an empty marks list to the student's enrolments
    students[student_id]["enrolments"][course_id] = []

    # Display a success message
    print(
        student_id + " " +
        students[student_id]["name"] +
        " enrolled in " +
        course_id + ": " +
        courses[course_id]["name"]
    )



# Withdraws a student from a course
def withdraw_student(courses, students):

    # Ask the user for the student ID
    student_id = input("Student ID: ").strip()

    # Ask the user for the course ID
    course_id = input("Course ID: ").strip()

    # Check if the student exists
    if student_id not in students:
        print("Student not found.")
        return

    # Check if the course exists
    if course_id not in courses:
        print("Course not found.")
        return

    # Check if the student is enrolled in the course
    if course_id not in students[student_id]["enrolments"]:
        print(
            student_id + " " +
            students[student_id]["name"] +
            " is not enrolled in " +
            course_id + ": " +
            courses[course_id]["name"] + "."
        )
        return

    # Ask the user to confirm the withdrawal
    confirm = input(
        "Withdraw " +
        student_id + " " +
        students[student_id]["name"] +
        " from " +
        course_id + ": " +
        courses[course_id]["name"] +
        "? (y/n): "
    ).strip().lower()

    # Check if the user confirmed the withdrawal
    if confirm != "y":
        print("Withdrawal cancelled.")
        return

    # Remove the student from the course roster
    courses[course_id]["roster"].remove(student_id)

    # Remove the course from the student's enrolments
    del students[student_id]["enrolments"][course_id]

    # Display a success message
    print(
        student_id + " " +
        students[student_id]["name"] +
        " withdrawn from " +
        course_id + ": " +
        courses[course_id]["name"]
    )


# ==========================
# Student Functions
# ==========================

def register_student(students):
    print("\n--- Register Student ---")

    student_id = input("Enter student ID: ").strip().upper()

    while student_id == "":
        print("Student ID cannot be blank.")
        student_id = input("Enter student ID: ").strip().upper()

    if student_id in students:
        print("Student ID already exists.")
        return

    student_name = input("Enter student name: ").strip()

    while student_name == "":
        print("Student name cannot be blank.")
        student_name = input("Enter student name: ").strip()

    students[student_id] = {
        "name": student_name,
        "enrolments": {}
    }

    print(
        student_id + " " +
        students[student_id]["name"] +
        " registered successfully."
    )

def record_mark(courses, students):
    print("\n--- Record Mark ---")

    student_id = input("Enter student ID: ").strip().upper()

    while student_id == "":
        print("Student ID cannot be blank.")
        student_id = input("Enter student ID: ").strip().upper()

    course_id = input("Enter course ID: ").strip().upper()

    while course_id == "":
        print("Course ID cannot be blank.")
        course_id = input("Enter course ID: ").strip().upper()

    if student_id not in students:
        print("Student does not exist.")
        return

    if course_id not in courses:
        print("Course does not exist.")
        return

    if course_id not in students[student_id]["enrolments"]:
        print("Student is not enrolled in this course.")
        return

    while True:
        mark_text = input("Enter mark from 0 to 100: ").strip()

        try:
            mark = float(mark_text)
        except ValueError:
            print("Invalid mark. Enter a number.")
            continue

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
        else:
            break

    students[student_id]["enrolments"][course_id].append(mark)
    print(
        str(mark) + " recorded for " +
        student_id + " " +
        students[student_id]["name"] +
        " in " +
        course_id + ": " +
        courses[course_id]["name"]
    )


def course_average_for(students, student_id, course_id):
    marks = students[student_id]["enrolments"][course_id]

    if len(marks) == 0:
        return (0, 0)

    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    return (average, len(marks))


def student_transcript(courses, students):
    print("\n--- Student Transcript ---")

    student_id = input("Enter student ID: ").strip().upper()

    while student_id == "":
        print("Student ID cannot be blank.")
        student_id = input("Enter student ID: ").strip().upper()

    if student_id not in students:
        print("Student does not exist.")
        return

    print("\nStudent ID:", student_id)
    print("Student name:", students[student_id]["name"])

    if len(students[student_id]["enrolments"]) == 0:
        print("This student has no enrolments.")
        return

    overall_total = 0
    overall_mark_count = 0

    for course_id in students[student_id]["enrolments"]:
        marks = students[student_id]["enrolments"][course_id]

        print("\nCourse ID:", course_id)
        print("Course name:", courses[course_id]["name"])

        if len(marks) == 0:
            print("No marks recorded.")
        else:
            average, mark_count = course_average_for(
                students, student_id, course_id
            )

            print("Marks:", marks)
            print("Course average:", round(average, 2))

            for mark in marks:
                overall_total = overall_total + mark
                overall_mark_count = overall_mark_count + 1

    if overall_mark_count == 0:
        print("\nOverall average: No marks recorded.")
    else:
        overall_average = overall_total / overall_mark_count
        print("\nOverall average:", round(overall_average, 2))


# ==========================
# Report Functions
# ==========================

def course_report(courses, students):
    pass


def search_everything(courses, students):
    
    print("\n--- Search ---")
    keyword = input("Enter a search keyword: ").strip().lower()

    matched_students = []
    for student_id, student_info in students.items():
        name_lower = student_info["name"].lower()
        if name_lower.count(keyword) > 0:
            matched_students.append((student_id, student_info["name"]))

    matched_courses = []
    for course_id, course_info in courses.items():
        name_lower = course_info["name"].lower()
        if name_lower.count(keyword) > 0:
            matched_courses.append((course_id, course_info["name"]))

    if len(matched_students) == 0 and len(matched_courses) == 0:
        print("No matches.")
        return

    if len(matched_students) > 0:
        print("Students:")
        for student_id, name in matched_students:
            print(" ", student_id, ":", name)

    if len(matched_courses) > 0:
        print("Courses:")
        for course_id, name in matched_courses:
            print(" ", course_id, ":", name)


def academy_report(courses, students):
    pass


# ==========================
# Main Program
# ==========================

def main():

    # Main data structures
    courses = {}
    students = {}

    while True:

        print()
        print("===== Melsoft Campus Manager =====")
        print("1. Add a course")
        print("2. Register a student")
        print("3. Enrol a student")
        print("4. Record a mark")
        print("5. Student transcript")
        print("6. Course report")
        print("7. Search")
        print("8. Withdraw a student")
        print("9. Academy report")
        print("10. Exit")

        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            add_course(courses)

        elif choice == "2":
            register_student(students)

        elif choice == "3":
            enrol_student(courses, students)

        elif choice == "4":
            record_mark(courses, students)

        elif choice == "5":
            student_transcript(courses, students)

        elif choice == "6":
            course_report(courses, students)

        elif choice == "7":
            search_everything(courses, students)

        elif choice == "8":
            withdraw_student(courses, students)

        elif choice == "9":
            academy_report(courses, students)

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-10.")


main()
