# 🚀 AI/ML Learning Journey - Step 2 - Python Basics for ML

# ✅ Variables
x = 5
y = "Hello AI/ML"
print(x, y)

# ✅ Lists
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# ✅ Dictionaries
student = {
    "name": "AI Student",
    "level": "Beginner"
}
print("Student:", student)

# ✅ Loops
for num in numbers:
    print(f"Number: {num}")

# ✅ Conditions
if x > 3:
    print("x is greater than 3")

# ✅ Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("AI/ML Learner"))

# ✅ File Handling
with open("sample.txt", "w") as file:
    file.write("This is my first AI/ML file!\n")
    file.write("Python file handling is important for data loading.\n")

# Read the file back
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)

# ✅ Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create random data
data = np.random.randn(100)

# ✅ Basic Plotting
plt.hist(data, bins=10)
plt.title("Random Data Distribution")
plt.show()

print("✅ Step 2 - Python Basics Completed!")
