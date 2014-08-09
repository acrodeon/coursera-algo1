#################################################################################
#                         Quick Sort                                            #
# A quick sort first selects a value, which is called the pivot value           #
# The actual position where the pivot value belongs in the final sorted list,   #
# the split point, will be used to divide the list for subsequent calls         #
#################################################################################

def quickSort(alist):
    """Quick Sort of alist"""
    return quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    """quick sort from first to last (included)"""
    # first == last, list of one element is already sorted
    if first < last:
        # pivot is at splitpoint in the final sorted list

        indexPivot = medianOf3(alist, first, last)
       
        splitpoint = partition(alist,first,last, indexPivot)
        # index < splitpoint => alist[index] <= pivot
        leftComparaisons = quickSortHelper(alist,first,splitpoint-1)
        # index > splitpoint => alist[index] > pivot
        rightComparaisons = quickSortHelper(alist,splitpoint+1,last)
        return (last - first) + leftComparaisons + rightComparaisons
    else:
        return 0

def partition(alist,first,last, indexPivot):
    """pivot at first position"""
    alist[first], alist[indexPivot] = alist[indexPivot], alist[first]
    pivotvalue = alist[first]
    i = first + 1
    for j in range(first+1, last+1):
        if alist[j] < pivotvalue:
            alist[j], alist[i] = alist[i], alist[j]
            i += 1
    alist[first], alist[i-1] = alist[i-1], alist[first]
    #print (alist[i-1],alist[first], i-1 )
    return (i-1)


def is_median(ar, i, j, k):
    """Determines whether ar[i] is a median of ar[i], ar[j] and ar[k]"""
    return (ar[i] < ar[j] and ar[i] > ar[k]) or (ar[i] > ar[j] and ar[i] < ar[k])

def medianOf3(ar,l,r):
    """return the index of the median of three"""
    m = l + ((r-l) >> 1)
    if is_median(ar, l, m, r):
        return l
    elif is_median(ar, m, l, r):
        return m
    else:
        return r

##################
# Main() to test #
##################
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print("Nb Comparaisons = {0}".format(quickSort(alist)))
    print(alist)
