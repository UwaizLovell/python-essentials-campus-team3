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
    pass


def best_course(courses, students):
    pass


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
    pass


def record_mark(courses, students):
    pass


def course_average_for(students, student_id, course_id):
    pass


def student_transcript(courses, students):
    pass


# ==========================
# Report Functions
# ==========================

def course_report(courses, students):
    pass


def search_everything(courses, students):
    pass


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