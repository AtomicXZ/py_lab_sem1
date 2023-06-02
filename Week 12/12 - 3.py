string = "python"
string_to_insert = "3.0"
print(f"String: {string}\nString to insert: {string_to_insert}\nString after insertion: {string[:len(string)//2]+string_to_insert+string[len(string)//2:]}")