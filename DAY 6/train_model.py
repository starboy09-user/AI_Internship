from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

model = LinearRegression()

model.fit(X, y)

print("Model Trained Successfully")