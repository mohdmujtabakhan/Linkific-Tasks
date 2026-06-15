# ==========================================
# PYTHON BASICS EXERCISES
# ==========================================


# ==========================================
# 1. Variable Example
# ==========================================

name = "Mujtaba"
age = 21

print("Name:", name)
print("Age:", age)


# ==========================================
# 2. User Input Program
# ==========================================

user_name = input("Enter your name: ")

print("Welcome", user_name)


# ==========================================
# 3. Data Types Program
# ==========================================

integer_num = 10
float_num = 5.5
text = "Python"
is_true = True

print(type(integer_num))
print(type(float_num))
print(type(text))
print(type(is_true))


# ==========================================
# 4. Even or Odd Program
# ==========================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==========================================
# 5. Positive or Negative Number
# ==========================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ==========================================
# 6. For Loop Example
# ==========================================

for i in range(1, 6):
    print(i)


# ==========================================
# 7. Multiplication Table Program
# ==========================================

table_num = int(input("Enter a number: "))

for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)


# ==========================================
# 8. While Loop Example
# ==========================================

count = 1

while count <= 5:
    print(count)
    count += 1


# ==========================================
# 9. Sum of Numbers Program
# ==========================================

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)


# ==========================================
# 10. Simple Function Program
# ==========================================

def greet():
    print("Hello Python")

greet()


# ==========================================
# 11. Addition Function Program
# ==========================================

def add(a, b):
    return a + b

result = add(5, 3)

print("Sum:", result)


# ==========================================
# 12. List Operations Program
# ==========================================

fruits = ["apple", "banana"]

fruits.append("orange")
fruits.remove("banana")

print(fruits)


# ==========================================
# 13. List Loop Program
# ==========================================

colors = ["red", "blue", "green"]

for color in colors:
    print(color)


# ==========================================
# 14. Dictionary Example
# ==========================================

student = {
    "name": "Ali",
    "age": 20
}

print(student["name"])
print(student["age"])


# ==========================================
# 15. Dictionary Loop Program
# ==========================================

student_info = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

for key, value in student_info.items():
    print(key, ":", value)
