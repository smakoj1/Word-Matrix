from operator import truediv
from pickle import FALSE
import time



wordList = []
wordLists = []
rawTile = list()
dispList = list()
verifiedTile = list() 
controlStruct = {
"rowPos": 0,
"columnPos": 0
}

def createListFromFile(fileName):
   # print ("start")
    listObject = list()
    fileObject = open(fileName, "r")
    
    for word in fileObject:
        
        listObject.append(word.strip())
    fileObject.close() 
    return listObject
    
def secondWordList(seedList, newSeedList):

    seedListCache=seedList.copy() #remove word that begins with same letter of 1st word in tile 
    vowel = ["a","A","e","E","i","I","o","O","u","U"]
    consOne = ["j","m","n","v","x","y","z"]
    seedList = [x for x in seedList if x[0] != seedListCache[0][0] ]
    """
    seedList = [x for x in seedList if x[1] != seedListCache[0][1] ]
    seedList = [x for x in seedList if x[2] != seedListCache[0][2] ]
    seedList = [x for x in seedList if x[3] != seedListCache[0][3] ]
    seedList = [x for x in seedList if x[4] != seedListCache[0][4] ] #remove everything begining with same letter as first letter of word in poition 1  
    """
    #seedLost = [x for x in seedList if x[0][0] != "c" ]
    #print (seedList)
    consTwo = {
    "b": "lr", "c":"hklry","d":"r","f":"lr", "g":"hlnrw", "h":"y", "k":"lnrw",
    "l":"s", "p":"hjlr", "q":"u", "r":"h", "s":"chklmnptwq", "t":"hrwy", "w":"hr"
    }
    #seedList = [x for x in seedList if x[0][0] in consTwo["s"] or x[0][0] in vowel] 
    if seedListCache[0][0] in vowel:
        pass   
         #print("a")
    elif seedListCache[0][0] in consOne:
        #pass
        seedList = [x for x in seedList if x[0][0] in vowel]
         #print("b")
    else:
        seedList = [x for x in seedList if x[0][0] in consTwo[seedListCache[0][0]] or x[0][0] in vowel]    
         #seedList = [x for x in seedList if x[0][0] in consTwo[seedListCache[0][0]]]
         #print("c")
        #pass

 
    return seedList

def thirdWordList(seedList, newSeedList):
    seedListCache=seedList.copy() #remove word that begins with same letter of 1st word in tile 
    vowel = ["a","A","e","E","i","I","o","O","u","U"]
    consOne = ["j","m","n","v","x","y","z"]
    #seedList = [x for x in seedList if x[0] != optTwo[0]]
   # seedList = [x for x in seedList if x[0][0] != seedListCache[0][0] ] #remove everything begining with same letter as first letter of word in poition 1 

    return seedList

def fourthWordList(seedList, newSeedList):
    return seedList
 
def fifthWordList(seedList, newSeedList): 
    seedListCache=seedList.copy() 
    vowel = ["a","A","e","E","i","I","o","O","u","U"] 
    consTwo = { 
    "a": "a", "b": "lr", "c":"hklry","d":"r","f":"lr", "g":"hlnrw", "h":"y ", "k":"lnrw",
    "l":"s", "p":"hjlr", "q":"u", "r":"h", "s":"chklmnptwq", "t":"hrwy", " w":"hr"
    } 
    newSeedList = [x for x in newSeedList if x[3] != seedList[3] and x[3] != "e"]
    return newSeedList 
 
def fiveLetterWordListOptimizer(seedList): 
    newSeedList=seedList.copy() 
    optimizedLists = list() 
    optimizedLists.append(seedList) 
    optimizedLists.append(secondWordList(optimizedLists[0], newSeedList)) 
    optimizedLists.append(thirdWordList(optimizedLists[1], newSeedList))#, optimizedLists[-1]) 
    optimizedLists.append(fourthWordList(optimizedLists[2], newSeedList)) 
    optimizedLists.append(fifthWordList(optimizedLists[3], newSeedList))
        
    return optimizedLists

