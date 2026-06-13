topic = input("Enter topic: ")

hashtags = [
    f"#{topic}",
    f"#{topic}Tips",
    f"#{topic}Life",
    f"#{topic}Daily",
    f"#{topic}Goals"
]

print("\nGenerated Hashtags:")
for tag in hashtags:
    print(tag)