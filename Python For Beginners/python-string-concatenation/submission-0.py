def concatenate(s1: str, s2: str) -> str:
    message = s1 + s2

    if len(message) > 10:
        print("Too long!")
    else:
        print(message)




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
