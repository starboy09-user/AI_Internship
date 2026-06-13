import random

captions = {
    "esports": [
        "Victory isn't given, it's earned. 🎮🔥",
        "Legends are made under pressure. 🏆",
        "Play smart. Aim true. Win big. 🎯",
        "Every match is a chance to become better. ⚡",
        "The grind never stops. 🚀"
    ]
}

topic = input("Enter topic: ").lower()

if topic == "esports":
    print(random.choice(captions["esports"]))
else:
   print(f"Ready to dominate the world of {topic}? 🔥")