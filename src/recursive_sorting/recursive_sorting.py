# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    # if arrA or arrB is not empty...
    while len( arrA ) != 0 and len( arrB ) != 0:
        # check to see if the first element in arrA is smaller than the first element in arrB...
        if arrA[0] < arrB[0]:
            # if it is, add the first element in arrA to the end of merged_arr...
            merged_arr.append( arrA[0] )
            # and delete first element in arrA
            arrA.remove( arrA[0] )
            # print(arrA, arrB, merged_arr)
        else:
            # if it is not, add the first element in arrB to the end of merged_arr...
            merged_arr.append( arrB[0] )
            # and delete first element in arrB
            arrB.remove( arrB[0] )
            # print(arrA, arrB, merged_arr)

    # if arrA or arrB is empty, then add the other list to the end of merged_arr...
    if len( arrA ) == 0:
        merged_arr = merged_arr + arrB
        # merged_arr += arrB
    else:
        # merged_arr = merged_arr + arrA
        merged_arr += arrA
    
    # print( merged_arr )
    return merged_arr

# x = [2,4,6,8]
# y = [1,3,5,7,9,11,13,15]
# merge(x, y)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
