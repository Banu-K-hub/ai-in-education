import random


TASKS = {
    "CorelDRAW": [
        "Create a simple vector logo using basic shapes.",
        "Create a poster using text, shapes and alignment tools.",
        "Design a business card using CorelDRAW."
    ],

    "Logo Design": [
        "Create a minimal logo for an educational organization.",
        "Design a logo for a fictional technology company.",
        "Create a logo using only geometric shapes."
    ],

    "Vector Graphics": [
        "Create a vector illustration using circles and rectangles.",
        "Draw a simple icon using vector shapes.",
        "Create three scalable icons for an educational application."
    ],

    "Typography": [
        "Create a poster using two different font families.",
        "Design a motivational quote using typography.",
        "Create a typographic composition for a school event."
    ],

    "Color Theory": [
        "Create a design using complementary colors.",
        "Create a three-color palette for an educational website.",
        "Design a poster using warm and cool colors."
    ]
}


def generate_lesson(topic, level):
    """Generate a graphic design learning task."""

    task = random.choice(TASKS.get(topic, ["Create a simple design project."]))

    if level.lower() == "beginner":
        instruction = (
            "Focus on basic tools, simple shapes and clear composition."
        )
    else:
        instruction = (
            "Use advanced composition, visual hierarchy and creative details."
        )

    return f"""
Topic: {topic}
Level: {level}

Task:
{task}

Recommendation:
{instruction}

Reflection:
Explain which design tools you used and why you chose them.
"""
