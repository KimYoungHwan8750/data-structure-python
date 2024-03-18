from example_list import ExampleUtils

list_ = ExampleUtils.create_list(50)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, equals, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equals.append(i)
    return quick_sort(left) + equals + quick_sort(right)

print(quick_sort(list_))

