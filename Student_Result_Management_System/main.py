from Student_marks import Student
def main():
    s1 = Student("Ravi Kumar", 101, "CSE", marks={"Maths": 92, "Physics": 88, "Chemistry": 76})
    s2 = Student("Anita Sharma", 102, "ECE", marks={"Maths": 40, "Physics": 35, "Chemistry": 38, "Biology": 20})

    print(f"College: {Student.COLLEGE_NAME}")
    print(Student.get_total_students())
    print(s1)
    print(s2)
    print(f"s1 marks : {s1.get_marks()}")
    print(f"s1 passed : {s1.has_passed()}")
    print(f"s2 passed : {s2.has_passed()}")
    s1.change_branch("IT")
    print(f"is_valid_mark(105): {Student.is_valid_mark(105)}")
    try:
        s1.add_marks("English", 150)
    except ValueError as e:
        print(f"Blocked (mark 150): {e}")

    try:
        s1.average = 90
    except AttributeError:
        print("Blocked (write average): property 'average' of 'Student' object has no setter")

    try:
        s1.roll_number = 105
    except AttributeError:
        print("Blocked (write roll): property 'roll_number' of 'Student' object has no setter")

    print(f"protected : {s1._branch}")
    print(f"private : {s1._Student__marks}")

if __name__ == "__main__":
    main()