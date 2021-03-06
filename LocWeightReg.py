import numpy as np
import math

#locally weighted regression, a non-parametric learning algo for non-linear curves
#could add T as "bandwidth" variable
class LocWeightReg:

    #input list is of format [[x1,x2,y],...]
    def __init__(self,inputList):
        self.mainList = inputList
        self.alpha=0.1
        self.numOfFeatures = len(inputList[0])
        self.numOfExamples = len(inputList)
        self.thetas = np.zeros(self.numOfFeatures)
        self.convToNPArray()
        inputTest = np.array([6,6])
        toCompare = np.array(self.mainList[1])
        self.trainForInput(inputTest,1)

    def convToNPArray(self):
        zeroFeature = np.zeros(self.numOfExamples)
        oneFeature = np.zeros(self.numOfExamples)
        yValues = np.zeros(self.numOfExamples)
        for i in range(len(self.mainList)):
            zeroFeature[i] = self.mainList[i][0]
            oneFeature[i] = self.mainList[i][1]
            yValues[i] = self.mainList[i][2]
        self.zeroFeature = zeroFeature
        self.oneFeature = oneFeature
        self.yValues = yValues

    #input two feature vectors, output weighted vector
    #xi iteration, x newValue
    def weightFunction(self,x,xi):
        x = x - xi
        x = np.dot(x,x)
        x = x/-2
        x = math.exp(x)
        return x

    def trainForInput(self,newVal,numOfIter):
        for w in range(numOfIter):
            for j in range(self.numOfFeatures):
                currJ = 0
                for i in range(self.numOfExamples):
                    currWeight = self.weightFunction(newVal,np.array([self.zeroFeature[i],self.oneFeature[i]]))
                    thetaTranspX = np.dot(self.thetas,np.array([1,self.zeroFeature[i],self.oneFeature[i]]))
                    diffSquare = math.pow(self.yValues[i] - thetaTranspX,2)
                    diffSquare = currWeight * diffSquare
                    currJ+=diffSquare
                print(currJ)
                for i in range(len(self.thetas)):
                    self.thetas[i] = self.thetas[i] - self.alpha*currJ
            print(self.thetas) 