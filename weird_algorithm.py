def weird_algorithm():
    valid_number = False
    while valid_number is False:
        try:
            num = int(input("Input a positive number above 1: "))
            if num < 2 or num > pow(10,6) or ValueError:
                print("Input a valid number")
            else:
                valid_number = True
        except:
            print("Input a valid number")  
    print(num)
    while num != 1:
        if num % 2 == 0:
            num /= 2
            print(int(num))
        elif num != 0:
            num = (num * 3) + 1
            print(int(num))

print("weird algorithm")
weird_algorithm()