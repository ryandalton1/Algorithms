def cuRobot(k, pods):
    tempPreviousValue = 0
    tempCurrentCharge = k
    numStops = 0
    solutionList = []
    for x in pods:
        if(x < tempCurrentCharge):
            tempPreviousValue = x
        else:
            solutionList.append(tempPreviousValue)
            numStops+=1
            tempCurrentCharge = tempPreviousValue + k
            if(x < tempCurrentCharge):
                tempPreviousValue = x
            
    print('Number of stops required is: ', numStops)
    print('The stops are: ', solutionList)
    
    
    
testK1 = 40
testPods1 = [0,20,37,54,70,90]
cuRobot(testK1, testPods1)

testK2 = 20
testPods2 = [0,18,21,24,37,56,66]
cuRobot(testK2, testPods2)

testK3 = 20
testPods3 = [0,10,15,18]
cuRobot(testK3, testPods3)