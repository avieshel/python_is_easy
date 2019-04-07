'''
 As part of the course 'python is easy' by Pirple, i would like to introduce
 the heapq algorithm, as part of #10 homework assignment on 'importing'
'''

'''
  A heap is a data structure that can maintains an invariant that the minimum
  (or maximum) value is always at it's root and the user can 'get-min' (or 
  get-max) in a O(1) time complexity.

  This is very useful for a priority queue, let's say we want to have a program
  that get's alert messages, where the higher the alert the sooner it should be 
  delt with.
  We could have a priority queue (i.e. heap) where the alert-level is the key
  by which we insert events, and later we always 'get he alert with highest 
  priority' and deal with it.
  The following code sample will show you how to use python's built in heapq
  for more see: https://en.wikipedia.org/wiki/Heap_(data_structure)
'''
  
# import the heap queue algorithm python implementation
import heapq

# sample data (Serverity levels: 0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notice, 6=Information, 7=Debug, 8=OK)
msg_sevs = [8,4,5,2,1,0,6,3,2]

# take the message severity levels and create a heap (min heap => highest serverity )
heapq.heapify(msg_sevs)

# print the sevs queue (note the list is now in 'heap order')
'''
      0
   1     5
 2  4   8 6
3 2
'''
print(msg_sevs)

# get the highest severity message (note this also removes the item!)
print('The current highest serverity is: ',heapq.heappop(msg_sevs))

# print the sevs queue(note the 0=Emergency is not there)
'''
       1
   2       5
 2   4   8   6
3
'''
print(msg_sevs)

# a new severity message was received, severity = CRITICAL (2)
print('A new Critical severity message was recieved, level = 2')
heapq.heappush(msg_sevs, 2)

'''
      1
   2     3
 2  4   6  8
3 2
'''
print(msg_sevs)

# common use case is to push a new item, and pop the min right away python 
# provides a built in function for this (which is more efficient than push 
# and pop seperately)
print('Push severity 4 and get min(highest) severity message', heapq.heappushpop(msg_sevs, 4))

# get the top 3 severity messages (note: this doesn't change the msg_sevs)
print('Top 3 (highest) severity messages: ',heapq.nsmallest(3, msg_sevs))

# get the last 3 (lowest) severity messages
print('Bottom 3 (least) severe messages: ',heapq.nlargest(3,msg_sevs))
