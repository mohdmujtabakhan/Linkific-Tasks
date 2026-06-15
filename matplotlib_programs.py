import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.bar(students, marks)

plt.title("Bar Plot")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 9, 10]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++"]
students = [40, 35, 25]

plt.pie(students, labels=subjects, autopct='%1.1f%%')

plt.title("Pie Chart")

plt.show()

import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,5]

plt.hist(data)

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()