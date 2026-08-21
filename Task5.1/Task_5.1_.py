def read_old_data():
    students = []

    try:
        with open("studentInfo.txt", "r") as info_file, \
             open("studentMarks.txt", "r") as marks_file:

            info_data = info_file.readlines()
            marks_data = marks_file.readlines()

            for info, marks in zip(info_data, marks_data):

                # Read rollno and name
                rollno, name = info.strip().split("-")

                # Read rollno and 3 marks
                mark_data = marks.strip().split("-")

                mark1 = float(mark_data[1])
                mark2 = float(mark_data[2])
                mark3 = float(mark_data[3])

                # Calculate average
                average = (mark1 + mark2 + mark3) / 3

                students.append([
                    rollno,
                    name,
                    mark1,
                    mark2,
                    mark3,
                    average
                ])

    except FileNotFoundError:
        # Files do not exist during the first run
        pass

    return students


def write_data(n):

    # Read previous students
    students = read_old_data()

    # Enter new students
    for i in range(n):

        print("\nEnter details of student", i + 1)

        rollno = input("Enter Roll No: ")
        name = input("Enter Name: ")

        mark1 = float(input("Enter Subject 1 Marks: "))
        mark2 = float(input("Enter Subject 2 Marks: "))
        mark3 = float(input("Enter Subject 3 Marks: "))

        # Calculate average
        average = (mark1 + mark2 + mark3) / 3

        students.append([
            rollno,
            name,
            mark1,
            mark2,
            mark3,
            average
        ])

    # Sort ALL students by average
    # Highest average comes first
    students.sort(key=lambda x: x[5], reverse=True)

    # --------------------------------
    # Write studentInfo.txt
    # --------------------------------

    with open("studentInfo.txt", "w") as file:

        for student in students:

            rollno = student[0]
            name = student[1]

            file.write(
                rollno + "-" + name + "\n"
            )

    # --------------------------------
    # Write studentMarks.txt
    # --------------------------------

    with open("studentMarks.txt", "w") as file:

        for student in students:

            rollno = student[0]
            mark1 = student[2]
            mark2 = student[3]
            mark3 = student[4]

            file.write(
                rollno + "-" +
                str(mark1) + "-" +
                str(mark2) + "-" +
                str(mark3) + "\n"
            )

    # --------------------------------
    # Write Grade Files
    # --------------------------------

    with open("Agrade.txt", "w") as afile, \
         open("Bgrade.txt", "w") as bfile, \
         open("Cgrade.txt", "w") as cfile:

        for student in students:

            rollno = student[0]
            name = student[1]
            average = student[5]

            data = (
                rollno + "-" +
                name + "-" +
                f"{average:.2f}" +
                "\n"
            )

            # A Grade
            if 80 <= average <= 100:
                afile.write(data)

            # B Grade
            elif 60 <= average < 80:
                bfile.write(data)

            # C Grade
            elif 40 <= average < 60:
                cfile.write(data)


# --------------------------------
# Main Program
# --------------------------------

n = int(input("Enter number of students: "))

write_data(n)

print("\nData stored successfully.")