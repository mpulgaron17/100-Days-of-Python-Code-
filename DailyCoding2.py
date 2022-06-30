"""
Given an array of integers, return a new array such that each element at index [i] of the
new array is the product of all the numbers in the original array except the one at i.
Example:
input [3,2,1]
output [2,3,6]
"""
numbers = [3, 2, 1]
result = []
product = 1
for i in range(len(numbers)):
    product = 1
    for j in range(len(numbers)):
        if i == j:
            continue
        else:
            product *= numbers[j]
        #Testing statements
        print("------------")
        print("Run i " + str(i))
        print("Run j " + str(j))
        print("product " + str(product))
        print("------------")
        #End of Testing Statements
    result.append(product)        
print(result)
