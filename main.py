import pandas as pd
import numpy as np

# Read the student dataset
df = pd.read_csv("students.csv")

# Display project title
print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# Display student data
print("\nSTUDENT DATA")
print("-" * 60)
print(df)

# Define subjects
subjects = ["Python", "DBMS", "Java"]


# Function to calculate total marks
def calculate_total(row):
    return sum(row[subject] for subject in subjects)


# Function to calculate average marks
def calculate_average(row):
    return np.round(np.mean([row[subject] for subject in subjects]), 2)


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to check pass or fail
def check_result(row):
    for subject in subjects:
        if row[subject] < 40:
            return "Fail"
    return "Pass"


# Calculate total, average, grade, and result
df["Total"] = df.apply(calculate_total, axis=1)
df["Average"] = df.apply(calculate_average, axis=1)
df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df.apply(check_result, axis=1)


# Display student performance summary
print("\n\nSTUDENT PERFORMANCE SUMMARY")
print("-" * 60)
print(df[["Student_ID", "Name", "Total",
          "Average", "Grade", "Result"]].to_string(index=False))


# Display class performance statistics
print("\n\nCLASS PERFORMANCE")
print("-" * 60)

print("Total students:", len(df))
print("Class average:", round(df["Average"].mean(), 2))
print("Highest average:", df["Average"].max())
print("Lowest average:", df["Average"].min())

passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("Students passed:", passed)
print("Students failed:", failed)


# Subject-wise performance analysis
print("\n\nSUBJECT-WISE PERFORMANCE")
print("-" * 60)

for subject in subjects:
    print(subject, "Average:", round(df[subject].mean(), 2))
    print(subject, "Highest marks:", df[subject].max())
    print(subject, "Lowest marks:", df[subject].min())


# Find the top-performing students
print("\n\nTOP PERFORMING STUDENTS")
print("-" * 60)

top_students = df.nlargest(3, "Average")

print(top_students[["Student_ID", "Name",
                    "Department", "Average", "Grade"]].to_string(index=False))


# Find the student with the highest average
best_student = df.loc[df["Average"].idxmax()]

print("\nBest performing student:", best_student["Name"])
print("Highest average marks:", best_student["Average"])


# Display attendance analysis
print("\n\nATTENDANCE ANALYSIS")
print("-" * 60)

print("Class average attendance:",
      round(df["Attendance"].mean(), 2), "%")

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with attendance below 75%:")

if len(low_attendance) > 0:
    print(low_attendance[["Student_ID", "Name",
                          "Attendance"]].to_string(index=False))
else:
    print("No students have attendance below 75%.")


# Final message
print("\n" + "=" * 60)
print("       ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)
