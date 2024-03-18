from example_list import ExampleUtils

list_ = ExampleUtils.create_list(10000)

@ExampleUtils.print_runtime
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


bubble_sort(list_)