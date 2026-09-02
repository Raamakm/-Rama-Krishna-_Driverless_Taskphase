
n=int(input("Enter number of integers: "))

hash_table=[[], [], [], [], [], [], [], [], [], []]

for i in range(n):
    num=int(input("Enter number: "))
    index=num%10
    sublist=hash_table[index]

    left=0
    right=len(sublist)

    while left<right:
        middle=(left + right)/2

        if sublist[middle]<num:
            left=middle+1
        else:
            right=middle

    sublist.insert(left, num)

for i in range(10):
    print(i, ":", hash_table[i])

