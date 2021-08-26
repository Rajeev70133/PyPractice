# In this mission your task is to determine the popularity of certain words in the text.
# At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.
# When solving this task pay attention to the following points:
# The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
# The search words are always indicated in the lowercase.
# If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
# Input: The text and the search words array.
# Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
# Precondition :
# The input text will consists of English letters in uppercase and lowercase and whitespaces.
# import re
def popular_words(text: str, words: list) -> dict:
    # your code here
    text_lower = text.lower()
    splitted_words = text_lower.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")


# dataString = '''Life morning don't were in multiply yielding multiply gathered from it. She'd of evening kind creature lesser years us every, without Abundantly fly land there there sixth creature it. All form every for a signs without very grass. Behold our bring can't one So itself fill bring together their rule from, let, given winged our. Creepeth Sixth earth saying also unto to his kind midst of. Living male without for fruitful earth open fruit for. Lesser beast replenish evening gathering.
# Behold own, don't place, winged. After said without of divide female signs blessed subdue wherein all were meat shall that living his tree morning cattle divide cattle creeping rule morning. Light he which he sea from fill. Of shall shall. Creature blessed.
# Our. Days under form stars so over shall which seed doesn't lesser rule waters. Saying whose. Seasons, place may brought over. All she'd thing male Stars their won't firmament above make earth to blessed set man shall two it abundantly in bring living green creepeth all air make stars under for let a great divided Void Wherein night light image fish one. Fowl, thing. Moved fruit i fill saw likeness seas Tree won't Don't moving days seed darkness.
# '''
#
# keyWords = ['Life', 'stars', 'seed', 'rule']
#
# #---------------------- SOLUTION 1
#
# print("Sol rajeev")
# # print 'Solution 1 output:'
# # for keyWord in keyWords:
# #     print re.findall(keyWord, dataString)
# for keyWord in keyWords:
#     index = 0
#     indexes = []
#     indexFound = 0
#     while indexFound != -1:
#         indexFound = dataString.find(keyWord, index)
#         if indexFound not in indexes:
#             indexes.append(indexFound)
#         index += 1
#     indexes.pop(-1)
#     print(indexes)

# def popular_words():
#     string = "Python is awesome, isn't it?"
#     substring = "i"
#
#     # count after first 'i' and before the last 'i'
#     count = string.count(substring, 8, 26)
#     return count
#
#
# print(popular_words())

# if __name__ == '__main__':
#     print("Example:")
#     print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
