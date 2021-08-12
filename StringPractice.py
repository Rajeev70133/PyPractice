# Glossary¶
#
# aliases
# Multiple variables that contain references to the same object.
#
# boolean value
# There are exactly two boolean values: True and False. Boolean values result when a boolean expression is evaluated by the Python interepreter. They have type bool.
#
# boolean expression
# An expression that is either true or false.
#
# clone
# To create a new object that has the same value as an existing object. Copying a reference to an object creates an alias but doesn’t clone the object.
#
# comparison operator
# One of the operators that compares two values: ==, !=, >, <, >=, and <=.
#
# compound data type
# A data type in which the values are made up of components, or elements, that are themselves values.
#
# element
# One of the parts that make up a sequence type (string, list, or tuple). Elements have a value and an index. The value is accessed by using the index operator ([*index*]) on the sequence.
#
# immutable data type
# A data type which cannot be modified. Assignments to elements or slices of immutable types cause a runtime error.
#
# index
# A variable or value used to select a member of an ordered collection, such as a character from a string, or an element from a list or tuple.
#
# logical operator
# One of the operators that combines boolean expressions: and, or, and not.
#
# mutable data type
# A data type which can be modified. All mutable types are compound types. Lists and dictionaries are mutable data types; strings and tuples are not.
#
# nested list
# A list that is an element of another list.
#
# slice
# A part of a string (substring) specified by a range of indices. More generally, a subsequence of any sequence type in Python can be created using the slice operator (sequence[start:stop]).
#
# step size
# The interval between successive elements of a linear sequence. The third (and optional argument) to the range function is called the step size. If not specified, it defaults to 1.
#
# traverse
# To iterate through the elements of a collection, performing a similar operation on each.
#
# tuple
# A data type that contains a sequence of elements of any type, like a list, but is immutable. Tuples can be used wherever an immutable type is required, such as a key in a dictionary (see next chapter).
#
# tuple assignment
# An assignment to all of the elements in a tuple using a single assignment statement. Tuple assignment occurs in parallel rather than in sequence, making it useful for swapping values.

# # All methods #########################################

# anyThing = 1, 3, 6, 1, 7
# print(type(anyThing))
# print(anyThing)

