import random
import timeit

def shell_sort(arr):
    n = len(arr)
    h = 1
    swaps = 0
    comparisons = 0
    start_time = timeit.default_timer()

    while h < n // 2:
        h = 2 * h + 1   #Hibbard's increment 

    while h > 0:
        for i in range(h, n):
            anchor = arr[i]
            j = i

            comparisons += 1
            while j >= h and arr[j - h] > anchor:
                arr[j] = arr[j - h]
                j -= h
                swaps += 1

            arr[j] = anchor

        h //= 2

    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    return comparisons, swaps,  execution_time

if __name__ == '__main__':
    tests = [
        random.choices(range(1, 1001), k=100),
        random.choices(range(1, 1001), k=1000) 
        # random.choices(range(1, 1001), k=10000)
    ]

    for elements in tests: 
        comparisons, swaps, execution_time = shell_sort(elements.copy())
        shell_sort(elements)
        print(elements )
        print("Number of comparisons::", comparisons)
        print("Number of swaps:", swaps)
        print("Execution time:",  execution_time, "seconds")

