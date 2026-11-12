def add_two_numbers() -> int:
    input_string = input().split(",")

    result = 0
    for n in input_string:
        result += int(n)
    
    return result



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
