triangle_nums = [int(.5*i*(i+1)) for i in range(1, 21)]


with open('data/p042_words.txt') as f:
    words = f.read().replace('"', '').split(',')

count = 0
for word in words:
    total = 0
    for l in word:
        total += ord(l) - 64

    if total in triangle_nums:
        count += 1

print(count)
