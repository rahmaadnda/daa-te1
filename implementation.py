import time
import math
import random
import tracemalloc

"""
Implementasi Algoritma 1, yaitu Clustered Binary Insertion Sort. Terdiri dari 1 main function dan 2 helper function.
Referensi: 
Shubham Goel and Ravinder Kumar. Brownian Motus and Clustered Binary Insertion Sort methods: An efficient progress over traditional methods. Future Generation Computer Systems, 86:266–280, 2018.
"""
def cbis(arr):
    position = 0
    for i in range(1, len(arr)):
        current = i
        key = arr[current]
        # right movement decision
        if key >= arr[position]:
            place = binary_loc_finder(arr, position+1, current-1, key)
        # left movement decision
        else:
            place = binary_loc_finder(arr, 0, position-1, key)
        position = place
        arr = place_inserter(arr, place, current)
        i+=1

def binary_loc_finder(arr, start, end, key):
    if start == end:
        if arr[start] > key:
            loc = start
        else:
            loc = start + 1
        return loc
    if start > end:
        loc = start
        return loc
    else:
        middle = math.floor((start+end)/2)
        if arr[middle] < key:
            return binary_loc_finder(arr, middle+1, end, key)
        elif arr[middle] > key:
            return binary_loc_finder(arr, start, middle-1, key)
        else:
            return middle
        
def place_inserter(arr, start, end):
    temp = arr[end]
    for k in range(end, start, -1):
        arr[k] = arr[k-1]
    arr[start] = temp
    return arr

"""
Implementasi Algoritma 2, yaitu Randomized Quick Sort. 
Terdiri dari 1 main function yang akan memanggil dirinya secara rekursif dan 2 helper function yang akan membuat partisi secara acak.
Referensi: Slide perkuliahan.
"""
def randomized_quicksort(A, left, right):
    if left < right:
        q = randomized_partition(A, left, right)
        randomized_quicksort(A, left, q-1)
        randomized_quicksort(A, q+1, right)
        
def randomized_partition(A, left, right):
    i = random.randint(left, right)
    temp = A[i]
    A[i] = A[right]
    A[right] = temp
    return partition(A, left, right)    
        
def partition(A, left, right):
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[right]
    A[right] = temp
    return i + 1

"""
Pengujian untuk setiap algoritma dengan setiap variasi dataset.
Untuk setiap pengujian, dilakukan perhitungan waktu eksekusi dan penggunaan memori
Referensi:
https://docs.python.org/3/library/time.html 
https://docs.python.org/3/library/tracemalloc.html 
"""
def measure_algorithm_performance(sorting_function, dataset):
    tracemalloc.start()
    start_time = time.time()
    if sorting_function == cbis:
        sorting_function(dataset)
    else:
        sorting_function(dataset, 0, len(dataset)-1)
    end_time = time.time()
    memory_usage = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()    
    execution_time = (end_time - start_time) * 1000
    return execution_time, memory_usage

# inisialisasi
dataset_sizes = [200, 2000, 20000]
dataset_status = ["sorted", "random", "reversed"]
algorithms = {
    "Clustered Binary Insertion Sort": cbis,
    "Randomized Quick Sort": randomized_quicksort
}

# main program yang akan membaca dataset dan memanggil setiap fungsi
for size in dataset_sizes:
    for status in dataset_status:
        with open(f"dataset/{status}_{size}.txt", "r") as f:
            dataset = f.read().split("\n")
            dataset = [int(data) for data in dataset if data.isnumeric()]
            print("="*50)
            print(f"Dataset: {size} elemen {status}")
            for algorithm_name, sorting_function in algorithms.items():
                execution_time, memory_usage = measure_algorithm_performance(sorting_function, dataset.copy())
                print(f"{algorithm_name}:")
                print(f"Penggunaan Memori: {memory_usage} B")
                print(f"Waktu Eksekusi: {execution_time:.2f} ms")
                print()