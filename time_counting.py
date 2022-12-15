import time
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

x = [i for i in range(100)]
y = [i for i in range(100)]


plt.plot(x, y, label='my label')
plt.legend()
plt.title('chart title')
plt.xlabel('size')
plt.ylabel('time')
plt.show()