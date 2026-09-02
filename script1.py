for i in range(n1):
    item=input(f"enter item{i+1}:")
    list.append(item)

class selectionsort:
    def __init__(self, arr):
        self.arr = arr
        n=len(self.arr)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if arr[i] < arr[j]:
                    min_index=j
                    arr[i], arr[min_index]=arr[min_index], arr[i]

selectionsort(list)
print(list)


def binary_search(arr, target):
    low=0
    high=len(arr) - 1

    while low<=high:
        mid=(low + high) // 2

        if arr[mid]==target:
            return mid

        elif arr[mid]<target:
            low=mid + 1

        else:
            high=mid - 1

    return -1

result = binary_search(numbers, target_value)
if result!=-1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")