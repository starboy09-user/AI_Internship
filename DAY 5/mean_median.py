marks = [60, 70, 80, 90, 100]

mean = sum(marks) / len(marks)

sorted_marks = sorted(marks)
median = sorted_marks[len(sorted_marks) // 2]

print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)