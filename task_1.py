import random
import timeit
import sys

# Increase recursion limit for merge sort
sys.setrecursionlimit(100_000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k]= R[j]
                j += 1
            k +=1

        while i < len(L):
            arr[k]=L[i]
            i +=1
            k +=1

        while j < len(R):
            arr[k]=R[j]
            j +=1
            k +=1

def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))

def main():
    sizes = [1000, 5000, 10_000, 50_000, 100_000]
    data_types = ['random', 'sorted', 'reversed']

    for size in sizes:
        print(f"\n\nArray Size: {size}")
        for data_type in data_types:
            print(f"\nData Type: {data_type}")
            data = generate_data(size, data_type)

            data_insertion = data.copy()
            data_merge = data.copy()
            data_timsort = data.copy()

            time_insertion = timeit.timeit(lambda: insertion_sort(data_insertion), number=1)
            time_merge = timeit.timeit(lambda: merge_sort(data_merge), number=1)
            time_timsort = timeit.timeit(lambda: sorted(data_timsort), number=1)

            print(f"Insertion Sort: {time_insertion:.6f} seconds")
            print(f"Merge Sort: {time_merge:.6f} seconds")
            print(f"Timsort: {time_timsort:.6f} seconds")

if __name__ == "__main__":
    main()
