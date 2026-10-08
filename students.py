from email.policy import default

FILENAME = "students.txt"

def load_students() -> list:
    students = []

    with open(FILENAME, "r") as students_f:
        for line in students_f:
            line = line.strip()

            if not line:
                continue

            name, grade = line.split(':')

            students.append({
                "student_name": name,
                "grade": int(grade)
            })

    return students


def save_students(students: list) -> None:
    with open(FILENAME, "w" ) as students_f:
        for student in students:
            students_f.write(f"{student['student_name']}:{student['grade']}\n")


def add_student(students) -> None:
    name = input("Enter student name: ").strip()
    grade = int(input("Enter grade: "))

    if not name:
        return

    students.append({
        "student_name": name,
        "grade": grade
    })

    save_students(students)


def update_student(students) -> None:
    name = input("Enter student name: ").strip()

    for student in students:
        if student["student_name"].lower() == name.lower():
            new_grade = int(input("Enter new grade: "))

            student["grade"] = new_grade

            save_students(students)
            print("Student updated!")
            return

    print("Student not found!")

def delete_student(students) -> None:
    name = input("Enter student name: ").strip()

    for student in students:
        if student["student_name"].lower() == name.lower():
            students.remove(student)

            save_students(students)

            print("Student deleted!")
            return

    print("Student not found!")

def show_menu() -> None:
    print("******* Students DB *******")
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Exit")

def main() -> None:
    students = load_students()

    while True:
        show_menu()

        command = input("Enter your command: ")

        match command:
            case "1": add_student(students)
            case "2": update_student(students)
            case "3": delete_student(students)
            case "4": break


main()