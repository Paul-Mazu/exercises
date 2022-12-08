import time
import random
import matplotlib.pyplot as plt


def timer_factor(rounds=3):
    def timer(func):
        def inner(*args, **kwargs):
            results = []
            for i in range(rounds):
                start = time.time()
                func(*args, **kwargs)
                elapsed_time = time.time() - start
                results.append(elapsed_time)
            return sum(results) / len(results)
        return inner
    return timer


# set
@timer_factor(rounds=10)
def union_set(needles, haystack):
    return len(needles & haystack)


#list
@timer_factor(rounds=3)
def union_list(needles, haystack):
    found = 0
    for needle in needles:
        if needle in haystack:
            found +=1
    return found

### here starts exercise

def time_different_sizes_in_set(sizes:list) -> list:
    """ 
    takes list of sizes and returns a list of times
    produces needles from range
    iterates over sizes using each size to produce new range of haystack each iteration
    calling the function union_set() which returns average time and
     appending the times to returned lst
    """
    needles = list(range(1000))
    random.shuffle(needles)
    lst = []
    for size in sizes:
        haystack = [*range(500,500+size), *needles[:500]]
        random.shuffle(haystack)
        lst.append(union_set(set(needles), set(haystack)))
    return lst


def time_different_sizes_in_list(sizes):
    needles = list(range(1000))
    random.shuffle(needles)
    lst = []
    for size in sizes:
        haystack = [*range(1000,1500+size), *needles[:500]]
        random.shuffle(haystack)
        lst.append(union_list(needles, haystack))
    return lst


sizes_list = [0, 10_000, 100_000, 1_000_000] # increses size of haystack
times_list_for_set = time_different_sizes_in_set(sizes_list)
times_list_for_list = time_different_sizes_in_list(sizes_list)


plt.plot(sizes_list, times_list_for_set, label='set')
plt.plot(sizes_list, times_list_for_list, label='list')
plt.legend()
plt.title('O notation')
plt.xlabel('size')
plt.ylabel('time')
plt.show()


""" 
Exercise
loop over the following list: [0, 1000, 10000, 1000000]
increase the original size of the haystack by 1_000, 10_000, 1_000_000 for each iteration step
in each iteration call union_set(set(needles), set(haystack)) and union_list(needles, haystack)
store the returned time in two seperated lists (time_list and time_set)
plot your results ( with matplotlib, where the size of the haystack is on th x axis and the time is on the y-axis 
"""