
def matrix_multiply(A, B):
    rows_A=len(A)
    cols_A=len(A[0])

    rows_B=len(B)
    cols_B=len(B[0])

    if cols_A!=rows_B:
        print("Error: Matrix multiplication is not possible.")
        return

    result=[]

    for i in range(rows_A):
        row=[]

        for j in range(cols_B):
            total=0

            for k in range(cols_A):
                total+=A[i][k]*B[k][j]

            row.append(total)

        result.append(row)

    print("Result:")
    for row in result:
        print(row)

A=[
   [1,2]
]
B=[
     [2],
     [2]]

Answer=matrix_multiply(A,B)
print(Answer)


