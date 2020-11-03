def alignStrings(x, y, cInsert, cDelete, cSub):
    S = [[0 for a in range(len(y) + 1)] for b in range(len(x) + 1)]
    S[0][0] = 0
    #insert first row for blank transform to y
    for j in range(1, len(y)+1):
        S[0][j] = S[0][j-1] + cInsert
    #insert first column for x transform to blank    
    for i in range(1, len(x) + 1):
        S[i][0] = S[i-1][0] + cInsert
    
    #consider all letters of x
    for i in range(1,len(x) + 1):
        #1,2,3,4 - now consider all letters of y
        for j in range(1,len(y) + 1):
            tempCost = -1
            if(x[i-1] == y[j-1]):
                #the letters being compared are the same so no-op
                tempCost = 0
            else:
                tempCost = cSub
                
            S[i][j] = min(S[i-1][j-1] + tempCost, S[i-1][j] + cDelete, S[i][j-1] + cInsert)
    return S
    
def extractAlignment(S, x, y, cInsert, cDelete, cSub):
    a = []
    i = len(x)
    j = len(y)
    
    while i != 0 or j != 0:
        if(i == 0):
            a.append("Insert")
            j = j-1
        elif(j == 0):
            a.append("Delete")
            i = i-1
        else:
            minValue = min(S[i][j-1], S[i-1][j-1], S[i-1][j])
            if(S[i-1][j-1] == minValue):
                #the parent is to the diagonal left, so record a swap or no-op and shift values of i and j
                if(S[i-1][j-1] == S[i][j]):
                    #no-op
                    a.append("No-Op")
                else:
                    a.append("Substitution")
                i = i-1
                j = j-1
            elif(S[i][j-1] == minValue):
                a.append("Insert")
                j = j-1
            else:
                a.append("Delete")
                i = i-1
    #we now have a list a with the backwards list of instructions so flip it
    a.reverse()
    return a
    
def commonSubstrings(x, L, a):
    #for each run of "no-ops" that are at least length L return that string
    stringCounter = 0
    blank = ""
    solution = []
    for i in range(len(x)):
        if(a[i] == "No-Op"):
            blank = blank + x[stringCounter]
            stringCounter += 1
        else:
            if(len(blank) >= L):
                solution.append(blank)
            blank = ""
            stringCounter += 1
    if(len(blank) >= L):
        solution.append(blank)
    return solution
    
    
#S = alignStrings("I hear the train a comin' it's rollin' round the bend  And I ain't seen the sunshine since I don't know when  I'm stuck in Folsom Prison and time keeps dragging on  But that train keeps a rollin' on down to San Antone.    When I was just a baby my mama told me son  Always be a good boy don't ever play with guns  But I shot a man in Reno just to watch him die  When I hear that whistle blowin' I hang my head and I cry.    I bet there's rich folks eatin' in a fancy dining car  They're probably drinkin' coffee and smokin' big cigars  But I know I had it comin' I know I can't be free  But them people keep a movin' that's what tortures me.    Well if they freed me from this prison if that railroad train was mine  I bet I'd move it on a little farther down the line  Far from Folsom Prison that's where I want to stay  And I'd let that lonesome whistle blow my blues away", "I hear the train a-comin, it's rolling 'round the bend  And I ain't been kissed lord since I don't know when  The boys in Crescent City don't seem to know I'm here  That lonesome whistle seems to tell me, Sue, disappear    When I was just a baby my mama told me, Sue  When you're grown up I want that you should go and see and do  But I'm stuck in Crescent City just watching life mosey by  When I hear that whistle blowin', I hang my head and cry    I see the rich folks eatin' in that fancy dining car  They're probably having pheasant breast and eastern caviar  Now I ain't crying envy and I ain't crying me  It's just that they get to see things that I've never seen    If I owned that lonesome whistle, if that railroad train was mine  I bet I'd find a man a little farther down the line  Far from Crescent City is where I'd like to stay  And I'd let that lonesome whistle blow my blues away", 2, 1, 2)
#a = extractAlignment(S, "I hear the train a comin' it's rollin' round the bend  And I ain't seen the sunshine since I don't know when  I'm stuck in Folsom Prison and time keeps dragging on  But that train keeps a rollin' on down to San Antone.    When I was just a baby my mama told me son  Always be a good boy don't ever play with guns  But I shot a man in Reno just to watch him die  When I hear that whistle blowin' I hang my head and I cry.    I bet there's rich folks eatin' in a fancy dining car  They're probably drinkin' coffee and smokin' big cigars  But I know I had it comin' I know I can't be free  But them people keep a movin' that's what tortures me.    Well if they freed me from this prison if that railroad train was mine  I bet I'd move it on a little farther down the line  Far from Folsom Prison that's where I want to stay  And I'd let that lonesome whistle blow my blues away", "I hear the train a-comin, it's rolling 'round the bend  And I ain't been kissed lord since I don't know when  The boys in Crescent City don't seem to know I'm here  That lonesome whistle seems to tell me, Sue, disappear    When I was just a baby my mama told me, Sue  When you're grown up I want that you should go and see and do  But I'm stuck in Crescent City just watching life mosey by  When I hear that whistle blowin', I hang my head and cry    I see the rich folks eatin' in that fancy dining car  They're probably having pheasant breast and eastern caviar  Now I ain't crying envy and I ain't crying me  It's just that they get to see things that I've never seen    If I owned that lonesome whistle, if that railroad train was mine  I bet I'd find a man a little farther down the line  Far from Crescent City is where I'd like to stay  And I'd let that lonesome whistle blow my blues away", 1, 1, 1)
#arr = commonSubstrings("I hear the train a comin' it's rollin' round the bend  And I ain't seen the sunshine since I don't know when  I'm stuck in Folsom Prison and time keeps dragging on  But that train keeps a rollin' on down to San Antone.    When I was just a baby my mama told me son  Always be a good boy don't ever play with guns  But I shot a man in Reno just to watch him die  When I hear that whistle blowin' I hang my head and I cry.    I bet there's rich folks eatin' in a fancy dining car  They're probably drinkin' coffee and smokin' big cigars  But I know I had it comin' I know I can't be free  But them people keep a movin' that's what tortures me.    Well if they freed me from this prison if that railroad train was mine  I bet I'd move it on a little farther down the line  Far from Folsom Prison that's where I want to stay  And I'd let that lonesome whistle blow my blues away", 10, a)
#print (arr)
    
#Problem 1c I think   
#print (alignStrings("EXPONENTIAL", "POLYNOMIAL", 2, 1, 2))

#print (alignStrings("THEIR", "THERE", 1, 1, 1))
#print (extractAlignment(alignStrings("THEIR", "THERE", 1, 1, 1), "THEIR", "THERE", 1, 1, 1))

print (extractAlignment(alignStrings("AAABCAADDADAAA", "AAAAAAAAAAAAAA", 1, 1, 1), "AAABCAADDADAAA", "AAAAAAAAAAAAAA", 1, 1, 1))
print (commonSubstrings("AAABCAADDADAAA", 2, extractAlignment(alignStrings("AAABCAADDADAAA", "AAAAAAAAAAAAAA", 1, 1, 1), "AAABCAADDADAAA", "AAAAAAAAAAAAAA", 1, 1, 1)))

#print (extractAlignment(alignStrings("FOUR", "SIX", 1, 1, 1), "FOUR", "SIX", 1, 1, 1))