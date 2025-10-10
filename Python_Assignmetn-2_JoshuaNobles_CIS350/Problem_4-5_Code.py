from time import time
import random
#recursive solution
#recursive solution
def recursive_sum(array, k):
    return _recursive_sum(array,k,0,len(array)-1)

def _recursive_sum(array, k, l,r):
    if l > r:
        return False
    else:
        if array[l] + array[r] == k:
            return array[l], array[r]
        elif (array[l] + array[r]) < k:
            return _recursive_sum(array,k,l + 1,r)
        else:
            return _recursive_sum(array,k,l,r -1)
#iterative solution

def iterative_sum(array, k):
    #initialize left and right pointers
    l = 0
    r = len(array) - 1
    while l < r:
    #wrap everything in a while loop instead of using recursion
        if array[l] + array[r] == k:
        #if the items at both pointers add to the target, return
            return array[l], array[r]
        elif (array[l] + array[r]) < k:
        #if they are less than the target, increment the left pointer to increase the sum
            l += 1
        else:
        #else increase the sum
            r -= 1
    return False
    #return false if we get to the end of the loop without finding a sum



#test where we know solution
array = [1,2,3,4]
k =  6
print(iterative_sum(array,k))
print(recursive_sum(array,k))
#should be 2,4 for both
print(iterative_sum(array, 29))
print(recursive_sum(array,29))
#should be false for both


#test runtime
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

k = random.randint(0,200)



start_time = time()
recursive_sum(array_10,k)
end_time = time()
recursive_10_time = end_time - start_time

start_time = time()
recursive_sum(array_100,k)
end_time = time()
recursive_100_time = end_time - start_time

start_time = time()
recursive_sum(array_500,k)
end_time = time()
recursive_500_time = end_time - start_time

start_time = time()
iterative_sum(array_10,k)
end_time = time()
iterative_10_time = end_time - start_time

start_time = time()
iterative_sum(array_100,k)
end_time = time()
iterative_100_time = end_time - start_time

start_time = time()
iterative_sum(array_500,k)
end_time = time()
iterative_500_time = end_time - start_time

print("recursive times:")
print(f"recursive 10: {recursive_10_time} recursive 100: {recursive_100_time}, recursive 500: {recursive_500_time}")
print('iterative times')
print(f'iterative 10: {iterative_10_time} iterative 100: {iterative_100_time} iterative 500: {iterative_500_time}')


