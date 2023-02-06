def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split(' '))[::-1]

sentence = str(input())
print(rev_copy_reverse(sentence))