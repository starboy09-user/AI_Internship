import pandas as pd

df = pd.read_csv("student_marks.csv")

print("First 5 Records:")
print(df.head())

print("\nAverage Marks:")
print(df[["Maths", "Science", "English"]].mean())

print("\nHighest Maths Marks:")
print(df["Maths"].max())