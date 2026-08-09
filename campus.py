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
    print("Mark recorded successfully.")


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
    pass


# ==========================
# Report Functions
# ==========================

def course_report(courses, students):
    print("\n--- Course Report ---")
    course_id = input("Enter course ID: ").strip().upper()
    course_info = courses.get(course_id)
    if course_info == None:
        print(course_id, "does not exist.")
        return

    roster = course_info["roster"]
    capacity = course_info["capacity"]
    pass_mark = course_info["pass_mark"]

    print("COURSE REPORT -", course_id, ":", course_info["name"], "(pass mark", pass_mark, ")")

    total_marks_sum = 0
    total_marks_count = 0
    passing_students = 0
    students_with_marks = 0

    leaderboard_list = []
    no_marks_list = []

    for student_id in roster:
        average, count = course_average_for(students, student_id, course_id)
        if count > 0:
            total_marks_sum = total_marks_sum + (average * count)
            total_marks_count = total_marks_count + count
            students_with_marks = students_with_marks + 1
            if average >= pass_mark:
                passing_students = passing_students + 1
            leaderboard_list.append((average, student_id))
        else:
            no_marks_list.append(student_id)

    if total_marks_count > 0:
        course_average = round(total_marks_sum / total_marks_count, 1)
        pass_rate = round((passing_students / students_with_marks) * 100, 1)
        print("Enrolled:", len(roster), "of", capacity, "| Course average:", course_average, "| Pass rate:", pass_rate, "%")
    else:
        print("Enrolled:", len(roster), "of", capacity, "| Course average: n/a | Pass rate: n/a")

    print("Leaderboard:")
    leaderboard_sorted = sorted(leaderboard_list, reverse=True)
    rank = 1
    for average, student_id in leaderboard_sorted:
        student_name = students[student_id]["name"]
        print(" ", rank, ".", student_id, student_name, round(average, 1))
        rank = rank + 1

    for student_id in no_marks_list:
        student_name = students[student_id]["name"]
        print(" ", student_id, student_name, "- no marks yet")


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
    print("\n--- Academy Report ---")
    total_students, total_enrolments, total_marks = academy_totals(students)

    if total_students == 0:
        print("No students registered yet.")
        return

    print("Students:", total_students)
    print("Courses:", len(courses))
    print("Enrolments:", total_enrolments)
    print("Marks recorded:", total_marks)

    total_sum = 0
    total_count = 0
    for student_id, student_info in students.items():
        for course_id, marks_list in student_info["enrolments"].items():
            for mark in marks_list:
                total_sum = total_sum + mark
                total_count = total_count + 1

    if total_count > 0:
        print("Academy-wide average:", round(total_sum / total_count, 1))
    else:
        print("Academy-wide average: n/a")

    best_id, best_average = best_course(courses, students)
    if best_id == None:
        print("Best performing course: none yet.")
    else:
        print("Best performing course:", best_id, ":", courses[best_id]["name"], "with average", best_average)

    distinction_list = []
    at_risk_list = []

    for student_id, student_info in students.items():
        student_sum = 0
        student_count = 0
        for course_id in student_info["enrolments"]:
            average, count = course_average_for(students, student_id, course_id)
            student_sum = student_sum + (average * count)
            student_count = student_count + count

        if student_count > 0:
            student_average = student_sum / student_count
            if student_average >= 80:
                distinction_list.append((student_id, student_info["name"], round(student_average, 1)))
            if student_average < 50:
                at_risk_list.append((student_id, student_info["name"], round(student_average, 1)))

    print("Distinction list (average 80+):")
    if len(distinction_list) == 0:
        print("  None yet.")
    else:
        for student_id, name, average in distinction_list:
            print(" ", student_id, name, average)

    print("At risk list (average below 50):")
    if len(at_risk_list) == 0:
        print("  None yet.")
    else:
        for student_id, name, average in at_risk_list:
            print(" ", student_id, name, average)


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
