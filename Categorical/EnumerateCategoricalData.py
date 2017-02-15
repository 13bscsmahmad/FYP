
# coding: utf-8

# In[36]:

f = open("../Dataset/train_categorical.csv", "r") # original categorical_train


# In[37]:

possibleFeatureValues = set() # all unique features in raw data
lineCount = 0

first_line_skip = f.readline() # read 1st line (header row)
lineCount +=1

for line in f:
   
    elements = line.strip().split(',')
    for element in elements[1:len(elements)]: # skip ID numbers
        possibleFeatureValues.add(element)
        
    lineCount+=1
    


# In[38]:

print len(possibleFeatureValues)


# In[40]:

print possibleFeatureValues
print "total lines: ", lineCount


# In[78]:

f.close()


# In[79]:

"""
Replace each feature value with a number, starting with 0
"""

newFeature = 0



# In[80]:

"""
Create dictionary and map each set element to a unique integer
"""

dictionary = {}
for item in possibleFeatureValues:
    dictionary[item] = str(newFeature)
    newFeature += 1

print len(dictionary)


# In[81]:

f = open("../Dataset/train_categorical.csv", "r") # original categorical_train


# In[82]:

import csv
with open('enumeratedCategorical.txt', 'w') as enumeratedCategorical:
    
    header = f.readline()
    wr = csv.writer(enumeratedCategorical, lineterminator='\n')
    
    count = 0
    """
    Replace in place of each feature, the value for it in the dictionary
    """

    for line in f:
        fullRow = line.strip().split(",")
        for element in range(1,len(fullRow)):
            fullRow[element] = dictionary[fullRow[element]] # return the value of the element from the dict.
        # have to re-write this row in the new file
        wr.writerow(fullRow)
        count += 1


# In[86]:

f.close()

print "Done. Wrote " + str(count) + " lines."


# In[ ]:




# In[ ]:



