fruit = input("Fruit name: ").title().strip()

fruits = [
    {"fruit": "Apple", "calorie": "130"},
    {"fruit": "Avocado", "calorie": "50"},
    {"fruit": "Banana", "calorie": "110"},
    {"fruit": "Cantaloupe", "calorie": "50"},
    {"fruit": "Grapefruit", "calorie": "60"},
    {"fruit": "Grapes", "calorie": "90"},
    {"fruit": "Honeydew", "calorie": "50"},
    {"fruit": "Kiwifruit", "calorie": "90"},
    {"fruit": "Lemon", "calorie": "15"},
    {"fruit": "Lime", "calorie": "20"},
    {"fruit": "Nectarine", "calorie": "60"},
    {"fruit": "Orange", "calorie": "80"},
    {"fruit": "Peach", "calorie": "60"},
    {"fruit": "Pear", "calorie": "100"},
    {"fruit": "Pineapple", "calorie": "50"},
    {"fruit": "Plums", "calorie": "70"},
    {"fruit": "Strawberries", "calorie": "50"},
    {"fruit": "Sweet Cherries", "calorie": "100"},
    {"fruit": "Tangerin", "calorie": "50"},
    {"fruit": "Watermelon", "calorie": "80"}]

for x in fruits:
    if x["fruit"] == fruit:
        print("Calories:", x["calorie"])