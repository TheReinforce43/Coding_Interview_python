def Maximum_Subarray(nums):

    # ans,temp=0,0
    ans=float('-inf')
    temp=0
    # temp=0
    # for i in range(len(nums)):
    for value in nums:

        temp=max(value , value + temp)
        ans=max(temp,ans)

        # print(temp,ans)

        # if temp > ans :
        #     ans=temp 
        # else:
        #     temp=0
        # i+=1
        
    
    return ans 



nums=[-1,-2,1,2,3,-5,4]
print(f"final output:{Maximum_Subarray(nums)}")



