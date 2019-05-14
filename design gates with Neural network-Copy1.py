
# coding: utf-8
import Numpy as np
# Binary function
def BF(x):
    if x>0:
        return 1
    return 0

# output function
def OF(x):
    if x:
        return True
    return False

w = np.array([-2, 1,2])
N=0.001
Input=[(1,1,1),(1,0,1),(0,1,1),(0,0,1)]
test_input = np.array([[1, 1,1], [1, 0,1],[0,1,1],[0,0,1]])
correct_output=[True,False,False,False]
#show dataset to know if linear or not
import matplotlib.pyplot as plt
x=np.array([[1,1],[1,0],[0,1],[0,0]])
y=[True,False,False,False]
for t in range(4):
    if y[t]==True:
        plt.scatter(x[t][0] , x[t][1]  , alpha = 0.8,c='r')
    else:
        
        plt.scatter(x[t][0] , x[t][1]  , alpha = 0.8,c='y')
plt.show()

# trian by preceptron


for i in range(40):
    index=0
    count=1    
    for t in Input:
        classifier_Equestion =np.sum(test_input[index]*w)

        if OF(BF(classifier_Equestion))!=correct_output[index]:
            count+=1
            while OF(BF(classifier_Equestion))!=correct_output[index]:
                w=w+(test_input[index]*(N*((int(correct_output[index])-int(OF(BF(classifier_Equestion)))))))
                classifier_Equestion =np.sum(test_input[index]*w)
        index +=1
    if count==1:
        break
    
    #using the programming here
z=[int(input("Enter first input")),int(input("Enter second input")),1]
def AND(z):
    print(OF(BF(np.sum(z*w))))
    
AND(z)







