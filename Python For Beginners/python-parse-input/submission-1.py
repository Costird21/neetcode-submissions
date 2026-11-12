from typing import List

def read_integers() -> List[int]:
    string_input = input()

    return string_input.split(",")

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
