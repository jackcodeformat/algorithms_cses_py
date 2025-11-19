"""Algorithms CSES Repitition Algorithm"""

def repetitions(letter, string):
    """Algorithm to count number of times a letter repeats itself in a string"""
    max_char = 0
    count = 0

    for char in string: # loop through the string
        if count > max_char:
            max_char = count
        if char == letter:
            count += 1
        elif char != letter:
            count = 0
    return max_char

print(repetitions("d", "aaaddddddddadsaaaddddaassda"))
