#Daily Coding Problem 1
numbers = [1, 7, 10, 3]
k = 17
"""
Given a list of numbers and a value k, find out whether any two numbers add up to k
"""
for i in range(len(numbers)):
    for j in range(len(numbers)):
        #Prevents numbers from being added to themselves (i.e. 1 + 1)
        if numbers[i] == numbers[j]:
            continue
        else:
            n = numbers[i]+numbers[j]
            #Testing statements for further understanding. Comment out before submitting.
            print("Run--> i: " + str(i))
            print("Run--> j: " + str(j))
            print("numbers[i]: " + str(numbers[i]))
            print("numbers[j]: " + str(numbers[j]))
            print("n: " + str(n))
            #End of Testing
            #Evaluation
            if numbers[i]+numbers[j] == k:
                print(True)
            else:
                print(False)
        print("-----------------------")