# anyThing = (6,)  # tuple type
# print(type(anyThing))
# print(anyThing)
#
# anyThing = (3)  # int type
# print(type(anyThing))
# print(anyThing)
#
# anyThing = ()
# print(type(anyThing))
# print(anyThing)
#
# anyThing = "apple"  # Str type ad we can use '' also
# print(type(anyThing))
# print(anyThing)
# print(anyThing[3])
# print(len(anyThing))
#
# anyThing = ['apples', 'cherries', 'pears']  # list type
# print(type(anyThing))
# print(anyThing)
# print(anyThing[2])
# print(len(anyThing))
#
# anyThing = (3.99, 6.00, 10.00, 5.25)  # tuple type
# print(type(anyThing))
# print(anyThing)
# print(anyThing[3])
# print(len(anyThing))
#
# anyThing = 3.99  # float type
# print(type(anyThing))
# print(anyThing)
# # print(anyThing[3])
# # print(len(anyThing))
#
# anyThing = [('cheese', 'queso'), ('red', 'rojo'), ('school', 'escuela')]  # List type
# print(type(anyThing))
# print(anyThing[1])
# print(len(anyThing))
#
# # anyThing = [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
# anyThing = [('cheese', 'queso'), ('red', 'rojo'), ('school', 'escuela')]  # List type
# # anyThing = 'thisislast'
# lastOfanyThing = anyThing[len(anyThing) - 2]
# print(lastOfanyThing)
#
# anyThing = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#
# for num in anyThing:  # squre cube powers etc.
#     print(num ** 3)
#
# anyThing = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos']
# for indx, anyThing in enumerate(anyThing):  # fetching elemnts of list one by one
#     print("The element " + anyThing + " is in position " + str(indx) + ". samjhey beta")
#
# anyThing = 'Peter, Paul, and Mary'
# print(anyThing[3:9])
# print(type(anyThing))
#
# anyThing = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos', 'cherry', 'litchi', 'JackFruit', 'Grapes',
#             'Watermelon']
# print("The element " + anyThing[2] + " is in position " + str(indx) + ". samjhey beta")
# print(type(anyThing))
#
# anyThing = ["apples", "bananas", "blueberries", "oranges", "mangos", "cherry", "litchi", "JackFruit", "Grapes",
#             "Watermelon"]
# print(anyThing[2:5])
# print(type(anyThing))
#
# anyThing = "banana"
# print(anyThing[:])
# print(anyThing[:3])
# print(anyThing[3:])
# print(anyThing[-3:])
# print(anyThing[:-3])
# print(anyThing[-4:5])
# print(type(anyThing))
#
# anyThing = ('apples', 'bananas', 'blueberries', 'oranges', 'mangos', 'cherry', 'litchi', 'JackFruit', 'Grapes', 'Watermelon')
# print(type(anyThing))
# print(anyThing[:-2])
# print(anyThing[-3:])
# print(anyThing[:-2])
# print(anyThing[3])
#
# anyThing = [(1, 2), [8, 32, 43], '12', 12, 12.0]
# print(anyThing[:])
# print(len(anyThing))
# print(type(anyThing))
# print(anyThing[0])
# print(len(anyThing[0]))
# print(type(anyThing[0]))
# print(anyThing[1])
# print(len(anyThing[1]))
# print(type(anyThing[1]))
# print(anyThing[2])
# print(type(anyThing[2]))
# print(anyThing[3])
# print(type(anyThing[3]))
# print(anyThing[4])
# print(type(anyThing[4]))
#
# anyThing = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos', 'cherry', 'litchi', 'JackFruit', 'Grapes',
#             'Watermelon']
# print('cherry' in anyThing)
# print('cherryee' in anyThing)
#
# anyThing = (2, 4, 6, 8)
# print(anyThing)
# print(type(anyThing))
# # a = anyThing[2]
# a = 9
# print(a in anyThing)
#
# anyThing = ' 12_apPles.'
# print(anyThing)
# print(type(anyThing))
# print(type(a))
# print('pPl' in anyThing)
# print(anyThing.upper())
# print(anyThing.lower())
# print(anyThing.capitalize())
# print(anyThing.strip()) # remove spaces
# # print(anyThing.strip())
#
# anyThing = 'mississippi'
# print(anyThing.startswith('Miss'))
#
# anyThing = '2'
# print(anyThing.isdigit())

# print(dir(str))
# a = str.replace.__doc__
# print(a)
# print(str.replace.__doc__)

# anyThing = 'Misspicieep'
# print(anyThing.replace('i', 'I'))
# print(anyThing.replace('p', 'Going'))
# print(anyThing.replace('i', ' ', 2))

# print(str.count.__doc__)  #Return the number of non-overlapping occurrences of substring sub in string S[start:end].
# print(tuple.count.__doc__) # Return number of occurrences of value. S.index(sub[, start[, end]]) -> int
# print(list.count.__doc__)  #Return number of occurrences of value.
# print(str.index.__doc__)   # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Raises ValueError when the substring is not found.
# print(tuple.index.__doc__)  #Return first index of value. Raises ValueError if the value is not present.
# print(list.index.__doc__)  # Return first index of value. Raises ValueError if the value is not present.

# anyThing = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos']
# print(anyThing[0])
# print(anyThing[-2])
# print(anyThing)
# # anyThing[0] = 'pears', 'beries' # Item Assignment is assignment to an element of a list is called item assignment.
# # print(anyThing)
# anyThing[1:3]= []
# # anyThing[0:2] = ['abc', 'hdhdh']
# print(anyThing)

# a_list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(a_list)
# a_list[0:4] = ['x', 'y'] # 0 is index position of updation of list and 4 is lenth till we want to replace and update
# print(a_list)
# # Same example with differc [index:len]
# a_list = ['a', 'd', 'e', 'f']
# print(a_list)
# a_list[1:0] = ['b', 'c'] # 1 is index position of updation of list and 0 is lenth we want to replace and update
# print(a_list)
# # another example
# a_list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(a_list)
# a_list[1:4] = [] # 0 is index position of updation of list and 4 is lenth till we want to replace and update
# print(a_list)
# # another example
# a_list = ['a', 'd', 'f']
# print(a_list)
# a_list[1:0] = ['b', 'c'] # 1 is index position of updation of list and 0 is lenth we want to replace and update
# print(a_list)
# a_list[4:0] =['e']
# print(a_list)

# a = ['one', 'two', 'three', 'four', 'three']
# print(a)
# # del a[2]
# del a[1:4]
# print(a)

