# First arrays to tey the solution
arr1 = [1,2,3,4,5,6,7]
arr2 = [-1,-100,3,99]

def rotate(nums, k):
    nums_length = len(nums)

    # doesnt matter what is k, the array will not change
    if nums_length == 1:
        return 
    # k is the the same size of the array, the array will stay the same
    if nums_length == k:
        return
    
    ind = 0
    while ind < k:
        # last number in the array
        last_number = nums[nums_length - 1]
        # index to run over the array
        ind2 = nums_length
        while ind2 > 0:
            nums[ind2 - 1] = nums[ind2 - 2]
            # decrese ind2 by 1
            ind2 -= 1
        # replace the first place with the number of the last place
        nums[0] = last_number
        # increse i
        ind += 1

rotate(arr1, 3)
rotate(arr2, 2)

print(arr1)
print(arr2)