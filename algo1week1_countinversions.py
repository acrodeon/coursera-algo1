##########################################
# Algo1 Week1 : MergeandCount Inversions #
##########################################


def count_inversion(lst):
    """return the number of inversions (merge sort is used) of int (not string)"""
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    """the (Merge Sorted)list and the number of inversions"""
    # base case single element thus no inversion
    if len(lst) <= 1:
        return (lst, 0)
    #break in two lists  
    middle = len(lst) // 2
    # a is the number of left inversions from indices 0 .. middle-1
    (left, a) = merge_count_inversion(lst[:middle])
    # b is the number of right inversions from indices middle .. len(lst)-1
    (right, b) = merge_count_inversion(lst[middle:])
    # c is the number of split inversions
    (result, c) = merge_count_split_inversion(left, right)
    
    return (result, a + b + c)

def merge_count_split_inversion(left, right):
    """Merge sorted left and right lists and give nb of split arrays"""
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    # += and not append because append([1,5]) is [[1,5]]
    result += left[i:]
    result += right[j:]
    return (result, count)        

##################
# Main() to test #
##################
if __name__ == '__main__':
    input_array_1 = []  #0
    input_array_2 = [1] #0
    input_array_3 = [1, 5]  #0
    input_array_4 = [4, 1] #1
    input_array_5 = [4, 1, 2, 3, 9] #3
    input_array_6 = [4, 1, 3, 2, 9, 5]  #5
    input_array_7 = [4, 1, 3, 2, 9, 1]  #8


    print (input_array_1, count_inversion(input_array_1))
    print (input_array_2, count_inversion(input_array_2))
    print (input_array_3, count_inversion(input_array_3))
    print (input_array_4, count_inversion(input_array_4))
    print (input_array_5, count_inversion(input_array_5))
    print (input_array_6, count_inversion(input_array_6))
    print (input_array_7, count_inversion(input_array_7))
