from string import ascii_lowercase

def newStr(arr):
    char = list(ascii_lowercase)
    data =list(arr)
    vowels = "aeiou"
    new = []
    cleaned  = ""
    for i in data:
        if i == " ":
            new.append(i)
        elif i not in vowels:
            if char[char.index(i)+1] in vowels:
                new.append(char[char.index(i)+2])
            else:
                new.append(char[char.index(i)+1])
        else:
            new.append(i)

    for i in new:
        cleaned += letter
        return cleaned

print(newStr("hello world"))