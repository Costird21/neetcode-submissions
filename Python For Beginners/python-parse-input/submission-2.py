from typing import List

def read_integers() -> List[int]:
    string_input = input()
    string_input = string_input.split(",")
    return string_input

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
