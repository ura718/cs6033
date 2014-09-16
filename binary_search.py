#!/usr/bin/python

# binary search

def binary_search(a, x, low=0, high=None):
  if high is None:
    high = len(a)
    print "high: %s" % high

  while low < high:
    mid = (low + high) // 2
    print "mid: %s" % mid
    mid_value = a[mid]
    print "mid_value: %s" % mid_value
    
    if mid_value < x:
      low = mid + 1
      print "mid_value<x: %s<%s" % (low,x)

    elif mid_value > x:
      high = mid
      print "mid_value>x: %s>%s" % (high,x)

    else:
      return mid

  return -1


value = binary_search(a=[1,20,30,40,500,600], x=425)
print value,
   
