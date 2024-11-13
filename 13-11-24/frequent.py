string = "sample string"

count = {}
for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

frequent= max(count, key=count.get)

print("The most frequent character is:", frequent)
