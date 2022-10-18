"""
Emma Naumann
CP1404 Practical 5

Word occurrences counts the occurrences of a word in a user input

Estimate: 30 minutes
Actual: 15 minutes
"""

text = input("Text: ")
words = text.split(" ")
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_length = max(len(word) for word in word_to_count.keys())
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count}")
