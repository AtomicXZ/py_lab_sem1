string = "An apple is called an apple because it is\
 an apple."

if "a" in string:
    print(f"Using the function obj.replace(): {string.replace('a', 'b')}\n")
    
    for i in range(len(string)):
        if string[i] == 'a':
            string = string[:i] + 'b' + string[i+1:]
    print(f"Using a for loop: {string}")

else:
    print("No \"a\" in the string.")