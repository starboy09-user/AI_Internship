customer = input("Customer Name: ")
product = input("Product Name: ")
qty = int(input("Quantity: "))
price = float(input("Price Per Item: "))

total = qty * price

print("\n========== INVOICE ==========")
print("Customer :", customer)
print("Product  :", product)
print("Quantity :", qty)
print("Price    :", price)
print("Total    :", total)
print("=============================")