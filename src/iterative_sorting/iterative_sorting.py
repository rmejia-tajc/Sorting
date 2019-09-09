# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # while cur_index > 0 






        # Start with current index = 0

        # For all indices EXCEPT the last index:

        # a. Loop through elements on right-hand-side of current index and find the smallest element

        # b. Swap the element at current index with the smallest element found in above loop
             



        # TO-DO: swap




    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    # initial state
    swapping = True
    
    while swapping:

        # switch state for next pass if no swapping occurs this pass
        swapping = False

        # Loop through your array
        for i in range(0, len(arr)-1):

            # Compare each element to its neighbor
            if arr[i] > arr[i+1]:
                
                # If elements in wrong position (relative to each other, swap them)
                arr[i], arr[i+1] = arr[i+1], arr[i]

                swapping = True
                # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    return arr
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr