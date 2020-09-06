def Palindrome(str):
    left_pos = 0 #from the left position
    right_pos = len(str) - 1 #from the right position

    while right_pos >= left_pos:
        if not str[left_pos] == str[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(Palindrome('madam'))

