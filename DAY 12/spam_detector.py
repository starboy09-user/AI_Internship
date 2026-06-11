import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("sample_data.csv")

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["message"])

# Labels
y = data["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Test message
test_message = ["You have won a cash prize"]

# Convert test text
test_vector = vectorizer.transform(test_message)

# Prediction
prediction = model.predict(test_vector)

print("Message:", test_message[0])
print("Prediction:", prediction[0])

# Save result
with open("OUTPUT/result.txt", "w") as file:
    file.write(f"Message: {test_message[0]}\n")
    file.write(f"Prediction: {prediction[0]}")