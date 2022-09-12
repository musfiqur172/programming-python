def is_palindrome(s):
    rev_str = ""
    for ch in s:
        rev_str = ch + rev_str

    if(s == rev_str):
        return True
    else:
        return False

str = input("Enter a word: ")

if (is_palindrome(str)):
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")
