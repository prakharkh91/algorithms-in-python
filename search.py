## All functions search for x in list given.
## given list can be unsorted. 
import random


## Complexity of search O(log(n))
## Currently works only for numbers 
## Have to extend to check against any object type.
##
## @param given_list the list to be checked against
## @param x var to be checked
## @return bool
def binary_search(x, given_list):
    ## TODO: Implement sorting algorithms without external libraries.
    given_list.sort()
    x = int(x)

    if (len(given_list) >= 1):
        mid = given_list[len(given_list)/2]
        print "len: " + str(len(given_list)) + " : mid : " + str(mid)
        if (x == mid):
            return True
        else:
            given_list = given_list[len(given_list)/2 + 1:] if (x > mid) else given_list[:len(given_list)/2]
            return binary_search(x, given_list)
    else:
        if (len(given_list) == 0):
            print given_list
            return False

x = range(100)
random.shuffle(x)
print binary_search(50, x)
