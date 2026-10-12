
def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} Marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Please enter numbers only!")


def show_result(name, subjects, first=60, second=45, third=30):
    print("\n" + "=" * 30)
    print("         STUDENT RESULT")
    print("=" * 30)

    print("Name:", name)

    for subject, marks in subjects:
        print(f"{subject}: {marks}")

    total_marks = sum(marks for subject, marks in subjects)
    maximum_marks = len(subjects) * 100
    percentage = total_marks / maximum_marks * 100

    print("Total Marks:", total_marks, "/", maximum_marks)
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= first:
        division = "First Division"
    elif percentage >= second:
        division = "Second Division"
    elif percentage >= third:
        division = "Third Division"
    else:
        division = "Fail"

    print("Division:", division)
    print("=" * 30)

print("Boards:")
print("> BSEB")
print("> CBSE")

choice1 = input("Enter Board Name: ").strip().lower()

print("\nClasses:")
print("> 10th")
print("> 12th")

choice2 = input("Enter Your Class: ").strip().lower()

valid_boards = ("bseb", "cbse")
valid_classes = ("10", "10th", "12", "12th")

if choice1 not in valid_boards or choice2 not in valid_classes:
    print("Invalid Board or Class!")

elif choice1 == "cbse" and choice2 in ("12", "12th"):
    print("CBSE 12th is not supported yet.")

else:
    name = input("Enter Student Name: ").strip()

    if not name:
        name = "Unknown"

    if choice1 == "bseb" and choice2 in ("10", "10th"):
        subjects = [
            ("Mathematics", get_marks("Mathematics")),
            ("Hindi", get_marks("Hindi")),
            ("Sanskrit", get_marks("Sanskrit")),
            ("Science", get_marks("Science")),
            ("Social Science", get_marks("Social Science"))
        ]

        show_result(name, subjects)

    elif choice1 == "cbse" and choice2 in ("10", "10th"):
        subjects = [
            ("Mathematics", get_marks("Mathematics")),
            ("Hindi", get_marks("Hindi")),
            ("Sanskrit", get_marks("Sanskrit")),
            ("Science", get_marks("Science")),
            ("Social Science", get_marks("Social Science")),
            ("English", get_marks("English"))
        ]

        show_result(name, subjects, 60, 50, 33)

    elif choice1 == "bseb" and choice2 in ("12", "12th"):
        print("\nStreams:")
        print("> Science")
        print("> Arts")
        print("> Commerce")

        stream = input("Enter Stream: ").strip().lower()

        if stream == "science":
            print("\nSubject combinations:")
            print("> PCM")
            print("> PCB")
            print("> PCMB")

            combination = input(
                "Enter Subject Combination: "
            ).strip().lower()

            if combination == "pcm":
                subjects = [
                    ("Mathematics", get_marks("Mathematics")),
                    ("Physics", get_marks("Physics")),
                    ("Chemistry", get_marks("Chemistry")),
                    ("English", get_marks("English")),
                    ("Hindi", get_marks("Hindi"))
                ]

            elif combination == "pcb":
                subjects = [
                    ("Biology", get_marks("Biology")),
                    ("Physics", get_marks("Physics")),
                    ("Chemistry", get_marks("Chemistry")),
                    ("English", get_marks("English")),
                    ("Hindi", get_marks("Hindi"))
                ]

            elif combination == "pcmb":
                main = input(
                    "Enter Main Subject (Math/Biology): "
                ).strip().lower()

                if main in ("math", "mathematics"):
                    main_subject = "Mathematics"
                elif main == "biology":
                    main_subject = "Biology"
                else:
                    main_subject = None

                if main_subject is None:
                    print("Invalid Main Subject!")
                    subjects = None
                else:
                    subjects = [
                        (main_subject, get_marks(main_subject)),
                        ("Physics", get_marks("Physics")),
                        ("Chemistry", get_marks("Chemistry")),
                        ("English", get_marks("English")),
                        ("Hindi", get_marks("Hindi"))
                    ]

            else:
                print("Invalid Subject Combination!")
                subjects = None

            if subjects is not None:
                show_result(name, subjects)

        elif stream == "arts":
            subjects = [
                ("English", get_marks("English")),
                ("Elective", get_marks("Elective")),
                ("Elective 1", get_marks("Elective 1")),
                ("Elective 2", get_marks("Elective 2")),
                ("Elective 3", get_marks("Elective 3"))
            ]

            show_result(name, subjects)

        # COMMERCE
        elif stream == "commerce":
            subjects = [
                ("English", get_marks("English")),
                ("Elective", get_marks("Elective")),
                ("Accounts", get_marks("Accounts")),
                ("Business", get_marks("Business")),
                ("Economics", get_marks("Economics"))
            ]

            show_result(name, subjects)

        else:
            print("Invalid Stream!")
