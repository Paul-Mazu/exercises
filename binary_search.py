from random import randint
def find_number(number, list):
    left = 0
    right = len(a_list)

    while left < right:
        index = (left + right) // 2

        if a_list[index] == number:
            return index
        elif a_list[index] < number:
            left = index+1
        else:
            right = index



a_list = [*range(100)]
number = randint(0, 100)

print(find_number(number, a_list))
