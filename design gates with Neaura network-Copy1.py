
# coding: utf-8

# In[ ]:


# Binary function
def BF(x):
    if x>0:
        return 1
    return 0


# In[3]:


# output function
def OF(x):
    if x:
        return True
    return False


# In[15]:



w = np.array([-2, 1,2])
N=0.001
Input=[(1,1,1),(1,0,1),(0,1,1),(0,0,1)]
test_input = np.array([[1, 1,1], [1, 0,1],[0,1,1],[0,0,1]])
correct_output=[True,False,False,False]
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
    
    

    
        
        


# In[18]:


test=w[0]*1+w[1]*1+w[2]*1

if test>=0:
        print(True)
else:
     print(False)


# In[30]:


z=[int(input("Enter first input")),int(input("Enter second input")),1]
z
def AND(z):
    print(OF(BF(np.sum(z*w))))
    


# In[31]:


AND(z)


# In[ ]:




