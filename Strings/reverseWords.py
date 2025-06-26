def reverseWords1(s):
    parts = s.split(' ')
    words = []
    for word in parts:
        if word != '':
            words.append(word)
    words.reverse()
    return ' '.join(words)
print(reverseWords1("  Hello   World  "))  # Output: "World Hello"

def reverseWords2(s):
    words = s.split()  # splits on all whitespace and ignores extras
    return ' '.join(reversed(words))
print(reverseWords2("  Hello   World  "))  # Output: "World Hello"

def reverseWords3(s):
    return ' '.join(s.split()[::-1])
print(reverseWords3("  Hello   World  "))