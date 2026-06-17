description = input("Enter image description: ")

captions = [
    f"{description} ✨ Living my best life.",
    f"{description} 📸 Capturing the moment.",
    f"{description} 🌟 Memories that last forever.",
    f"{description} ❤️ Good vibes only.",
    f"{description} 🚀 Chasing dreams."
]

print("\nGenerated Captions:\n")

for c in captions:
    print("-", c)