def is_palindrome(word):
    reversed_word = word[::-1]  # return word == word[::-1]
    if word == reversed_word:   # word == word[::-1]
        return True
    else:
        return False
print(is_palindrome("NidhdiN"))            