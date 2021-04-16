"""
Name: Jason Guerrero
UID: 305118489
"""
import math

#Problem 1:
def longestpath(d):
    pathLength = 0  # set path counter
    longestPath = {}    # store nodes in the longest path a -> b -> c -> ...
    middleNodes = []    # keep track of intermediate nodes
    
    for key, value in d.items():

        if ( key not in longestPath.keys() ) and  ( value not in middleNodes ):     # if the key is not in the longest path and value not an intermediate node
            if value in longestPath.keys():     # check if value is in longest path
                middleNodes.append(value)       # if so, add it to list of intermediate nodes

            longestPath[key] = value    # update longest path
            pathLength+=1       # update path counter
            
    return pathLength
        
# d1 = {"a":"b","b":"c"}
# d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}
# d3 = {"a":"b","b":"c","d":"a","e":"a","c":"d"}
# print(longestpath(d1))
# print(longestpath(d2))
# print(longestpath(d3))


# Problem 2:
def solve(f, guess, TOL):

    if abs(f(guess)[0]) <= TOL:    # if our guess is close enough to the root
        return guess            # we are done, return it

    update = guess - f(guess)[0]/f(guess)[1]    # if not use guess with first iteration of Newton's method

    while abs(f(update)[0]) > TOL:      #  while the approximation is still not close enough to the root
        update = update - f(update)[0]/f(update)[1]     # perform another iteration of Newton's method

    return update   # output final approximation

print(solve(lambda x: [x**2-1, 2*x], 3, 0))
print(solve(lambda x: [x**2-1, 2*x], -1, 0))
print(solve(lambda x: [math.exp(x) - 1, math.exp(x)], 1, 0))
print(solve(lambda x: [math.sin(x), math.cos(x)], 0.5, 0))

