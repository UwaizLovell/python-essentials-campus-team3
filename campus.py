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

    print("Student registered successfully.")

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
