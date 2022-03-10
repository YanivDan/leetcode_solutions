arr1 = [0,0,1,1,1,2,2,3,3,4]
arr2 = [1,2,2]
arr3 = [1,1,2]
arr4 = [1,1,2,2]
arr5 = [1,2,2,2]

def removeDuplicates(nums):
    if len(nums) == 1:
        return 1

    # K - numsber of duplicate's
    K = 0

    # nums last place
    last = len(nums) - 1

    # Go over nums 
    for i in range(0, last):
        # Compare value's of current and prev
        if nums[last - i] == nums[last - (i + 1)]:
            # if the value is the same replace the value with "_"
            nums[last - i] = "_"
            K += 1

    # print(nums)

    # indexer
    cur = -1
    # To distiguish the first last place "_" were seen
    flag = False
    # index to run in while loop
    i = 0
    # reorder the numsbers
    while i < len(nums) - 1:
        # increase the index
        i += 1
        
        #check if "_"
        if nums[i] == "_" and flag == False:
            # change the indexer to first place "_" occured 
            cur = i
            # update the flag value
            flag = True
            continue

        # check if nums[i] is an integer and i != len(nums) - 2
        if nums[i] != "_" and cur != -1:
            # get the numsber backwords  
            nums[cur] = nums[i]
            # replace index integer with "_"
            nums[i] = "_"
            # update i to start from last place "_" seen
            i = cur
            # update the flag value
            flag = False
    return len(nums) - K    

removeDuplicates(arr1)
print("arr 1 is ", arr1)

removeDuplicates(arr2)
print("arr 2 is ", arr2)

removeDuplicates(arr3)
print("arr 4 is ", arr3)

removeDuplicates(arr4)
print("arr 4 is ", arr4)

removeDuplicates(arr5)
print("arr 5 is ", arr5)