from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5]]
marks = [40, 50, 60, 70, 80]

model = LinearRegression()
model.fit(hours, marks)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])