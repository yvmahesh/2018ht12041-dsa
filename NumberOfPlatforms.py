# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 01:14:26 2018

@author: mahesh
"""
import sys
#find the minimum number of platforms so that all the trains can be 
#accommodated as per their schedule

#Ex: The time table is as given below, the answer is 3. otherwise, 
#the railway station will not be able to accommodate all the trains 

#Rail         Arrival        Departure
#Rail A        0900hrs.        0930hrs
#Rail B        0915hrs.        1300hrs
#Rail C        1030hrs        1100hrs
#Rail D        1045hrs        1145hrs
 
def findPlatform(arr,dep,n): 

    # Sort arrival and departure arrays 
    arr.sort() 
    dep.sort() 

    # plat_needed indicates number of platforms needed at a time 
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in merge sort to process all events in sorted order 
    while (i < n and j < n): 
    
        # If next event in sorted order is arrival, increment count of 
        # platforms needed 
        if (arr[i] < dep[j]): 
             plat_needed+=1
             i+=1
             # Update result if needed 
             if (plat_needed > result): 
                result = plat_needed 
        
         # Else decrement count of platforms needed 
        else: 
             plat_needed-=1
             j+=1
        
    return result 

# driver code 
if __name__ == '__main__':
    if(len(sys.argv) == 3):
        arr_input=sys.argv[1]
        arr = [int(e.lstrip("0")) if e.lstrip("0").isdigit() else e for e in arr_input.split(',')]
        dep_input=(sys.argv[2])
        dep = [int(e.lstrip("0")) if e.lstrip("0").isdigit() else e for e in dep_input.split(',')]
        print (arr)
        print (dep)
        if(len(arr) != len(dep)):
            print ("Arrival and Departure Count is not Matching")
        else:
            n = len(arr) 
            print("Minimum Number of Platforms Required = ", findPlatform(arr, dep, n)) 
    else:
        print ("Please specify arrival and departure timings")

