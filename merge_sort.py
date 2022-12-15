def merge_sort(lst):
    if len(lst) > 1:
        middle = len(lst)//2
        left_lst = lst[:middle]
        right_lst = lst[middle:]

        # recursion
        merge_sort(left_lst)
        merge_sort(right_lst)

        # merge
        i = 0 # left lst index
        j = 0 # right lst index
        k = 0 # merged lst index
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1
    return lst


arr = [2,3,5,1,7,4,4,4,2,6,0]
print(merge_sort(arr))