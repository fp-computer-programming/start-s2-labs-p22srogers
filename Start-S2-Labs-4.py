# Author: SMR(AMDG) 2/1/22
# First defining the function
def double_every_other(l):
# Returning x times 2 if i modulus 2 = remainder of zero . Otherwise x for i,x in enumerate list given   
    return [x * 2 if i % 2 else x for i, x in enumerate(l)]
