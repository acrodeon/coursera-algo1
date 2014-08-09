####################################################################
# Algo1 Week2 : 10,000 integers between 1 and 10,000 (inclusive)   #
#               in some order, with no integer repeated.           #
####################################################################

import os
import sys
from algo1week2_quicksort import quickSort

def createListFromFile (fileName=""):
    """create a list of integers in fileName, one integer per line"""
    lst = []
    try:
        f = open(fileName, mode='r')
        while 1:
            x = f.readline()
            if x == '':
                break
            # remove the '\n' at the end of the line and transform x as int
            lst.append(int(x[:-1]))
        f.close()
        return lst
    except:
        print("ERROR: File ", fileName, "does not exist here ", os.getcwd ())
        return lst
            
########
# Main #
########
if __name__ == '__main__':
    l = createListFromFile("QuickSort.txt")
    #print(len(l))
    print("Nb Comparaisons = {0}".format(quickSort(l)))