# my_list = []
# my_list.append('this')
# print(my_list)
# my_list.append('that')
# print(my_list)
# my_list.insert(1, 'thing')
# print(my_list)
# my_list.insert(4, 'thing')
# print(my_list)
# my_list.reverse()
# print(my_list)

# a = [1, 2, 3, '23']
# b = [1, 2, 3]
# print(a)
# print(b)
# print(a==b)
# print(a is b)
# print(a[0])
# b = a[:]  # cloning
# print(b)


# If we print nested[3], we get [10, 20]. To extract an element from the nested list, we can proceed in two steps:
# a = ["hello", 2.0, 5, [10, 20]]
# elem = a[3]
# # print(elem)
# print(a[3])
# elem = a[0:2]
# print(elem)
# print(a[3][0])

# # String and list
# print(list("Crinchy Toast inside the container".split('in')))
# print(list("Crinchy Toast inside the container".split()))
# print(list("Crinchy Toast"))
# print(' '.join(['Crinchy', 'Toast', 'inside', 'the', 'container']))
# print('*'.join(['Crinchy', 'Toast', 'inside', 'the', 'container']))
# print(''.join(['Crinchy', 'Toast', 'inside', 'the', 'container']))

# Tuple is Immutable
# a, b, c, d= 1, 2, 3, 4
# print(c)
# Boolean values
# print(type(True))
# print(type(False))
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# numbers = (5, 11, 13, 24)
# print(numbers[2]%2 == 0)
# print(len(numbers) >= 5 and numbers[2] !=0)

# Truthiness : All Python values have a “truthiness” or “falsiness”
# print('B' and 'Apples')
# print('B' and (2, 6))
# print('B' and [2, 6])
# print('' or {5, 6})
# print('' or [5, 6])
# print(0 and ['ayNams', 6]
# print(('a', 'b', 'c') or [5, 6])
# print('apple' in 'Pineapple')
# print('Python'[:1])
# print('pear' not in 'Pineapple')
# print('e' in 'Pineapple')
# print("Strings are sequences of characters hai".split())
# print(len("wonderful"))

# word = "sdfghjertyuicvbnmFGHJsdfghjkhj"
# print(word[6]+ word[9])
# print(bool(word[6]==word[9]))

# print([("cheese", "queso"), ("rrj", "rojo")][1][0][2])  # output: j
# print('aqqqqqwertyu'.count())
# print('Mississippi'.count('s')
# print('Python'.upper())
# print('Python'.upper())
# letters = [1, 5, -1, 3]
# print(letters.sort())
# print(letters)
# print('Splitting worg of a sentance..'.split())
# anystr = 'Splitting worg of a sentance..'
# print(anystr.split())
# >>> mystery
# tup = 'any', 'py', 'lan', 'tree'
# print(tup.index('len'))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


# Joining all the items of a lit if all the items are of one type
# def addListItems(letters):
#     adda = ""
#     for x in letters:
#         adda = adda + x
#     return adda
#
#
# letters = ['c', 'z', 'b', 's']
#
# print(addListItems(letters))
# Below is another way of adding list
# letters = ['c', 'z', 'b', 's']
# print(''.join(letters))
# abc = ['Crinchy', 'Toast', 'inside', 'the', 'container']
# print(''.join(abc))

# def revWord(abc):
#     # using recursion
#     if len(abc) == 0:
#         return abc
#     else:
#         return revWord(abc[1:])+abc[0]
#     # Using for loop
#     # stri = ""
#     # for x in abc:
#     #     stri = x+stri
#     # return stri
#
# abc = "hello this"
# print(abc)
# print(revWord(abc))
# print((abc[1:])+ abc[0])

# def revWord(abc):
#     # using recursion
#     if len(abc) == 0:
#         return abc
#     else:
#         return revWord(abc[1:])+abc[0]
#     # Using for loop
#     # stri = ""
#     # for x in abc:
#     #     stri = x+stri
#     # return stri
#
# abc = "helloReversingWord"
# print(abc)
# print(revWord(abc))
# print((abc[1:])+ abc[0])

# Python code to reverse a string
# using stack

