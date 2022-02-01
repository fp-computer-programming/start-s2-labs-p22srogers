# Author: SMR (AMDG) 2/1/22
# First Defining the Function
def add_last_initial(names,linit):
# Setting x = 0 as a counter   
    x = 0
# For the index value in names enumate    
    for i, v in enumerate(names):
# For loop making the ind_2, seat enumerate the value        
        for ind_2, seat in enumerate(v):
# Update the names to add last initial            
            names[i][ind_2] += " "+ linit[x] + "."
 # Set x equal to x + 1           
            x += 1
    return names
initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
rows = add_last_initial(rows, initials)
print(rows)
