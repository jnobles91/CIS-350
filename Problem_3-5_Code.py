from time import time
import random
#recursive method
def recursive_sort(array, k):
    return _recursive_sort(array, k , 0 , len(array) - 1)
    #the recursive solution needs an argument for a left and right pointer, so to make things cleaner for the user
    #we can use a helper function that only takes arguments for the array and integer k

def _recursive_sort(array, k , l , r):
    if l > r:
        return array
        #base case, returns the sorted array when the left and right pointers cross
    if array[l] <= k:
        #the item is on the correct side already, so we just need to move the left pointer forward
        return _recursive_sort(array, k, l + 1, r)
    else:
        #item is in the wrong place, switch it with the item at the right pointer and move the right pointer
        #since we know that the item at the right pointer is in the correct place
        array[l],array[r] = array[r],array[l]
        return _recursive_sort(array, k, l, r - 1)


#iterative method
def iterative_sort(array,k):
    l = 0
    r = len(array) - 1
    while l < r:
        #we're basically going to do the same thing as the recursive method, its just going to be wrapped in a while loop
        #instead of using recursion
        if array[l] <= k:
            l += 1
        #item is on the correct side, just move the left pointer forward
        else:
            #item is on the wrong side, flip it and move the right pointer down
            array[l], array[r] = array[r],array[l]
            r -= 1
    return array
    #return the sorted array when we exit the loop

#initialize arrays
random.seed(10)
array_10 = []
for i in range(10):
    array_10.append(random.randint(0,100))
array_100 = []
for i in range(100):
    array_100.append(random.randint(0,100))
array_500 = []
for i in range(500):
    array_500.append(random.randint(0,100))
#initialize k
k = 50

#run functions

start_time = time()
output_array = recursive_sort(array_10,k)
end_time = time()
print(output_array)
recursive_10_time = end_time - start_time

start_time = time()
recursive_sort(array_100,k)
end_time = time()
recursive_100_time = end_time - start_time

start_time = time()
recursive_sort(array_500,k)
end_time = time()
recursive_500_time = end_time - start_time

start_time = time()
output_array = iterative_sort(array_10,k)
end_time = time()
print(output_array)
iterative_10_time = end_time - start_time

start_time = time()
iterative_sort(array_100,k)
end_time = time()
iterative_100_time = end_time - start_time

start_time = time()
iterative_sort(array_500,k)
end_time = time()
iterative_500_time = end_time - start_time

print("recursive times:")
print(f"recursive 10: {recursive_10_time} recursive 100: {recursive_100_time}, recursive 500: {recursive_500_time}")
print('iterative times')
print(f'iterative 10: {iterative_10_time} iterative 100: {iterative_100_time} iterative 500: {iterative_500_time}')




    
