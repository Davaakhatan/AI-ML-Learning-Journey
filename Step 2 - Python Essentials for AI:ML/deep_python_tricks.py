# 🚀 AI/ML Learning Journey - Advanced Python Tricks

# 1️⃣ List Comprehensions
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print("Upper Names:", upper_names)

# 2️⃣ Lambda, Map, Filter, Reduce
from functools import reduce

salaries = [45000, 55000, 60000, 40000]
high_salaries = list(filter(lambda x: x > 50000, salaries))
print("High Salaries:", high_salaries)

ages = [25, 30, 22, 35, 28]
total_age = reduce(lambda x, y: x + y, ages)
print("Total Age:", total_age)

# 3️⃣ Decorators
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution Time: {time.time() - start:.2f} seconds")
        return result
    return wrapper

@timer
def sample_task():
    time.sleep(1)
    print("Task Complete")

sample_task()

# 4️⃣ Context Manager
with open("sample_context.txt", "w") as file:
    file.write("AI/ML Rocks!")
