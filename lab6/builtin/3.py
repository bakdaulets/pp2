string = input()
def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
x = check_palindrome(string)
print(x)