# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):

    # Start with current index = 0
    # For all indices EXCEPT the last index (loop through n-1 elements)
    for i in range(0, len(arr) - 1):

        cur_index = i

        smallest_index = cur_index

        # a. Loop through elements on right-hand-side of current index
        for j in range(cur_index, len(arr)):

            # and find the smallest element
            if arr[cur_index] > arr[j]:

                smallest_index = j

                # b. Swap the element at current index with the smallest element found in above loop
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



        
        # # a. Loop through elements on right-hand-side of current index
        # for j in range(cur_index, len(arr)):

        #     # and find the smallest element
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j 

        # temp = arr[smallest_index]

        # # b. Swap the element at current index with the smallest element found in above loop
        # arr[smallest_index] = arr[cur_index]
        
        # arr[cur_index] = temp
             


    return arr



# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    
    # initial state. True allows pass to start
    swapping = True
    
    while swapping:

        # switch state for next pass. If no swapping occurs this pass, it will stay False
        swapping = False

        # Loop through your array
        for i in range(0, len(arr)-1):

            # Compare each element to its neighbor
            if arr[i] > arr[i+1]:
                
                # If elements in wrong position (relative to each other, swap them)
                arr[i], arr[i+1] = arr[i+1], arr[i]

                # If swap occurs, switch state to True to allow next pass
                swapping = True

            # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    return arr


# def bubble_sort( arr ):
#     # Loop through your array
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             # Compare each element to its neighbor
#             if arr[i] < arr[j]:
#                 # If elements in wrong position (relative to each other, swap them)
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr