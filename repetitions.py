"""Algorithms CSES Repitition Algorithm"""

def repetitions(string):
    """Algorithm to count largest letter repetition in a string"""
    max_char = 0
    count = 0
    letter = string[0]

    for char in string: # loop through the string
        if count > max_char:
            max_char = count

        if char == letter:
            count += 1

        elif char != letter:
            count = 1
            letter = char

    return max_char

print(repetitions("GGGGGAAAAAABBBSSSAAA"))
