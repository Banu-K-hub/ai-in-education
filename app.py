from lesson_generator import generate_lesson

print("===================================")
print("  Graphic Design Learning Assistant")
print("===================================")

print("\nWelcome!")
print("This program creates practice tasks for graphic design students.")

topics = {
    "1": "CorelDRAW",
    "2": "Logo Design",
    "3": "Vector Graphics",
    "4": "Typography",
    "5": "Color Theory"
}

print("\nChoose a topic:")

for number, topic in topics.items():
    print(f"{number}. {topic}")

choice = input("\nEnter a number (1-5): ")

if choice not in topics:
    print("Invalid choice. Please restart the program.")
else:
    level = input("Student level (Beginner / Intermediate): ")

    topic = topics[choice]

    lesson = generate_lesson(topic, level)

    print("\n--- YOUR LEARNING TASK ---")
    print(lesson)

    print("\nGood luck with your design! 🎨")
