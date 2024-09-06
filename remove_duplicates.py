
# Solution 1: Brute force Solution , 
# Time-Complexity : O(N)
# Space-Complexity : O(N)

# def Remove_duplicate(nums):
#     ans=[]
#     ans.append(nums[0])

#     n=len(nums)
#     print(f"length of array: {len(nums)}\n")
#     for i in range( 1,n ):
#         if nums[i]!=nums[i-1] :
#             ans.append(nums[i])
        
#     return ans 

# nums=[1,1,1,2,2,3,3,4,5,6,6,7,7,8,8,9,9,10,10]

# print(Remove_duplicate(nums))


# Solution 2: using built in functions set 
# Time - Complexity - O(N)
# Space Complexity - O(N)


# def Remove_duplicate(nums):
#     ans=list(set(nums))
#     # ans.sort()
#     return ans 


# nums=[1,1,1,2,2,3,3,4,5,6,6,7,7,8,8,9,9,10,10]

# print(Remove_duplicate(nums))

# Solution 3: In-place Optimized Solution
# Time-Complexity : O(N)
# Space-Complexity : O(1)


def Remove_duplicate(nums):
    i=0

    for j in range(1,len(nums)):
        if (nums[i] != nums[j]):
            nums[i+1]=nums[j]
            i+=1

    return i+1


nums=[1,1,1,2,2,3,3,4,5,6,6,7,7,8,8,9,9,10,10]

index=Remove_duplicate(nums)
print(nums)
print(nums[:index])


# Another Solution 

# def Remove_duplicate(nums):
#     n=len(nums)
#     unique_nums=[0]*n 
#     unique_nums[0]=nums[0]
#     current_index=1 

#     for i in range(1,len(nums)):

#         if nums[i-1]!= nums[i]:
#             unique_nums[current_index]=nums[i]
#             current_index+=1
        
#     return unique_nums



# nums=[1,1,1,2,2,3,3,4,5,6,6,7,7,8,8,9,9,10,10]

# # index=Remove_duplicate(nums)
# print(Remove_duplicate(nums))