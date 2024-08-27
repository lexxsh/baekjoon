import sys
input = sys.stdin.readline
a, b = map(int, input().split())
word_dict = {}
for i in range(a):
    word = input().rstrip()
    if len(word) < b:
        continue
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
sorted_words = sorted(word_dict.items(), key=lambda i: (-i[1], -len(i[0]), i[0]))
for word, _ in sorted_words:
    print(word)