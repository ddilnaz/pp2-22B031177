def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

soz = input()
print(is_palindrome(soz))