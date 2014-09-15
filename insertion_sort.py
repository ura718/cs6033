#!/usr/bin/python


mylist = [8, 2, 4, 9, 3, 6] # list elements in array mylist
print '%s <<initial list' % mylist

for j in range(1, len(mylist)):   # start from index 1 where list element 2 sits
  key = mylist[j]  	# list element inside array
  i = j	   	# j is an array (counter) index

  while i > 0 and mylist[i-1] > key:    # we start at location 2 - 1 => 8
    #print mylist[i-1], 
    mylist[i] = mylist[i-1]     # swap array elements because right is smaller then left
    i = i - 1                   # 'i' is the counter to end while loop. 'j' gives 'i' counter from for loop.
    mylist[i] = key
    print mylist


# sorted list    
print '%s <<end result' % mylist
