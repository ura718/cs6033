#!/usr/bin/python

import math

n = 2000

print "\t\t1"
print "n^log(n): \t", n**math.log(n)
print "loglog(n): \t", math.log(math.log(n))
print "log10(n): \t", math.log10(n)
print "log(n): \t", math.log(n)
print "2^log(n): \t", 2**math.log(n)
print "n: \t\t", n
print "log(n)*1000: \t", math.log(n) * 1000
print "log^(1000)n: \t", math.log(1000)*n
print "log^1000n: \t", math.log(1000)*n
print "log(n)^log(n): \t", math.log(n)**math.log(n)
