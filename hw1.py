"""
Name: Jason Guerrero
UID: 305118489
"""

import random

# Problem 1:
def largerIndex(c):
    k = []
    for i in range(0, len(c)):
        if c[i] > i:
            k.append(1)         # k[i] = 1 if c[i] > i
        if c[i] == i:
            k.append(0)         # k[i] = 0 if c[i] = i
        if c[i] < i:
            k.append(-1)        # k[i] = -1 if c[i] < i
            
    return k
            
# Problem 1 test cases
# l1 = [1, 2, 0, 4, 2, 1, 40, -5]
# print(largerIndex(l1))
# l2 = [0, 3, 2, 1, 32, 3, 4, 0]
# print(largerIndex(l2))

#Problem 2:
def squareUpTo(n):
    l = []
    for i in range(0,n+1):
       if i*i <= n:             # append to l only if the square is not bigger than n
           l.append(i*i)
        
    return l
        

# Problem 2 test cases
# print(squareUpTo(10))
# print(squareUpTo(100))
# print(squareUpTo(101))

#Problem 3:
def flip1in3():
    
    coin1 = random.randint(0,1) # flip two coins
    coin2 = random.randint(0,1)
    
    while (coin1 == 0 and coin2 == 0): # if TT flip again
        coin1 = random.randint(0,1)
        coin2 = random.randint(0,1)
        
    if coin1 == 1 and coin2 == 1: # return true if HH
        return True
    elif coin1 != coin2: # return false if HT or TH
        return False
    
#Problem 4:
def duplicates(c):
    
    l = []
    for i in range(0, len(c)-1):    #iterate up to second to last element
        j=i+1
        for k in range(j, len(c)):  # for every (i+1)th element
            if c[i] == c[k]:        # if same append to l
                l.append(c[i])

    return l

#Problem 4 test cases
# l3 = [1, 2, 5, 3, 6, 2, 4, 5]
# l4 = [1, 3, 5, 5, 1, 4, 3]
# print(duplicates(l3))
# print(duplicates(l4))

#Problem 3 test 
"""
def flipTest():
        l = []
        headCounter = 0
        tailCounter = 0
        
        for i in range(999):
            x = flip1in3()
            if x == False:
                l.append(0)
                tailCounter+=1
            else:
                l.append(1)
                headCounter+=1
                 
        return [headCounter/(tailCounter+headCounter), tailCounter/(tailCounter+headCounter)]
    
print(flipTest())
"""
