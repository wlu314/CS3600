from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)


def question_5_pen():
    ## tuppl = [(max_acc, average_acc, std_acc)]
    tup_list = []
    max_acc = 0
    
    iter_list = []
    for i in range(5):
        nnet, testAccuracy = testPenData()
        if testAccuracy > max_acc:
            max_acc = testAccuracy
        iter_list.append(testAccuracy)
    avg_acc = average(iter_list)
    std_acc = stDeviation(iter_list)
    tup_list.append((max_acc, avg_acc, std_acc))
    return tup_list
        
        
def question_5_car():
    ## tuppl = [(max_acc, average_acc, std_acc)]
    tup_list = []
    max_acc = 0
    
    iter_list = []
    for i in range(5):
        nnet, testAccuracy = testCarData()
        if testAccuracy > max_acc:
            max_acc = testAccuracy
        iter_list.append(testAccuracy)
    avg_acc = average(iter_list)
    std_acc = stDeviation(iter_list)
    tup_list.append((max_acc, avg_acc, std_acc))
    return tup_list

def question_6_car():
    ## tuple = [(number, max_acc, average_acc, std_acc)]
    tup_list = []
    for i in range(0, 41, 5): ## 0 to 40 inclusive; increment 5
        iter_list = []
        max_acc = 0
        for j in range(5): ## 5 iterations 
            nnet, testAccuracy = testCarData(hiddenLayers= [i])
            iter_list.append(testAccuracy)
            if testAccuracy > max_acc:
                max_acc = testAccuracy
        avg_acc = average(iter_list)
        std_acc = stDeviation(iter_list)
        tup_list.append((i, max_acc, avg_acc, std_acc))
        
    return tup_list

def question_6_pen():
    ## tuple = [(number, max_acc, average_acc, std_acc)]
    tup_list = []
    for i in range(0, 41, 5): ## 0 to 40 inclusive; increment 5
        iter_list = []
        max_acc = 0
        for j in range(5): ## 5 iterations 
            nnet, testAccuracy = testPenData(hiddenLayers= [i])
            iter_list.append(testAccuracy)
            if testAccuracy > max_acc:
                max_acc = testAccuracy
        avg_acc = average(iter_list)
        std_acc = stDeviation(iter_list)
        tup_list.append((i, max_acc, avg_acc, std_acc))
        
    return tup_list

#results_car_5 = question_5_car()
#print("Question 5: Car Data Results:")
#for result in results_car_5:
#    print(result)
   

#results_pen_5 = question_5_pen()
#print("\n Question 5: Pen Data Results:")
#for result in results_pen_5:
#    print(result)


#results_car_6 = question_6_car()
#print("\n Question 6: Car Data Results:")
#for result in results_car_6:
#   print(result)
    
results_pen_6 = question_6_pen()
print("\n Question 6: Pen Data Results:")
for result in results_pen_6:
    print(result)