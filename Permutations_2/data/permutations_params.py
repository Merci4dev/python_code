# chars_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&/(?:)_-.\[]{}*+|=¡"
# chars_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJ*+|=¡" 
# chars_value = []

chars_value = "xyz"
min_value = 3
max_value = 3
chars_value = "abcdefghi123"
# min_value = 6
# max_value = 10


# This class handles the data logic validation we will use for the permutations 
class DataPermutationValues:
    def __init__(self, input_chars_value, input_min_value=None, input_max_value=None):
        self.set_chars_values(input_chars_value)
        self.set_min_value(input_min_value)
        self.set_max_value(input_max_value)

    # Method to handle the string logic over which we make the permutations
    def set_chars_values(self, input_chars_value):
        if isinstance(input_chars_value, str) and input_chars_value != "":
            self.chars_value = input_chars_value
        else:
            raise ValueError(f"The value: {input_chars_value} is not a valid string.")

    # Method to handle the min value logic over which we make the permutations
    def set_min_value(self, input_min_value):
        if input_min_value is not None and (not isinstance(input_min_value, int) or input_min_value <= 0):
            self.min_value_error = f"The value: {input_min_value} is not a valid integer number or is less than or equal to 0."
            raise ValueError(self.min_value_error)
        else:
            self.min_value_error = None
            self.min_value = input_min_value

    # Method to handle the max value logic over which we make the permutations
    def set_max_value(self, input_max_value):
        if input_max_value is not None and (not isinstance(input_max_value, int) or input_max_value <= 0):
            self.max_value_error = f"The value: {input_max_value} is not a valid integer number or is less than or equal to 0."
            raise ValueError(self.max_value_error)
        else:
            self.max_value_error = None
            self.max_value = input_max_value

    # Methods to return the result from set_chars_values(), set_min_value, and set_max_value
    def get_chars_value(self):
        return self.chars_value

    def get_min_value(self):
        return self.min_value
    
    def get_max_value(self):
        return self.max_value

    def __str__(self):
        if self.min_value_error is not None:
            return self.min_value_error
        elif self.max_value_error is not None:
            return self.max_value_error
        else:
            return f"Chars: {self.get_chars_value()}, Min: {self.get_min_value()}, Max: {self.get_max_value()}"


#=========================================================
# permutation_data = DataPermutationValues(chars_value)

# try:
    
#     # Chars
#     permutation_value = permutation_data.get_chars_value()
#     # permutation_data.set_chars_value("1234abcd")
#     print(permutation_data.get_chars_value())
    
#     # Min
#     permutation_data.set_min_value(min_value)
#     min_value = permutation_data.get_min_value()
#     print(min_value)
    
#     # Max
#     permutation_data.set_max_value(max_value)
#     max_value = permutation_data.get_max_value()
#     print(max_value)
# except ValueError as e:
#     print(f"An error occurred: {e}")

