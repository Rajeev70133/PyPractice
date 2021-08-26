# You are given a string and two markers (the initial and final). You have to find a substring enclosed between these
# two markers. But there are a few important conditions:
# The initial and final markers are always different.
# If there is no initial marker, then the first character should be considered the beginning of a string.
# If there is no final marker, then the last character should be considered the ending of a string.
# If the initial and final markers are missing then simply return the whole string.
# If the final marker comes before the initial marker, then return an empty string.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output: A string.
#
# Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string

def between_markers(text: str, bgn: str, end: str) -> str:
    bgn_index = text.index(bgn) + len(bgn) if bgn in text else 0
    end_index = text.index(end) if end in text else len(text)
    return text[bgn_index:end_index]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
#
# This is a simplified version of the Between Markers mission.
#
# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output: A string.
#
# Precondition: There can't be more than one final and one initial markers.

# def between_markers(text: str, begin: str, end: str) -> str:
#     if begin in text:
#         begin_index = text.find(begin) + len(begin)
#     else:
#         begin_index = 0
#
#     if end in text:
#         end_index = text.find(end)
#     else:
#         end_index = len(text)
#
#     return text[begin_index:end_index]


