import numpy, random, os

learningRate = 1
bias = 1

weights = [random.random(),random.random(),random.random()]
print(weights)

def Perceptron(input1,input2,output):
    
    outputP = input1*weights[0] + input2*weights[1] + bias*weights[2]
    
    outputP = 1/(1+numpy.exp(-outputP))
    
    #if outputP>0:
     #   outputP = 1
    #else :
     #   outputP = 0
    
    error = output - outputP
    print(error)
    weights[0] = weights[0] + error * input1 * learningRate
    weights[1] = weights[1] + error * input2 * learningRate
    weights[2] = weights[2] + error * bias * learningRate
    
def main():
    
    for i in range(50):
        Perceptron(1,1,1)
        Perceptron(1,0,1)
        Perceptron(0,1,1)
        Perceptron(0,0,0)
        print("\n")
    
    print("Please enter two values in 1's or 0's")
    x = int(input())
    y = int(input())
    
    outputP = x*weights[0] + y*weights[1] + bias*weights[2]
    
    if outputP > 0 :
        outputP = 1
    else:
        outputP = 0
    
    print(x,"or",y, "is : ",outputP)
    
    
if __name__ == "__main__":
    main()