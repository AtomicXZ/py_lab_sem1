def anagram(string_1, string_2, ind=0):
    if len(string_1) == len(string_2):
        for i in set(string_1):
            if i not in string_2:
                return False
            string_2 = string_2.replace(i, "")
        if string_2:
            return False
        else:
            return True
    else:
        return False


string_1 = "abdc"
string_2 = "abcc"

print("Anagram" if anagram(string_1, string_2) else "Not an anagram")