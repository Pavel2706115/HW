# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Create a dictionary to represent person's data:
    name      : Ivan
    age       : 30
    city      : Sofia
Print the data as shown:
"""
### YOUR CODE HERE
    # dict_person = {
    #     "name": "Ivan",
    #     "age": 30,
    #     "city": "Sofia"
    # }
    # print(f"name      : {dict_person['name']}")
    # print(f"age       : {dict_person['age']}")
    # print(f"city      : {dict_person['city']}")

### EXPECTED OUTPUT:
# name      : Ivan
# age       : 30
# city      : Sofia

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Given the person dictionary above, add a new key-value pair: "job":"Developer"
"""

### Your code here
    # dict_person["job"] = "Developer"
    # print(dict_person)
### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 30, 'city': 'Sofia', 'job': 'Developer'}


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, update the value of an existing key and print the updated dictionary.
"""

### Your code here
    # dict_person["age"] = 31
    # print(dict_person)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 31, 'city': 'Sofia'}


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, remove a key-value pair and print the updated dictionary.
"""

### Your code here
    # dict_person.pop("age")
    # print(dict_person)
### EXPECTED OUTPUT:
# {'name': 'Ivan', 'city': 'Sofia'}


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, check if a specific key exists and print the result.
"""

### Your code here
    # if "name" in dict_person:
    #     print(True)
### EXPECTED OUTPUT:
# True


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
    Given two dictionaries, merge them into one and print the result.
"""

### Your code here
    # dict_job = {
    #     "job": "Developer",
    #     "salary": 50000
    # }

    # dict_merged = {**dict_person, **dict_job}
    # print(dict_merged)
### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 30, 'city': 'Sofia', 'job': 'Developer', 'salary': 50000}


# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, print all key-value pairs in the format "key: value".
"""

### Your code here
    # dict_person_items = dict_person.items()
    # for key, value in dict_person_items:
    #     print(f"{key}: {value}")

### EXPECTED OUTPUT:
# name: Ivan
# age: 30
# city: Sofia