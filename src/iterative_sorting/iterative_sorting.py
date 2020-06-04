# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # ## loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # ## TO-DO: find next smallest element
        # ## (hint, can do in 3 loc)
        # ## Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # ## TO-DO: swap
        # ## Your code here
        arr[i], arr[smallest_index] = arr[smallest_index, arr[i] ]

    return arr

#########################################################

# ##Resources:

# ## 1.  

# ## Traverse through all array elements 
# for i in range(len(A)): 
      
#     ## Find the minimum element in remaining  
#     ## unsorted array 
#     min_idx = i 
#     for j in range(i+1, len(A)): 
#         if A[smallest_index > A[j]: 
#             min_idx = j 
              
#     ## Swap the found minimum element with  
#     ## the first element         
#     A[i], A[smallest_index = A[smallest_index, A[i] 
  
# ## Driver code to test above 
# print ("Sorted array") 
# for i in range(len(A)): 
#     print("%d" %A[i]), 
########################################################


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr



############################################
# ## Bubble Sort ==>
# ## Refernces

# ##  1.  https://www.geeksforgeeks.org/python-program-for-selection-sort/:
# ## # Traverse through all array elements 
# for i in range(len(A)): 
      
# ##    # Find the minimum element in remaining  
# ##     # unsorted array 
#     min_idx = i 
#     for j in range(i+1, len(A)): 
#         if A[smallest_index > A[j]: 
#             min_idx = j 
              
# ##     # Swap the found minimum element with  
# ##     # the first element         
#     A[i], A[smallest_index = A[smallest_index, A[i] 

####################################################


# ## 2. https://www.educba.com/bubble-sort-in-python/ 

# def bubble_Sort(arr):
# m = len(arr)
# # Traverse through all the array elements
# for u in range(m):
# for v in range(0, m-u-1):
# # traverse the array from 0 to m-u-1
# # Swap if the element is greater than adjacent next one
# if arr[v] > arr[v+1] :
# arr[v], arr[v+1] = arr[v+1], arr[v]

######################################################################

# ## 3. https://www.programminginpython.com/bubble-sort-algorithm-python/

	# def bubble_sort(sort_list):
	#     for j in range(len(sort_list)):
	#         for k in range(len(sort_list) - 1):
	#             if sort_list[k] > sort_list[k + 1]:
	#                 sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
	#     print(sort_list)
	
	
	# lst = []
	# size = int(input("Enter size of the list: \t"))
	
	# for i in range(size):
	#     elements = int(input("Enter the element: \t"))
	#     lst.append(elements)
	
	# bubble_sort(lst)

#################################################################



'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
