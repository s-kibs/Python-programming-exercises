# Write a program which takes 2 digits, X,Y as input and generates a 
# 2-dimensional array. The element value in the i-th row and j-th column of the
# array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

strInp= input("Enter 2 numbers: ")

rowCol = [int(n) for n in strInp.split(',')]
x = rowCol[0]
y = rowCol[1]
arr2d=[[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        arr2d[i][j]= i*j
print(arr2d)

# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# arr = [[0 for col in range(colNum)] for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         arr[row][col]= row*col

# print (arr)