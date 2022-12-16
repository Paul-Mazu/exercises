# slicing but not changin in place
def quicksort(lst):
    if len(lst) > 1:
        pivot = lst[0]
        left = [i for i in lst[1:] if i <= pivot]
        right = [i for i in lst[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    return lst

# quicksort with both pointers traveling left to right, changes in place
def quicksort_lomuto_partition(lst, left = 0, right = -1):
    if right == -1: right = len(lst) -1

    if left < right:
        pivot = partition(lst, left, right)
        quicksort_lomuto_partition(lst, left, pivot-1)
        quicksort_lomuto_partition(lst, pivot +1, right)

def partition(lst, left, right):
    pivot = lst[right]
    i = left - 1

    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i + 1


# quick sort with pointers in oposit direction
def quicksort1(lst, left=0, right=-1):
    if right == -1: right = len(lst) -1
    if left < right:
        partition_pos = partition1(lst, left, right)
        quicksort1(lst, left, partition_pos -1)
        quicksort1(lst, partition_pos +1, right)
    return lst


def partition1(lst, left, right):
    pivot = lst[right]
    i = left
    j = right -1

    while i < j:
        while i < right and lst[i] < pivot:
            i += 1
        while j > left and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    if lst[i] > pivot:
        lst[i], lst[right] = lst[right], lst[i]
    return i


a = [3, 7, 2, 8, 4, 6, 9, 15, 1, 4, 5]

if __name__ == "__main__":
    # print(quicksort(a))
    # print(quicksort_lomuto_partition(a))
    # print(quicksort1(a))
    pass