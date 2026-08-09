# =====================================
# Melsoft Campus Manager
# Python Essentials 1 - Capstone Project
# =====================================


# ==========================
# Helper Functions
# ==========================

def read_valid_number(prompt, minimum, maximum):
    pass


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

def add_course(courses):
    pass


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
