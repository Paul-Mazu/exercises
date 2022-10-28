def bubble_sort(list):

    #jumps_counter = 0
    changes = 1
    reduction = 1

    while changes > 0:  # closes if during iteration no changes have been done
        changes = 0
        for i in range(len(a_list) - reduction):
            # jumps_counter += (len(a_list) - reduction) # checks how many iteration has benn done
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                changes += 1
        reduction += 1  # reduces iteration in for loop every time by 1, no need to go every time to end of list
    return list

a_list = [5, 4, 1, 2, 9, 6, 7, 3, 8, 0]

print(bubble_sort(a_list))
