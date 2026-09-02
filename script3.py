n=int(input("Enter number of integers: "))

hash_table=[[], [], [], [], [], [], [], [], [], []]

for i in range(n):
    num=int(input("Enter number: "))
    index=num%10
    hash_table[index].append(num)

for i in range(10):
    print(i, ":", hash_table[i])
