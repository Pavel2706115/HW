# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""


### YOUR CODE HERE
    # def calculate_area(length, width):
    #     return length * width
    # print(calculate_area(10, 5))  # Example usage`

### TEST:
# print(calculate_area(10, 5))

### EXPECTED OUTPUT:
# 50


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""


### YOUR CODE HERE
    # def is_even(number):
    #     return number % 2 == 0
    # print(is_even(4))  # Example usage
    # print(is_even(5))  # Example usage

### TEST:
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT
# True
# False


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Write a function named 'multiply_elements' that takes a list of integers and returns the product of all the elements in the list.
"""


### YOUR CODE HERE
    # def multiply_elements(numbers):
    #     product = 1
    #     for number in numbers:
    #         product *= number
    #     return product
    # print(multiply_elements([2, 3, 4]))  # Example usage

### TEST:
# print(multiply_elements([2, 3, 4]))

### EXPECTED OUTPUT:
# 24


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### YOUR CODE HERE
    # def count_vowels(s):
    #     vowels = 'aeiouAEIOU'
    #     count = sum(1 for char in s if char in vowels)
    #     return count
    # print(count_vowels("hello"))  # Example usage
    # print(count_vowels("world"))  # Example usage

### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'reverse_string' that takes a string and returns the string reversed.
"""

### YOUR CODE HERE
    # reverse_string = lambda s: s[::-1]
    # print(reverse_string("hello"))  # Example usage

### TEST:
# print(reverse_string("hello"))

### EXPECTED OUTPUT:
# "olleh"


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Write a function 'find_max' that takes a list of numbers and returns the largest number in the list.
"""


### YOUR CODE HERE
    # def find_max(numbers):
    #     return max(numbers)
    # print(find_max([1, 3, 2, 8, 5]))  # Example usage

### TEST:
# print(find_max([1, 3, 2, 8, 5]))

### EXPECTED OUTPUT:
# 8


# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""


### YOUR CODE HERE
    # def remove_duplicates(lst):
    #     return list(set(lst))
    # print(remove_duplicates([1, 2, 2, 3, 4, 3]))  # Example usage

### TEST:
# print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]


# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""

### YOUR CODE HERE
    # is_palindrome = lambda s: s == s[::-1]
    # print(is_palindrome("madam"))  # Example usage
    # print(is_palindrome("hello"))  # Example usage
    # print(is_palindrome("racecar"))  # Example usage

### TEST:
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False


# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### YOUR CODE HERE
    # add = lambda x, y: x + y
    # print(add(2, 3))  # Example usage

### TEST:
# print(add(2, 3))

### EXPECTED OUTPUT:
# 5


# ---------------------------------- Task 10 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""


### YOUR CODE HERE
    # def filter_words(words, min_length):
    #     return [word for word in words if len(word) > min_length]
    # print(filter_words(["apple", "pear", "banana", "cherry"], 5))  # Example usage

### TEST:
# print(filter_words(["apple", "pear", "banana", "cherry"], 5))

### EXPECTED OUTPUT:
# ['banana', 'cherry']


# ---------------------------------- Task 11 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### YOUR CODE HERE
    # sort_by_last_letter = lambda word: word[-1]
    # sorted_list = sorted(["cherry", "banana", "apple"], key=sort_by_last_letter)
    # print(sorted_list)  # Example usage

### TEST:
# print(sorted(["cherry", "banana", "apple"], key=sort_by_last_letter))

### EXPECTED OUTPUT:
# ['banana', 'apple', 'cherry']