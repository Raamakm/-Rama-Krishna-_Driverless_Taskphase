list=[]
n1=int(input("Enter the number of elements in set:"))
for i in range(n1):
    item=input(f"enter item{i+1}:")
    list.append(item)

class selectionsort:
    def __init__(self, arr):
        self.arr=arr
        n=len(self.arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if arr[i]<arr[j]:
                    min_index = j
                    arr[i], arr[min_index]=arr[min_index], arr[i]

selectionsort(list)
print(list)