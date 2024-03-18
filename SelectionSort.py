from example_list import ExampleUtils

list_ = ExampleUtils.create_list(1000)

@ExampleUtils.print_runtime
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

selection_sort(list_)