# Function to create an empty stack. It
# initializes size of stack as 0
# def createStack():
#     stack = []
#     return stack
#
#
# # Function to determine the size of the stack
# def size(stack):
#     return len(stack)
#
#
# # Stack is empty if the size is 0
# def isEmpty(stack):
#     if size(stack) == 0:
#         return True
#
#
# # Function to add an item to stack . It
# # increases size by 1
# def push(stack, item):
#     stack.append(item)
#
#
# # Function to remove an item from stack.
# # It decreases size by 1
# def pop(stack):
#     if isEmpty(stack): return
#     return stack.pop()
#
#
# def reverse(string):
#     n = len(string)
#
#     # Create a empty stack
#     stack = createStack()
#
#     # Push all characters of string to stack
#     for i in range(0, n, 1):
#         push(stack, string[i])
#
#     # Making the string empty since all
#     # characters are saved in stack
#     string = ""
#
#     # Pop all characters of string and put
#     # them back to string
#     for i in range(0, n, 1):
#         string += pop(stack)
#
#     return string
#
#
# # Driver code
# s = "Geeksforgeeks"
# print("The original string  is : ", end="")
# print(s)
# print("The reversed string(using stack) is : ", end="")
# print(reverse(s))

# splitedAbc = abc.split()

# splitedAbc = abc.split(" ")
# print(splitedAbc)
# print(splitedAbc[::2])
# splitedWord = [splitedAbc[::-1] for x in splitedAbc]
# reversedStr = "".join(splitedWord)
# print(reversedStr)
# def revWord(splitedAbc):
#     rever =""
#     for x in splitedAbc:
#         rever = rever +x(len(rever)-1)
#     return rever
# print(revWord(splitedAbc))# def revWord(splitedAbc):
#     rever =""
#     for x in splitedAbc:
#         rever = rever +x(len(rever)-1)
#     return rever
# print(revWord(splitedAbc))

#
# # Python code to Reverse each word
# # of a Sentence individually
#
# # Function to Reverse words
# def reverseWordSentence(Sentence):
#     # Splitting the Sentence into list of words.
#     words = Sentence.split(" ")
#
#     # Reversing each word and creating
#     # a new list of words
#     # List Comprehension Technique
#     newWords = [word[::-1] for word in words]
#
#     # Joining the new list of words
#     # to for a new Sentence
#     newSentence = " ".join(newWords)
#
#     return newSentence
#
#
# # Driver's Code
# Sentence = "GeeksforGeeks is good to learn"
# # Calling the reverseWordSentence
# # Function to get the newSentence
# print(reverseWordSentence(Sentence))


# Python code to Reverse each word
# of a Sentence individually

# Function to Reverse words of sentence///////////////////////
# def reverseWordSentence(Sentence):
#     # All in One line
#     return ' '.join(word[::-1] for word in Sentence.split(" "))
#
#
# # Driver's Code
# Sentence = "Geeks for Geeks"
# print(reverseWordSentence(Sentence))

#  Lis of dictionary //////////  Lis of dictionary////////////////
# lis = [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]
# print(lis)
# abc = sorted(lis, key=lambda i: i['age'])
# # abc = sorted(lis, key=lambda i: i['age'], reverse=True)
# print(abc[1:2])

# def bigger_price(limit: int, data: list) -> list:
#     """
#         TOP most expensive goods
#     """
#     # your code here
#     a = sorted(data, key=lambda i: i['price'], reverse=True)
#     return a[0:limit]
#
#
# if __name__ == '__main__':
#     from pprint import pprint
#
#     print('Example:')
#     pprint(bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]))
#
#     # These "asserts" using for self-checking and not for auto-testing
#     assert bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]) == [
#                {"name": "wine", "price": 138},
#                {"name": "bread", "price": 100}
#            ], "First"
#
#     assert bigger_price(1, [
#         {"name": "pen", "price": 5},
#         {"name": "whiteboard", "price": 170}
#     ]) == [{"name": "whiteboard", "price": 170}], "Second"
#
#     print('Done! Looks like it is fine. Go and check it')

# # vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
#
# # # sort the vowels in reverse
# # vowels.sort(reverse=True)
# # print(vowels)
#
# # # print vowels
# # print('Sorted list:', sorted(vowels))

# def lis(elemts):
#     return elemts[1]
#
# randomList = [(9,1), (3,8), (2,7), (7,9), (2,4), (1,3)]
# print(randomList)
#
# randomList.sort(key=lis)
#
# print(randomList)

