import numpy as np
# The odd ones out
arr= np.array([[1,2,3],[5,7,9],[2,4,6,], [7,7,7]])

def onlyOdd(arr):
    odd_arr =[]
    for row in arr:
        if all (element %2 != 0 for element in row):
            odd_arr.append(row)
    odd_arr=np.array(odd_arr)
    print(odd_arr)
onlyOdd(arr)

#2 Lets play checkers
checkers= np.zeros ((8,8), dtype=int)
print(checkers)
#2.2
for i in range(8): #why can't i do the for row in checkers??
    if (i % 2 == 0):  
        checkers[i] = 1-np.arange(8) % 2  
print(checkers)

#2.3
for i in range(8): 
    if (i%2 ==1):
        checkers[i] = np.arange(8) %2
print(checkers)

#2.4 
def reverse_checkerboard():
    for i in range(8): #why can't i do the for row in checkers??
        if (i % 2 == 0):  
            checkers[i] = np.arange(8) % 2  
    for i in range(8): 
        if (i%2 ==1):
            checkers[i] = 1-np.arange(8) %2
    return checkers
print(reverse_checkerboard())
#3
universe = np.array(["galaxy", "clusters"])
def expansion(universe,x): 
    spaces= ' '* x
    all_lists= []
    for word in universe: 
        expansion= spaces.join(list(word))
        all_lists.append(expansion) 
    return np.array(all_lists)

print(expansion(universe,1))    
print(expansion(universe,2))

#4
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
def secondLargest(planets):
    second_largest_values = []
    for col in planets.T:
        values= np.unique(col)
        if len(values) >= 2:
            second_largest_values.append(np.sort(values)[-2])
    return np.array(second_largest_values)

print(secondLargest(planets))



                
