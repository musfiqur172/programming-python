str = "Hello Test! 123 123, good."
up_word = ""
low_word = ""
numbers = ""
others = ""

for c in str:
    if ord(c) in range(65, 91):
        up_word += c
    elif ord(c) in range(97, 123):
        low_word += c
    elif ord(c) in range(48, 58):
        numbers += c
    else:
        others += c


print(up_word)
print(low_word)
print(numbers)
print(others)
