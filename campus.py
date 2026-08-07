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


def enrol_student(courses, students):
    pass


def withdraw_student(courses, students):
    pass


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