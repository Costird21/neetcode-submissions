def remove_fourth_character(word: str) -> str:
    before_forth = word[:3]
    after_forth = word[4:]

    return before_forth + after_forth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
