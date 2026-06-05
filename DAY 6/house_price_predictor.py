from sklearn.linear_model import LinearRegression

area = [[500], [1000], [1500], [2000], [2500]]
price = [10, 20, 30, 40, 50]

model = LinearRegression()

model.fit(area, price)

house_area = int(input("Enter house area: "))

prediction = model.predict([[house_area]])

print("Predicted Price:", prediction[0], "Lakh")