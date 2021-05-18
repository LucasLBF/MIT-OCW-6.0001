# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
perm_list = []

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    if len(sequence) == 1:
        return sequence
    else:
        last_letter = sequence[-1]
        new_sequence = sequence[0:-1]
        perm = get_permutations(new_sequence)
        
        for seq in perm:
            for pos in range(len(seq) + 1) :
                s = seq[pos:] + last_letter + seq[:pos]
                perms.append(s)
                
                
    return list(set(perms))            
                
                
            
        
    
   
            

    

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

# Put three example test cases here (for your sanity, limit your inputs
# to be three characters or fewer as you will have n! permutations for a 
# sequence of length n)



