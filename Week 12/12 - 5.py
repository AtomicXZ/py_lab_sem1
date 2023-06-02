def add_prefix(string, prefix):
    lines = string.split("\n")
    prefixed_lines = [prefix + line for line in lines]
    prefixed_string = "\n".join(prefixed_lines)
    return prefixed_string

original_string = """line 1
line 2
line 3"""
prefix = "prefix: "
print(add_prefix(original_string, prefix))