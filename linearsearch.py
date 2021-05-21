
def orderedSequentialSearch(alist, item):
	    pos = 0
	    found = False
	    stop = False
	    while pos < len(alist) and not found and not stop:
	        if alist[pos] == item:
	            found = True
	        else:
	            if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1
	
	    return found

def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1

	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
val=search(testlist,42)
if val != -1:
    print("item found at position:", val)
else:
    print("item not found")