"""Algorithms CSES Missing Numbers Algorithm"""

def missing_number(numbers):
    """Runs the missing number algorithm from CSES Problem Set 
    This is a try of this problem by codeformat"""
    for i in range(len(numbers) - 1):
        for num in range(len(numbers) - i - 1):
            if numbers[num] > numbers[num + 1]:
                numbers[num], numbers[num + 1] = numbers[num + 1], numbers[num]
    print(numbers)
    for x in range(len(numbers) - 1):
        if numbers[x + 1] != numbers[x] + 1:
            return numbers[x] + 1

number_list_inclusive = [5,1,3,4,2,6,8,10,9]
print(number_list_inclusive)
missing_number = missing_number(number_list_inclusive)

print(missing_number)
