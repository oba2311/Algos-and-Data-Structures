import random
import time

start_time = time.time()

def KMergeSort(unsortedarray,k):
    #divide the len of unsorted into k subarrays
    ListofLists=[]
    n=len(unsortedarray)
    if n==1:
        return unsortedarray
    elif k==1: 
        raise ValueError ("Divide and conquer with 1 list is not exactly \"divide\" and conquer..")
    elif k>n:
        return KMergeSort(unsortedarray,n) #since this is unreasonable request, I return the closest one.
    elif k>n//2:
        k==n//2 #This is unreasonable request, so I return the closest which is k==n/2.
    elif k<1:
        return "Well, haha"
    if n%k==0:
        for i in range(k):
            ListofLists.append(unsortedarray[(n/k)*i:(n/k)*(i)+(n/k)]) #need to make it more robust.for all k
            #this line is the same as the one above: ListofLists.append(unsortedarray[(n/k)*i:(n/k)*(i+1)]) #need to make it more robust.for all k
    else:
        for i in range(k+k%n): #check with noam and Alechko for this line.
            ListofLists.append(unsortedarray[(n/k)*i:(n/k)*(i)+(n/k)]) #need to make it more robust.for all k
            #this line is the same as the one above: ListofLists.append(unsortedarray[(n/k)*i:(n/k)*(i+1)]) #need to make it more robust.for all k
    SortedListofLists=[]
    for j in ListofLists:
        SortedListofLists.append(mergesort(j,k))
    while len(ListofLists)>1:
        Left=ListofLists.pop(0)
        Right=ListofLists.pop(0)
        ListofLists.append(merge(Left,Right))     #pair up those unsorted arrays into pairs.
    return ListofLists

def mergesort(unsortedarray,k=2):
    #Use insertion sort once number of elements <=4: (for a version without insertion,
    # comment out this block)
    if len(unsortedarray)<=4:
        for i in range(1,len(unsortedarray)):
            currentvalue = unsortedarray[i]
            position = i
            while position>0 and unsortedarray[position-1]>currentvalue:
                unsortedarray[position]=unsortedarray[position-1]
                position = position-1
            unsortedarray[position]=currentvalue
        return unsortedarray
    else:
        # baseCase - blocks of one:
        if len(unsortedarray)==1:
            return unsortedarray
        # break it to pieces.
            # break it once, call the function again.
        mid=(len(unsortedarray)//k) #divide into 2, floor method
        Left=mergesort(unsortedarray[:mid]) 
        Right=mergesort(unsortedarray[mid:])
        return merge(Left,Right)

def mergesortNoInsertion(unsortedarray,k=2):
        # baseCase - blocks of one:
        if len(unsortedarray)==1:
            return unsortedarray
        # break it to pieces.
            # break it once, call the function again.
        mid=(len(unsortedarray)//k) #divide into 2, floor method
        Left=mergesort(unsortedarray[:mid]) 
        Right=mergesort(unsortedarray[mid:])
        return merge(Left,Right)


#this helper function sorts the blocks upwards.
def merge(Left,Right):
    NewSorted=[]
    # compares minimal elements of the "sorted" lists. 
    while len(Left)!=0 and len(Right)!=0:
        if Left[0]<=Right[0]:
            NewSorted.append(Left.pop(0))
        else:
            NewSorted.append(Right.pop(0))
    if len(Left)==0:
        NewSorted=NewSorted+Right
    else:
        NewSorted=NewSorted+Left
    return NewSorted

# import ipdb; ipdb.set_trace()  #debuger I used while coding.


times=[]
times1=[]
#time measurment for KMergeSort:
for i in xrange(1,1000,10):  # n grows in order to see the trend.
    unsortedarray=random.sample(range(0, 100), 33)
    print KMergeSort(unsortedarray,4) #4 can be changed to any k>1.
    times.append((time.time() - start_time))

#time measurment for mergesort:
for i in xrange(1,1000,10):  # n grows in order to see the trend.
    unsortedarray=random.sample(range(0, 100), 33)
    print mergesort(unsortedarray,2)
    times1.append((time.time() - start_time))

#time measurment for mergesort without insertion sort break:
times2=[]
for i in xrange(1,1000,10):  # n grows in order to see the trend.
    unsortedarray=random.sample(range(0, 100), 33)
    print mergesortNoInsertion(unsortedarray,2)
    times2.append((time.time() - start_time))


#Plotting:
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
p1 = ax.plot(times, 'r', linewidth=2)
p2 = ax.plot(times1, 'b', linewidth=2)
p3 = ax.plot(times2, 'g', linewidth=2)

plt.xlabel('Length of n')
plt.ylabel('Time')
plt.title('Time in relation to growth of n')
plt.grid(True)
plt.show()
