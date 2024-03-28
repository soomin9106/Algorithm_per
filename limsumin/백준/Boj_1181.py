import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())

words = []

for _ in range(n):
    words.append(input())

words = list(set(words))



words = sorted(words, key = lambda x: (len(x), x))

for w in words:
    print(w)
