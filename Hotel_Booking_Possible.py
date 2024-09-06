
def hotel_booking(arrive,depart,k):

    arrive.sort()
    depart.sort()
    n=len(arrive)
    i,j=0,0
    count=0

    while i<n and j<n:

        if arrive[i] < depart[j]:
            count+=1
            i+=1
    
        elif  depart[j] <arrive[i]:
            count-=1
            j+=1
        else :
            i+=1
            j+=1

        if count > k:
            return False
    #     print(i,j,count)

    # print("total count: ",count)
    
    return True


if __name__ =='__main__':
    arrive = [1,3,5]
    depart = [2,6,8]
    k = 1
    print(hotel_booking(arrive, depart, k)) # True