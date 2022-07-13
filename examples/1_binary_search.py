import time


def time_track(func):
    def surrogate(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'Function operation time: {delta_time} sec')
        return result
    return surrogate


# O(n)
@time_track
def linear_search(list_item, item):
    count_iterations = 0
    for i, guess in enumerate(list_item, 0):
        count_iterations += 1
        if guess == item:
            print(f'Linear search iterations: {count_iterations}')
            return i
    return None


# O(log(n))
@time_track
def binary_search(list_item, item):
    low = 0
    high = len(list_item) - 1

    count_iterations = 0
    while low <= high:
        count_iterations += 1
        mid = (low + high) // 2
        guess = list_item[mid]

        if guess == item:
            print(f'Binary search iterations: {count_iterations}')
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = range(1, 10 ** 10)
index_x = binary_search(my_list, 10 ** 8)
print('Binary search: {}'.format(index_x))

index_y = linear_search(my_list, 10 ** 8)
print('Linear search: {}'.format(index_y))

