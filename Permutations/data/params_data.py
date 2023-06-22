# char_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&/(?:)_-.\[]{}*+|=¡"
# char_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJ{}*+|=¡"
# char_value = "abc"
char_value = []
min_value = 2
max_value = 3


def get_string():
    if not isinstance(char_value, str):
        return f"The value: {char_value} is not a valid String"
    return char_value

def get_min_value():
    if not isinstance(min_value, int):
        return f"The value: {min_value} is not a valid Number"
    return min_value

def get_max_value():
    if not isinstance(max_value, int):
        return f"The value: {max_value} is not a valid Number"
    return max_value