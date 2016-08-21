import re 
import sys
def createDict(filename,k):
    dictOfWords={}
    listOfWords = [re.sub(r'[?|$|.|!|,]',r'',i).strip().lower().split() for i in open(filename).readlines()]
    listOfWords=[j for i in listOfWords for j in i]
    #print(listOfWords)
    for i in range(len(listOfWords)):
        if(listOfWords[i] in listOfDictWords):
            listOfDictWords[listOfWords[i]]+=1
        else:
            listOfDictWords[listOfWords[i]]=1
        #print(listOfDictWords)
        for j in range(1,k+1):
            if(i-j>=0):
                #print((listOfWords[i],listOfWords[i-j]))
                if((listOfWords[i],listOfWords[i-j]) not in dictOfWords):
                    dictOfWords[(listOfWords[i],listOfWords[i-j])]=1
                else:
                    break
        #print(dictOfWords)
        #print('\n\n')
                
        for l in range(1,k+1):
            if(i+l<len(listOfWords)):
                if((listOfWords[i],listOfWords[i+l]) not in dictOfWords):
                    dictOfWords[(listOfWords[i],listOfWords[i+l])]=1
           
        for key in dictOfWords:
            #print(key)
            if(key in mainDict):
                mainDict[key]+=1  
            else:
                mainDict[key]=1
        dictOfWords={}
    #print(dictOfWords)
    #print(mainDict)
	#return mainDict
    #print("hello")
if __name__=="__main__":
    #dictOfWords={}
    listOfDictWords={}
    mainDict={}
    filename=sys.argv[1]
    k=int(sys.argv[2])
    if(k<1 or k>5):
        print("Invalid k")
        sys.exit()
    createDict(filename,k)
    while True:
        a, b = input().split(' ')
        a=a.lower()
        b=b.lower()
        val=(a,b,)
    #print(listOfDictWords)
    #print(val, mainDict)
        if(val in mainDict):
            searchTerm=int(mainDict[val])
            countWord=int(listOfDictWords[a])
            print("%.2f"%(searchTerm/countWord))
        else:
            print("0.00")