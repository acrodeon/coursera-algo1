#################################################################################
#               Median Maintain with two Heaps (Min/Max)                        #
# in O(log(i))                                                                  #
#################################################################################

# provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
import heapq




class MedianHeap:
    """maintating the median of a stream of numbers arriving one by one, using O(log(n)) operations each step"""
    
    def __init__(self):
        """Max heap Hlow, Min Heap Hhigh"""
        self.h_low = []
        self.h_high = []

    def insert(self, x):
        """insert x in the streams and return the median"""

        # base case first element
        if (len(self.h_low) == 0):
            heapq.heappush(self.h_low, -x)
            return x
        else:
            # as self.h_low is Max Heap as a Min Heap for each (-1)*item
            z = self.h_low[0] * (-1)
            if x <= z:
                heapq.heappush(self.h_low, -x)
            else:
                heapq.heappush(self.h_high, x)

            # if necessary balance size of self.h_low and self.h_high
            lowSize = len(self.h_low)
            highSize = len(self.h_high)
            if highSize > lowSize:
                z = (-1) * heapq.heappop(self.h_high)
                heapq.heappush(self.h_low, z)
            elif lowSize >= highSize+2:
                z = (-1) * heapq.heappop(self.h_low)
                heapq.heappush(self.h_high, z)
                
            return (-1) * self.h_low[0]



##################
# Main() to test #
##################
if __name__ == '__main__':
##    data = [1,5,2,4,3]
##    medianMaintenance = MedianHeap()
##    for x in data:
##        print(medianMaintenance.insert(x))
##    
    lines = open('Median.txt').read().splitlines()
    # apply lambda function to every item of iterable and return a list of the results. 
    data = map(lambda x: int(x), lines)
    medians = []
    
    medianMaintenance = MedianHeap()
    
    for x in data:
        median = medianMaintenance.insert(x)
        medians.append(median)

    # Print out the last four digits of the running sum of medians
    sum = 0
    for x in medians:
        sum += x
    print(sum % 10000)

