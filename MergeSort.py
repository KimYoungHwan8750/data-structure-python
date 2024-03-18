from example_list import ExampleUtils

list_ = ExampleUtils.create_list(50)
list2_ = list_.copy()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

# print(merge_sort(list_))

def merge(left, right):
    merge_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
    merge_arr += left[l:]
    merge_arr += right[r:]
    print("실행2")
    return merge_arr
def merge_sort2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort2(arr[:mid])
    right = merge_sort2(arr[mid:])
    print("실행")
    return merge(left, right)

print(merge_sort2(list2_))