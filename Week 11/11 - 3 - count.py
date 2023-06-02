def anagram(s, t):
    if len(s) != len(t):
        return False
    for ch in set(s):
        if s.count(ch) != t.count(ch):
            return False
    return True

string_1 = "abdc"
string_2 = "abcc"

print("Anagram" if anagram(string_1, string_2) else "Not an anagram")