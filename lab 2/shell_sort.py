import random
import timeit

def shell_sort(arr):
    comparisons = 0
    swaps = 0
    start_time = timeit.default_timer()

    n = len(arr)
    gap = n // 2 

    while gap > 0:
        for i in range(gap, n):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap] 
                j -= gap
                comparisons += 1  

            arr[j] = anchor
            swaps += 1 
        gap = gap //2

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