# # sorting using custom key
# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, ]
#
#
# # custom functions to get employee info
# def naam(emps):
#     return emps.get('Name')
# def umar(emps):
#     return emps.get('age')
# def tanqa(emps):
#     return emps.get('Name')
#
# # sorting in accending
# employees.sort(key=tanqa, reverse=True)
# print(employees, end='\n\n')
#
# employees.sort(key=tanqa, reverse=False)
# print(employees, end='\n\n')
#
# employees.sort(key=naam, reverse=True)
# print(employees, end='\n\n')
#
# employees.sort(key=naam, reverse=False)
# print(employees, end='\n\n')
#
# employees.sort(key=umar, reverse=True)
# print(employees, end='\n\n')
#
# employees.sort(key=umar, reverse=False)
# print(employees, end='\n\n')

# # custom functions to get employee info # another example using LAMBDA
# employees.sort(key=lambda x: x.get('Name'))
# print(employees, end='\n')
#
# employees.sort(key=lambda x: x.get('age'))
# print(employees, end='\n')
#
# employees.sort(key=lambda x: x.get('salary'), reverse=True)
# print(employees, end='\n')

"""# LAMDA #
def minu(x-y):
    return x-y
Above can be achived in another way
minu = lambda x, y: x-y
"""
# # def a_func(a):
# #     return a[1]
#
# a = [[1, 3], [2,9], [12, 77]]
# a.sort(key=lambda x:x[1])
# print(a)

# def double(n):
#     return n*2

# double = lambda n:n*2
# print(10)

# larg = lambda a,b:a if a>b else b
# print(larg(10, 20))

# a = ["jshhj","kjsdhkj", "ka", "kjdsdskksks"]
# a.sort(key=lambda b:len(b), reverse=True)
# print(a)

# Program to filter out only the even items from a list and maping values
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# intotow_list = list(map(lambda a:a*2, new_list))
#
# print(new_list)
# print(intotow_list)

#  Simple funcion
# def greet(name):
#     return ("Hello, " + name + ". Good morning!")
# print(greet('Rajeev'))

# Python Function Arguments
# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)
# def greet(nam):
#     """This is a function discription"""
#     print("Aapka naam hai *"+nam+"*! DHANYAWAD")
# print(greet("Raam"))
# print(greet.__doc__)
#
# def returning_absolute_val(numb):
#     """This function returns the absolute
#         value of the entered number. non zero"""
#     if numb>=5:return numb
#     else:return numb*2
# print(returning_absolute_val(2))
#
# # Program to illustrate
# # the use of user-defined functions
#
# def add_numbers(x,y):
#    sum = x + y
#    return sum
#
# num1 = 5
# num2 = 6
#
# print("The sum is", add_numbers(num1, num2))

# a= [4, 6, 2, 2, 6, 4, 4, 6]
# a.sort(key=lambda x: x, reverse=True )
# print(a)
# l = ['bob', 'bob', 'carl', 'alex', 'bob']
# def sorting(emp):
#     emp = l
#     new_lst = []
#     for i in emp:
#         if emp[0]== emp[len(l)-1]:
#             return new_lst.append(i)
#         else:return i
#
# l = ['bob', 'bob', 'carl', 'alex', 'bob']
# l.sort(key=sorting(l))
# print(l)

#
# Working#
# from collections import Counter
#
# def frequency_sort(items):
#     counts = Counter(items)
#     return sorted(items, key=lambda k: counts[k] * len(items) - items.index(k), reverse=True)
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# from collections import Counter
#
# l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# # d = Counter(l1)
# # print(d)
#
# new_list = list([item for item in l1 if l1[0] == l1[-1]], any)
# print(new_list)


# l.sort(key=lambda  x:x, reverse=True)

# Counter

# Python code to demonstrate
# sort list by frequency
# of elements
import datetime
import math
import time
from collections import Counter
from itertools import repeat, chain

# ini_list = [4, 6, 2, 2, 6, 4, 4, 4]

# # printing initial ini_list
# print("initial list", str(ini_list))
#
# # sorting on bais of frequency of elements
# result = [itm for itms, a in Counter(ini_list).most_common() for itm in [itms]* a]
#
# # printing final result
# print("final list", str(result))
# # Another iterable method
# print(ini_list)
# # ini_listToStr=str(ini_list)
# result = list(chain.from_iterable(repeat(i, a) for i, a in Counter(ini_list).most_common()))
# print(result)
#  # using sorted
# result =sorted(ini_list, key=ini_list.count, reverse=True)
# result = [itm for itms, a in Counter(ini_list).most_common() for itm in [itms]* a]
# result = sorted(ini_list, key=ini_list.count, reverse=True)
# print(result)

