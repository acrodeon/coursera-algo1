#################################################################################
#                        2-SUM algorithm                                        #                                      
# that for given list of integers and number t finds whether there are          #
# two distinct integers x and y in the list such that x+y = t                   #
#################################################################################

import threading, sys

class TwoSum():
    """integers x and y in the list such that x+y = t"""
    def __init__(self, numbers):
        """numbers as list of integers and target as the expect 2-sum"""
        self.hashTable = {}
        self.nbTwoSums = 0
        for x in numbers:
            self.hashTable[x] = True

    def hasTwoSum(self, t):
        """returns True if there is 2-sum x+y==t with x,y in hashTable"""
        for x in self.hashTable.keys():
            y = t-x
            if y != x and y in self.hashTable:
                return True
        return False

    def twoSumCounters(self, t):
        """returns True if there is 2-sum x+y==t with x,y in hashTable"""
        stop1 = False
        stop2 = False
        for x in self.hashTable.keys():
            y1 = t-x
            y2 = -t-x
            if not stop1:
                if y1 != x and y1 in self.hashTable:
                    self.nbTwoSums += 1
                    stop1 = True
                    print("Target Sum {0} : {1}".format(t, self.nbTwoSums))
            if not stop2 and t != 0:
                if y2 != x and y2 in self.hashTable:
                    self.nbTwoSums += 1
                    stop2 = True
                    print("Target Sum {0} : {1}".format(-t, self.nbTwoSums))
            if stop1 and stop2:
                break



def main():
    """Main function to be launched as thread"""
    lines = open('algo1-programming_prob-2sum.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    twoSum = TwoSum(data)
    twoSum.nbTwoSums = 0
    for t in range(0, 10001):
        twoSum.twoSumCounters(t)
    print("Number of two Sums is {}".format(twoSum.nbTwoSums))

    
##################
# Main() to test #
##################
if __name__ == '__main__':
##    # In summary, sys.setrecursionlimit is just a limit enforced by the interpreter itself.
##    # threading.stack_size lets you manipulate the actual limit imposed by the OS. If you hit the latter limit first, Python will just crash completely.
##    threading.stack_size(67108864) # 64MB stack
##    # to avoid RuntimeError: maximum recursion depth exceeded because by default 1000 is the limit returnt by sys.getrecursionlimit()
##    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
##    thread = threading.Thread(target = main) # instantiate thread object
##    thread.start() # run program at target
    main()



        
