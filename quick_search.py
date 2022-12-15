def quicksort(lst):
    if len(lst) > 1:
        pivot = lst[0]
        left = [i for i in lst[1:] if i <= pivot]
        right = [i for i in lst[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    return lst

def quicksort_lomuto_partition(lst, left = 0, right = -1):
    if right == -1: right = len(lst) -1

    if left < right:
        pivot = partition(lst, left, right)
        quicksort_lomuto_partition(lst, left, pivot-1)
        quicksort_lomuto_partition(lst, pivot +1, right)
    return lst
def partition(lst, left, right):
    pivot = lst[right]
    i = left - 1

    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i + 1



a = [3, 7, 2, 8, 4, 6, 9, 15, 1, 4]

if __name__ == "__main__":
    #print(quicksort(a))
    print(quicksort_lomuto_partition(a))