def verifyTile(rawTile):
    newTile=list() 
   # flipRow = list()
    
    for a in range(5):
        flipRow=list()
        for row in rawTile:     
            flipRow.append(row[a])
            flipRowStr =''.join(flipRow)    
        newTile.append(flipRowStr)  
        if newTile[0] in wordList and newTile[1] in wordList and newTile[2] in wordList and newTile[3] and newTile[4] in wordList:
            tileStat = True
        else:
            tileState = False
    return tileState

def ifEndOfFor(word, wordLists):
    if word == wordLists[-1]:
        return True
def dispTileFormatter(dispTile):
   # print (dispTile)

    for word in dispTile:
        dispList.append(word)
        if len(dispList) == 150:
            for x in range(5):
                print(dispList[x],dispList[x+5], dispList[x+10], dispList[x+15], dispList[x+20],
                dispList[x+25],dispList[x+30], dispList[x+35], dispList[x+40], dispList[x+45],
                dispList[x+50],dispList[x+55], dispList[x+60], dispList[x+65], dispList[x+70],
                dispList[x+75],dispList[x+80], dispList[x+85], dispList[x+90], dispList[x+95],
                dispList[x+100],dispList[x+105], dispList[x+110], dispList[x+115], dispList[x+120],
                dispList[x+125],dispList[x+130], dispList[x+135], dispList[x+140], dispList[x+145]
                )
            print("\n")    
            dispList.clear()
       

   # print(dispTile[0],"\n",dispTile[1],"\n",dispTile[2],"\n",dispTile[3],"\n",dispTile[4], end=" ")
"""
    for word in dispTile:
        print (*dispTile)
    #print('\n')
"""
#print("wordLists[0]")    
wordList = createListFromFile("5letetrs.txt")

#print (wordLists[1])

for word in wordList:
    wordLists = fiveLetterWordListOptimizer(wordList)
    for word in wordLists[0]:
        wordA = word
        rawTile.append(word)
        #print (wordLists[0])
        for word in wordLists[1]:
            wordB = word
            rawTile.append(word)
            for word in wordLists[2]:
                wordC = word
                rawTile.append(word)
                for word in wordLists[3]:
                    wordD = word
                    rawTile.append(word)
                    for word in wordLists[4]:
                        wordE = word
                        rawTile.append(word)
                        if verifyTile(rawTile):
                            verifiedTile.append(rawTile)
                       # print (rawTile)
                        dispTileFormatter(rawTile)
                        rawTile.pop()
                        if ifEndOfFor(wordE, wordLists[4]):
                            rawTile.pop()
                            if ifEndOfFor(wordD, wordLists[3]):
                                rawTile.pop()
                                if ifEndOfFor(wordC, wordList[2]):
                                    rawTile.pop()
                                    if ifEndOfFor(wordB, wordLists[1]):
                                        rawTile.pop()
                

#WordListOptimizer(wordList)

#genWordList(wordList[0])


#for word in wordLists[0]:
 #   #setControlStruct(1, 0)
  #  rawTile.insert(wordLists[0].index(word), word)
    
   # for word in wordList:
    #   setControlStruct(2, 0)
     ##  for word in wordList: 
       #     setControlStruct(3, 0)
        ##   for word in wordList:
          #          setControlStruct(4, 0)
           #         rawTile.insert(wordList.index(word), word)
            #        for word in wordList:
             #           setControlStruct(5, 0)
              #          rawTile.insert(4, word)
               #         if (verifyTile(rawTile)):
                #        #print(rawTile)
                 #       rawFile = rowPOP(wordList, word)
                  #      #time.sleep(5) 
                   # print(rawTile)    
                    #time.sleep(5)    
                    

  
 
def setControlStruct(x, y):
    controlStruct["rowPos"] = x
    controlStruct["colunmPos"] = y
    