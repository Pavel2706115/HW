# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write an EvensIterator class, such that its objects can be used in for loops, iterating over the even numbers in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE
# class EvensIterator:
#     def __init__(self, start, end):
#         self.start = start if start % 2 == 0 else start + 1
#         self.end = end
#         self.current = self.start

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             even_number = self.current
#             self.current += 2
#             return even_number
    
    

# ### TEST:
# for x in EvensIterator(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a generator function (evens_generator), such that will yield an even number
in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE
# def evens_generator(start, end):
#     if start % 2 != 0:
#         start += 1

#     for number in range(start, end + 1, 2):
#         yield number

# ### TEST:
# for x in evens_generator(1,10):
#     print(x, end=", ")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''
print( chr(1041) )
# 'Б'
print( chr(1071) )
# 'Я'
"""


### YOUR CODE HERE
# def cyrilic_letter_generator():
#     for code in range(1040, 1072):
#         yield chr(code)

# # TEST:
# for l in cyrilic_letter_generator():
#     print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create both a generator function (words_from_sentence) and an iterator class (WordsFromSentence) that produces words from a sentence. Both should split the input sentence by spaces and return each word
one at a time when iterated over.
Your implementation should handle empty sentences properly.
"""
# Case 1
    # class WordsFromSentence:
    #     def __init__(self, sentence):
    #         self.words = sentence.split()
    #         self.index = 0

    #     def __iter__(self):
    #         return self

    #     def __next__(self):
    #         if self.index < len(self.words):
    #             word = self.words[self.index]
    #             self.index += 1
    #             return word
    #         else:
    #             raise StopIteration
# Case 2
    # def words_from_sentence(sentence):
    #     words = sentence.split()
    #     for word in words:
    #         yield word

### YOUR CODE HERE


# # TEST Case 1: Using the iterator class
# print("Test with iterator class:")
# for w in WordsFromSentence("This is a test"):
#     print(w)

# # TEST Case 2: Using the generator function
# print("\nTest with generator function:")
# for w in words_from_sentence("This is a test"):
#     print(w)

### EXPECTED OUTPUT:
# Test with iterator class:
# this
# is
# a
# test
#
# Test with generator function:
# this
# is
# a
# test