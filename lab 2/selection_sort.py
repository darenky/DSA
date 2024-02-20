import random
import timeit

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    start_time = timeit.default_timer()

    n = len(arr)

    for i in range(n-1):
        cur_min = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[cur_min]:
                cur_min = j

        if i != cur_min:
            arr[i], arr[cur_min] = arr[cur_min], arr[i]
            swaps += 1

    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    return comparisons, swaps,  execution_time


if __name__ == '__main__':
    tests = [
        random.choices(range(1, 1001), k=100),
        random.choices(range(1, 1001), k=1000) #,
        #random.choices(range(1, 1001), k=10000)
    ]

    for elements in tests: 
        comparisons, swaps, execution_time = selection_sort(elements.copy())
        selection_sort(elements)
        print(elements )
        print("Number of comparisons::", comparisons)
        print("Number of swaps:", swaps)
        print("Execution time:",  execution_time, "seconds")