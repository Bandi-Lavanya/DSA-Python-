#Without using join and reverse methods, reverse the words in a sentence.
def reverse_words_brute1(sentence):
    print("Before reversing words:")
    print(sentence)

    sentence += " "  # Append space at end to handle last word
    stack = []
    word = ""

    for ch in sentence:
        if ch == ' ':
            stack.append(word)
            word = ""
        else:
            word += ch

    ans = ""
    while len(stack) > 1:
        ans += stack.pop() + " "
    ans += stack.pop()  # Last word without trailing space

    print("After reversing words:")
    print(ans)

# Example usage
s = "Hi I am a student"
reverse_words_brute1(s)

def reverse_words_brute2(s):
    return ' '.join(s.split()[::-1])

st = "Hi I am a student"
print("Before reversing words:")
print(st)
print("After reversing words:")
print(reverse_words_brute2(st))


def result_optimal(s):
    left = 0
    right = len(s) - 1
    temp = ""
    ans = ""

    # Iterate through the string to form words manually
    while left <= right:
        ch = s[left]
        if ch != ' ':
            temp += ch
        else:
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp
            temp = ""
        left += 1

    # Handle the last word
    if temp != "":
        if ans != "":
            ans = temp + " " + ans
        else:
            ans = temp

    return ans

# Main
st = "Hi I am a student"
print("Before reversing words:")
print(st)
print("After reversing words:")
print(result_optimal(st))
