# Author: SMR(AMDG) 2/1/22
# Define the function to receive two different values
def comes_after(st, letter):
# Sets the variable letter which is the second value accepted, to all lower case    
    letter = letter.lower()
# Then returns the alphabetic character after every instance of letter. Now it's case insensitive due to lowercasing everything in previous line of code.
    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha())
    