#DICTIONARIES
# creating a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}

#  using integers as keys and string as values
student_scores = {
    1: "Alice",
    2: "Bob",
    3: "him"
}

# using tuples as a key
location_map = {
    (6, 10): "school",
    (8, 12): "library"
}

# using different types as values
user_profile = {
    "name": "Ada",
    "age": 25,
    "is_admin": True,
    "skills": ["python", "javascript"],
    "location": (6, 43, 3, 43),
}

#  retrieving a value from a dictionary - you identify the element by their key in squared brackets
# N.B: the key must be typed correctly unless you'll a key error
print(programming_dictionary["Function"])
# Also, be careful about the data type if you just put function without the quotation marks, python will
# think you declared a function variable somewhere.

#  adding more items to a dictionary
programming_dictionary["loop"]: "the acton of dong something over and over again."

# creating an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_language)

# Edit an item in a dictionary - if item not found, a new entry will be created.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
#  loop through a dictionary
for key in programming_dictionary:
    print(key) #will print just the key)
    print(programming_dictionary[key]) # will print the value of each key.

# print all the keys in the dictionary
# using list() around student_info.keys() and student_info.values() is not strictly necessary, but it ensures the output is in list format/, which may be more readable and consistent
print("keys:", programming_dictionary.keys())

# print all the values in the dictionary
print("values:", list(programming_dictionary.values()))

#  check if "bug" exists in the dictionary
is_bug_present = "Bug" in programming_dictionary
print("is 'Bug' in the dictionary?", is_bug_present)






