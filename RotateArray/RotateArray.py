
arr1 = [1,2,3,4,5,6,7]
arr2 = [-1,-100,3,99]

def rotate(nums, k):
    # doesnt matter what is k, the array will not change
    if len(nums) == 1:
        return 
    # k is the the same size of the array, the array will stay the same
    if len(nums) == k:
        return
    
    ind = 0
    runner = "_"
    while ind < k:
        


        # increse i
        ind += 1

rotate(arr1, 3)
rotate(arr2, 2)

print(arr1)
print(arr2)