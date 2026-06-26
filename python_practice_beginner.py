
# PYTHON BASICS — Interview Practice

# 1. Functions
# ----------------------------------------------------------
# Q: Write a function greet that takes a name and returns a welcome message
def greet(name):
    return f"Hello, {name}! Welcome to your Python journey."

# ----------------------------------------------------------
# 2. Conditionals
# ----------------------------------------------------------
# Q: Write a function check_age that returns "You can vote!" if age >= 18
def check_age(age):
    if age >= 18:
        return "You can vote!"
    else:
        return "Too young to vote."

# ----------------------------------------------------------
# 3. Loops
# ----------------------------------------------------------
# Q: Write a function count_up that prints every number from 1 to n
def count_up(n):
    for i in range(1, n + 1):
        print(i)

# ----------------------------------------------------------
# 4. Lists + List Comprehension
# ----------------------------------------------------------
# Q: Write a function get_evens that returns only even numbers from a list
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

# ----------------------------------------------------------
# 5. Dictionaries
# ----------------------------------------------------------
# Q: Write a function word_count that counts occurrences of each word
def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

# ----------------------------------------------------------
# 6. Strings
# ----------------------------------------------------------
# Q: Write a function reverse_string that returns a string reversed
def reverse_string(string):
    return string[::-1]

# ----------------------------------------------------------
# 7. Sets + Tuples
# ----------------------------------------------------------
# Q: Write a function remove_duplicates that removes duplicates from a list
def remove_duplicates(numbers):
    return list(set(numbers))

# ----------------------------------------------------------
# 8. Classes + OOP
# ----------------------------------------------------------
# Q: Write a Dog class with name, breed and a bark method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Woof! My name is {self.name}"

# ----------------------------------------------------------
# 9. Error Handling
# ----------------------------------------------------------
# Q: Write a safe_divide function that handles division by zero
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# ----------------------------------------------------------
# 10. Lambda
# ----------------------------------------------------------
# Q: Write a lambda that doubles a number
double = lambda x: x * 2

# ----------------------------------------------------------
# 11. Find Maximum
# ----------------------------------------------------------
# Q: Find the largest number in a list without using max()
def find_max(numbers):
    current_max = numbers[0]
    for n in numbers:
        if n > current_max:
            current_max = n
    return current_max

# ----------------------------------------------------------
# 12. Enumerate
# ----------------------------------------------------------
# Q: Write a function find_index that returns the index of a value in a list
def find_index(numbers, target):
    for i, n in enumerate(numbers):
        if n == target:
            return i

# ============================================================
# TEST YOUR ANSWERS
# ============================================================
print(greet("Pari"))
print(check_age(20))
print(check_age(15))
count_up(5)
print(get_evens([1, 2, 3, 4, 5, 6]))
print(word_count("hi bye hi hi bye"))
print(reverse_string("hello"))
print(remove_duplicates([1, 2, 2, 3, 3, 3]))
dog1 = Dog("Rex", "Labrador")
print(dog1.bark())
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(double(5))
print(find_max([3, 1, 7, 2, 9, 4]))
print(find_index([10, 20, 30, 40], 30))





    
