def problem(arr): 
    #we go through array and create max value up until every point by checking max of taking item, and not taking it
    
    #we create these two variables points1 and points2 which keep track of the two max values we need since we're saving space and not filling a whole array
    #for first item, the max will of course be take it
    points1 = arr[0]
    #for second item, the max will be the max between those two items
    points2 = max(arr[0], arr[1])
    
    #now we loop through the array, keeping track of the best point value for every i position and at the end return it
    maximumPoints = 0
    for i in range(2, len(arr)):
        #as an example we're on the third assignment, the max points we could get would be either (take it + points1) or (leave it + points 2)
        maximumPoints = max(arr[i] + points1, points2)
        
        #now to move on we update our two previous maxes
        points1 = points2 #we keep the value of points1 as the maximumPoints of two assignments behind our current
        points2 = maximumPoints #we keep points2 as the maximumPoints of one assignment behind the current
    return maximumPoints 
    
    
array = [1,10,1,1,14]
print(problem(array))