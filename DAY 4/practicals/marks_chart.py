import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_marks.csv")

plt.bar(df["Name"], df["Maths"])
plt.title("Maths Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()