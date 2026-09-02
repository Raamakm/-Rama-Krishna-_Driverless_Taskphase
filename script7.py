n = int(input("Enter number of strings: "))

strings = []

for i in range(n):
    strings.append(input("Enter string: "))

count = {}

for string in strings:
    for char in string.lower():
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

print(count)
