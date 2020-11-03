import random

#part i
def generateSequence(n):
    #creates array containing numbers 1 to n
    array = []
    for x in range(1,(n+1)):
        array.append(x)
    #now shuffle this array
    random.shuffle(array)
    return array


#part ii
def bubblesort(array):
    #bubblesort that sorts array and returns the number of flips
    flipCount = 0
    
    for x in range(len(array)):
        for y in range(0, len(array)-x-1):
            if(array[y] > array[y+1]):
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
                flipCount += 1
    return flipCount

#part iii
def mergesort(array):
    #will sort array and return number of flips
    flipCount = 0
    #keep merging until mergesort is called with only one element left
    if(len(array) > 1): 
        #divide the number of elements and divide by two to get number of elements in each half
        halfElements = len(array)//2
        #fill left array with first half of elements
        left = []
        for x in range(halfElements):
            left.append(array[x])
        #fill right array
        right = []
        for x in range(halfElements, len(array)):
            right.append(array[x])
        
        
        #recursive call to both halves
        flipCount += mergesort(left)
        flipCount += mergesort(right)
        
        #now merge them together
        leftCounter = 0
        rightCounter = 0
        arrayCounter = 0
        
        #while there are elements still in left and right compare them and add the smaller to array
        while(leftCounter < len(left) and rightCounter < len(right)):
            if(left[leftCounter] < right[rightCounter]):
                array[arrayCounter] = left[leftCounter]
                leftCounter += 1
                arrayCounter += 1
            else:
                array[arrayCounter] = right[rightCounter]
                flipCount += len(left) - leftCounter
                rightCounter += 1
                arrayCounter += 1
                
        #at this point either left or right has been exhausted so addd the rest of the other array
        while(leftCounter < len(left)):
            array[arrayCounter] = left[leftCounter]
            leftCounter += 1
            arrayCounter += 1
            
        while(rightCounter < len(right)):
            array[arrayCounter] = right[rightCounter]
            rightCounter += 1
            arrayCounter += 1
    return flipCount


#part iv
def data():
    print("now generating random sequences from 2 to 2^12 and then running bubblesort on them and printing number of flips for each")
    for x in range(1, 13):
        bigNum = 2**x
        tempArray = generateSequence(bigNum)
        print("when bubblesort runs on an array of length",bigNum," it does this many flips")
        print(bubblesort(tempArray))
        
    print("now generating random sequences from 2 to 2^12 and then running mergesort on them and printing number of flips for each")
    for x in range(1, 13):
        bigNum = 2**x
        tempArray = generateSequence(bigNum)
        print("when mergesort runs on an array of length",bigNum," it does this many flips")
        print(mergesort(tempArray))
        
data()