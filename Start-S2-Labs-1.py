# Author: SMR (AMDG) 2/1/22
# Defining the function to take a list 
def smash(lst):
# Creating fresh blank quotes for variable x  
    x = ""
# For loop for index value in list enumerate    
    for index, value in enumerate(lst):
# If the index is zero, then x is equal to x + value        
        if index == 0:
            x = x + value
# Or else x is equal to x + whitespace+ its value        
        else:
            x = x +" "+ value
# must return x at the end to update x    
    return x
# Final print statement saying to 'buy the dip'    
print(smash(["Buy", "the", "dip."]))