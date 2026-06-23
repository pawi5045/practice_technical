#1. Write a function greet that takes a name and returns "Hello, [name]!"

def greet(name):
    return f"Hello, {name}!"

#2. Write a function check_age that returns "You can vote!" if age >= 18, else "Too young to vote."

def check_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"

#3. Write a function word_count that takes a sentence and returns a dictionary of word occurrences
def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

#4. Write a function reverse_string that returns a string reversed

def reverse_string(string):
    return string[::-1]




    
