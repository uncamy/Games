lloyd = {
    "name": "Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}
alice = {
    "name": "Alice",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}
tyler = {
    "name": "Tyler",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

# Add your function below!
students = [lloyd, alice, tyler]
def average(x):
    return sum(x)/ len(x)
def get_average(student):
    return average(student["homework"])*.10 + average(student["quizzes"])*.3 + average(student["tests"])*.6
    
def get_letter_grade(score):
    score = round(score)
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70: 
        return "D"
    else:
        return "F"

def get_class_average(students):
    mean =0
    for x in students:
        mean += get_average(x)
    return mean/ len(students)
    
print get_class_average(students)
print get_letter_grade(get_class_average(students))

