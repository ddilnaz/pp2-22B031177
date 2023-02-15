def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split(' '))[::-1]

sentence = str(input())
print(reverse_words(sentence))