# a = "hi may or"
# b = " "
# c=list(a)
# if b in c:
#     res = c.index(b)
#     # print(res)
#     res_f = c.index(b, res+1, len(c))
#     print(res_f)
# else:
#     print("No match")
# if a.count(b)<2:
#     print("no matchg")
# else:
#     res = c.index(b)
#     # print(res)
#     res_f = c.index(b, res+1, len(c))
#     print(res_f)


# def second_index(text: str, symbol: str) -> [int, None]:
#     """
#         returns the second index of a symbol in a given text
#     """
#
#     # your code here
#     ls = list(text)
#     if text.count(symbol)<2:
#         return None
#     else:
#         first_one = ls.index(symbol)
#         second_one = ls.index(symbol, first_one+1, len(ls))
#         return second_one
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(second_index("sims", "s"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert second_index("sims", "s") == 3, "First"
#     assert second_index("find the river", "e") == 12, "Second"
#     assert second_index("hi", " ") is None, "Third"
#     assert second_index("hi mayor", " ") is None, "Fourth"
#     assert second_index("hi mr Mayor", " ") == 5, "Fifth"
#     print('You are awesome! All tests are done! Go Check it!')

# TRY Exception
# print("Enter 1st numbe:")
# num1= input()
# print("Enter 2nd number:")
# num2 = input()
# try:
#     print("Sub of numbers is: ", int(num2)- int(num1))
# except Exception as e:
#     print("galat forma")

# """
# "r -Open read mode
# "w" -Write mode
# "x" - Create file
# "a" - Add content
# "t" - text mode
# "b" - binary mode
# "+" - read write
# """
# Appending file
# f = open("abcTestFile.txt", "a")
# a= f.write("Adding new lines..\n")
# print(a)

# Perform read and write file both/////////////////

# with open("abcTestFile.txt") as f:
#     a = f.read()
#     print(a)
# f = open("abcTestFile.txt", "r+")
# print(f.tell())
# print(f.readline())
# f.tell()
# print(f.readline())
# print(f.read())
# f.write("Adding new lines...........3")


# print(f.read())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# cont =f.read()

# for a in f:
#     print(a)
# print(cont)
# containing = f.read(10)
# print(containing)
#
# containing = f.read(5)
# print(containing)

# f.close()

# RECURSION////////////////
"""n = 5
5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * factorial_recursive(1)
5 * 4 * 3 * 2 * 1 = 120"""

# def factorial_recursive(n):
#     if n ==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# aank = int(input("Enter your number"))
# print(factorial_recursive(aank))

"""
n! = n * n-1 * n-2 * n-3... 1
n1 = n * (n - 1)!
:param n: Integer
:return: n * n-1 * n-2 * n-3..
"""
# def factorial_iterative(n):
#     """
#     n! = n * n-1 * n-2 * n-3... 1
#     n1 = n * (n - 1)!
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3..
#     """
#     factor = 1
#     for i in range(n):
#         factor = factor * (i+1)
#     return factor
#
# aank = int(input("Enter your number"))
# print(factorial_iterative(aank))

"""
0 1 1 2 3 5 8 13
"""
# def fibonacii(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacii(n-1)+fibonacii(n-2)
#
# aank = int(input("Enter your number"))
# print(fibonacii(aank))


#     print("This string " + str1)
#
# printin1("Any String")


"""import DateTimeDifference"""
# # # t = time.gmtime()
# # import time
# # from datetime import timedelta
# #
# # today = datetime.date.today()
# # print(today)
# # print(today == datetime.date.fromtimestamp(time.time()))

# d = timedelta(microseconds=-1)
# print(d)
# print(str(d))
# print(d.days, d.min)
# print(d.days,d.seconds,d.microseconds)

"""# import random
"""
#
# rn=random.randint(0, 1)
# # print(rn)
# ran =random.random() * 100
# # print(ran)
# lst = ["qwer s", "ghj", "qazwsx", "qazwsx", "edvrfb"]
# chose = random.choice(lst)
# print(chose)
""" F String"""
# me = "Raje"
# a1 = 3
# # a = "this is %s%s"%(me, a1)
# # a = "this is {1} {0}"
# # b = a.format(me,a1)
# # print(b)
# a = f"This is {me} and {a1} and {math.cos(65)} "
# print(a)

# def func_nam_prnt(a, b, c, d):
#     print(a, b, c, d)
# func_nam_prnt("abc", "def", "ghi", "jkl")
"""*args, **kwargs"""
# def funArgs(normal, *args, **kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     print("\nHere are out heros:")
#     for key, value in kwargs.items():
#         print(f"{key}, is the {value}")
#     # print(type(args))
#     # print(args[0])
#
# func_nam_prnt=["abc", "def", "ghi", "jkl"]
# normal_main = "This is normal now"
# kw = {"Amit":"Monitor", "Sumit":"Ladchat", "Asim": "LadChato Ka Monitor"}
# funArgs(normal_main, *func_nam_prnt, **kw)

"""Enumerate"""

# lis=["abc", "def", "ghi", "jkl", "qmsn"]
"""Iterate"""
# i = 1
# for item in lis:
#     if i%2 != 0:
#         print(f"Pleales print: {item}")
#     i += 1
"""Enumerate"""
# for indx, item in enumerate(lis):
#     if indx%2 == 0:
#         print(f"Please print : {item}")
"""Import another file values"""
# import sys
# # print(sys.path)
#
# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())
#
# import CountingDigitsInStr
# print(CountingDigitsInStr.c)
# CountingDigitsInStr.anyJoke("My Joke")
"""__name__=__main__"""
# import CountingDigitsInStr
#
# print(CountingDigitsInStr.wanna_add(10, 11))

"""Join Functions"""
# lis=["abc", "def", "ghi", "jkl", "qmsn"]

# for items in lis:
#     print(items, "AND", end="**")
# Above can be achived using JOIN
# a =" AND ".join(lis)
# print(a, "other WWE sstars")

"""Map & Filter"""
# numbers = ["2","42","77", "12", "14", "15"]
# numbers = list(map(int, numbers))
#
# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
# #
# # numbers[2]=numbers[2]+1
# # print(numbers[2]+1)
# numbers[2]=numbers[2]+1
# # print(numbers[2])
# num = [2, 3, 6, 7, 1, 5]
"""Map function use"""
# square = list(map(lambda x:x*x, num))
# print(square)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# funcLis = [square, cube]
# for i in range(len(num)):
#     valu = list(map(lambda x:x(i), funcLis))
#     print(valu)
"""Filter function"""
# def is_greater(num):
#     return num>5
#
# greter_than = list(filter(is_greater, num))
# print(greter_than)
"""Reduce"""
# from functools import reduce
#
# num = [2, 3, 6, 7, 1, 5]
# # using itteration
# # a=0
# # for i in num:
# #     a= a+i
# # print(a)
# # using reduce
# prod =reduce(lambda x,y:x+y, num)
# print(prod)
"""Decorators"""
# def func1():
#     print("abc printing")
#
# func2=func1
# # del func1
# func2()
# def func_ret(n):
#     if n==0:
#         return print
#     if n == 1:
#         return sum
#
# a = func_ret(1)
# print(a)
"""Function print as argument"""


# def execute(fun):
#     fun("This")
#
# execute(print)
"""@decorator"""
# def dec1(fun1):
#     def exec():
#         print("Executing now")
#         fun1()
#         print("endinnn")
#
#     return exec
#
# @dec1
# def what_is_this():
#     print("This is decorator")
#
#
# # what_is_this = dec1(what_is_this)
# what_is_this()



# from CountingDigitsInStr import a

# print(a)

# # ########## Class Example # Multiple inheritance################################################
# class A:
#     def met(self)
#         print("This s met A method")
#
#
# class B(A):
#     def met(self):
#         print("This s met B method")
#
#
# class C(A):
#     def met(self):
#         print("This is C class")
#     # def met(self):
#     #     pass
#         # print("This s met C method")
#
#
# class D(C, B):
#     pass
#     # def met(self):
#     #     pass
#         # print("This is method D of set")
#
# a=A()
# b=B()
# c=C()
# d=D()
#
# d.met()
###########################################################################
# string = "Geek1 \nGeek2 \nGeek3"
# # string = "Geek1 Geek2 Geek3"
# print(string)
# print(string.split())
# print(string.split(' ', 1))


# import os
#
# currentDirectory = os.getcwd()
# print(currentDirectory)
# checking python is installed  and wher
# import subprocess

# String initialization
# String initialization

#
# # Defining splitting point
# n = 3
#
# # Using list comprehension
# out = [(string[i:' ']) for i in range(0, len(string), n)]
#
# # Printing output
# print(out)

# word1 = 'frog'
# word2 = 'friend'
# print(lambda ab: ab[0] == ab[1], zip(word1, word2))
# Python 3.x (see comments for pointers re: changes):
#
# >>> word1 = 'frog'
# >>> word2 = 'friend'
# >>> len(list(filter(lambda xy: xy[0] == xy[1], zip(word1, word2))))
# 2


#
# def run_command(command):
#     p = subprocess.Popen(command,
#     stdout = subprocess.PIPE,
#     stderr = subprocess.STDOUT)
#     return iter(p.stdout.readline, b'')
# out = list(run_command("java -version"))


# # def backward_string_by_word(text: str) -> str:
# #     # your code y
#     def rever(sentance):
#         if len(sentance) == 0:
#             return sentance
#         else:
#             return rever(sentance[1:]) + sentance[0]
#     return rever(sentance=text)
# #
# #
# # if __name__ == '__main__':
# #     print("Example:")
# #     print(backward_string_by_word(''))
# #
# #     # These "asserts" are used for self-checking and not for an auto-testing
# #     assert backward_string_by_word('') == ''
# #     assert backward_string_by_word('world') == 'dlrow'
# #     assert backward_string_by_word('hello world') == 'olleh dlrow'
# #     assert backward_string_by_word('hello   world') == 'olleh   dlrow'
# #     assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
# #     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# # Python3 program to reverse individual words
# # in a given string using STL list
#
# # reverses individual words of a string
# def reverserWords(strng):
#     st = list()
#
#     for i in range(len(strng)): # Traverse given string and push all characters
#         if strng[i] != " ":  # to stack until we see a space.
#             st.append(strng[i])
#
#         # contents of stack.
#         else:
#             while len(st) > 0:
#                 print(st[-1], end="")  # When we see a space, we print
#                 st.pop()
#             print(end=" ")  # contents of stack printed and deleted
#
#     # Since there may not be space after
#     # last word.
#     while len(st) > 0:
#         print(st[-1], end="") # last word.
#         st.pop()
#
#
# # Driver Code
# if __name__ == "__main__":
#     string = 'hello world'
#     reverserWords(string)
#
# # This code is contributed by
# # sanjeev2552
#
# # s = "Geeksfo rgeeks"
# #
# #
# # def rever(sentnce):
# #     if len(sentnce) == 0:
# #         return sentnce
# #     else:
# #         return rever(sentnce[1:]) + sentnce[0]
# #
# #
# # a = rever(sentnce=s)
# # print(a)
#
# # def rever(sentance):
# #     if len(sentance) == 0:
# #         return sentance
# #     else:
# #         return rever(sentance[1:]) + sentance[0]
# #
# #
# # s = "Geeksfo rgeeks"
# #
# # print("The original string  is : ", end="")
# # print(s)
# #
# # print("The reversed string(using recursion) is : ", end="")
# # print(rever(s))
#
# # def rev(s):
# #     stri = ""
# #     for i in s:
# #         stri = i + stri
# #         return stri
# #
# #
# # s = "abcd efgh ijkl"
# # print(rev(s))
# You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.
#
# Some possible cases:
#
# Filename cannot be an empty string;
# Files without the extension should go before the files with one;
# Filename ".config" has an empty extension and a name ".config";
# Filename "config." has an empty extension and a name "config.";
# Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
# Filename ".imp.xls" has an extension "xls" and a name ".imp".
# Input: A list of filenames.
#
# Output: A list of filenames.

# from typing import List

# def sorting():
# a = (['1.cad', '1.bat', '1.aa'])
# for i in a:
#     if a[i]=
#     print(a[0])

# These "asserts" are used for self-checking and not for an auto-testing
# assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
# assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
# assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
# assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
# assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
# assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
# assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
# print("Coding complete? Click 'Check' to earn cool rewards!")
# sentence = "GeeksforGeeks is good to learn"

# def revWordOfSentance(sentence):
#     sent_word = sentence.split(" ")
#     newWord = [word[::-1] for word in sent_word]
#     newSent = " ".join(newWord)
#     return newSent
#
# print(revWordOfSentance(sentence))
