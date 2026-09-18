import streamlit as st

from calculations import get_grade, calculate_sgpa
from database import get_marks, delete_marks, create_tables, add_marks


# Create database table when the app starts
create_tables()


# Page title
st.title("Student Management System")
st.write("Student Marks and SGPA Calculator")


# Student ID
student_id = st.number_input(
    "Enter Student ID",
    min_value=1,
    step=1
)


# View student result
if st.button("View Student Result"):

    marks = get_marks(student_id)

    if not marks:
        st.warning("No marks found for this student.")

    else:
        st.subheader("Student Marks")

        subjects = []

        for mark in marks:
            mark_id = mark[0]
            subject = mark[1]
            marks_obtained = mark[2]
            credits = mark[3]

            subjects.append(
                (subject, marks_obtained, credits)
            )

            st.write(
                f"**{subject}** - "
                f"Marks: {marks_obtained} | "
                f"Credits: {credits} | "
                f"Grade: {get_grade(marks_obtained)}"
            )

        # Calculate SGPA
        sgpa = calculate_sgpa(subjects)

        st.subheader("Result")
        st.success(f"SGPA: {sgpa}")


# Add marks section
st.subheader("Add Student Marks")

student_id_add = st.number_input(
    "Enter Student ID",
    min_value=1,
    step=1,
    key="add_student_id"
)

subject = st.text_input("Enter Subject")

marks = st.number_input(
    "Enter Marks",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

credits = st.number_input(
    "Enter Credits",
    min_value=1.0,
    step=1.0
)

if st.button("Add Marks"):

    add_marks(
        student_id_add,
        subject,
        marks,
        credits
    )

    st.success("Marks added successfully!")

# Delete marks section
st.subheader("Delete Marks")

mark_id = st.number_input(
    "Enter Mark ID to delete",
    min_value=1,
    step=1
)


if st.button("Delete Mark"):

    delete_marks(mark_id)

    st.success("Marks deleted successfully.")