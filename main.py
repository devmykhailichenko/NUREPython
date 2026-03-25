# # file object -> cursor position, mode, buffer, functions
# # Hello
# # ^
# # Hello
# #   ^
#
# # file = open("test.txt", "r")
# #
# # content = file.read()
# #
# # print(content)
# #
# # file.close()
#
# file_cursor = open("test.txt", "r")
#
# content = file_cursor.read(5)
# position = file_cursor.tell()
# print(position, content)
#
# next_content = file_cursor.read(5)
# position = file_cursor.tell()
# print(position, next_content)
#
# file_cursor.close()
#
# file_cursor = open("test.txt", "r")
# line1 = file_cursor.readline()
# line2 = file_cursor.readline()
# line3 = file_cursor.readline()
# line4 = file_cursor.readline()
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# file_cursor.close()
#
# file_cursor = open("test.txt", "r")
#
# lines = file_cursor.readlines()
#
# print(lines)
# file_cursor.close()
#
# file_cursor = open("test.txt", "r")
#
# for line in file_cursor:
#     print(line)
#
# file_cursor.close()
#
# file_cursor = open("test.txt", "r")
#
# content = file_cursor.read(5)
# position = file_cursor.tell()
# print(position, content)
#
# file_cursor.seek(0)
#
# next_content = file_cursor.read(5)
# position = file_cursor.tell()
# print(position, next_content)
#
# file_cursor.close()
#
# # read readline, readlines, for + while, read
#
# lines = [
#     "First\n",
#     "Second\n",
#     "Third\n"
# ]
#
# file_write = open("test.txt", "w")
#
# file_write.writelines(lines)
#
# file_write.close()
#
#
# file_write = open("test.txt", "a")
#
# file_write.write("Fourth\n")
#
# file_write.close()
#
# file_wr = open("test.txt", "r+")
#
# content = file_wr.read(5)
# print(content)
#
# file_wr.write("WRITE")
#
# file_wr.close()
#
# # Context manager
# with open("test.txt", "r") as file_context:
#     data = file_context.read()
#     print("With context manager:", data)
#
#
#

#Task
FILENAME = "students.txt"

def load_students() -> list:
    students = []

    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if ":" not in line:
                continue

            name, grade = line.split(":")

            students.append({
                "name": name,
                "grade": int(grade)
            })

    return students

def save_students(students) -> None:
    with open(FILENAME, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']}:{student['grade']}\n"

            file.write(line)

def show_students(students) -> None:
    if len(students) == 0:
        print("Student list is empty!")
        return

    print("\nStudent list:")

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} – {student['grade']}")

def add_student(students) -> None:
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name should be non-empty")
        return

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!")
            return

    grade = int(input("Please enter students grade (0-100): ").strip())

    if grade < 0 or grade > 100:
        print("Grade should be between 0 and 100!")
        return

    students.append({
        "name": name,
        "grade": grade
    })

    save_students(students)

    print("Student added successfully!")

def update_students_grade(students) -> None:
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name should be non-empty")
        return

    grade = int(input("Please enter new grade (0-100): ").strip())

    if grade < 0 or grade > 100:
        print("Grade should be between 0 and 100!")
        return

    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            student["grade"] = grade
            found = True
            break

    if not found:
        print("Student not found!")
        return

    save_students(students)

    print("Student updated successfully!")

def delete_student(students) -> None:
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name should be non-empty")
        return

    new_students = []
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            found = True
            continue

        new_students.append(student)

    if not found:
        print("Student not found!")
        return

    students.clear()
    students.extend(new_students)

    save_students(students)

    print("Student deleted successfully!")


def show_menu() -> None:
    print("\n======= Student Journal =======")
    print("1. Show all students")
    print("2. Add new student")
    print("3. Update student's grade")
    print("4. Delete student")
    print("5. Exit")

def main() -> None:
    students = load_students()

    while True:
        show_menu()

        command = input("Enter command number ->").strip()

        if command == "1":
            show_students(students)
        elif command == "2":
            add_student(students)
        elif command =="3":
            update_students_grade(students)
        elif command =="4":
            delete_student(students)
        elif command =="5":
            print("The end...")
            break
        else:
            print("Invalid command!")

main()