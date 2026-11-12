from typing import List

def read_integers() -> List[int]:
    string_input = input()
    string_input = string_input.split(",")
    
    result = []

    for n in string_input:
        result.append(int(n))

    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
