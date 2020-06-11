# Problem Set 4A
# Name: Ayush Garg

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
    '''
    if (len(sequence) == 1):
        return [sequence]
    else:
        first_letter = sequence[0]
        new_list = get_permutations((sequence[1:]))
        all_perms = []
        for perm in new_list:
            all_perms.append(first_letter + perm)
            for i in range(len(perm)-1):
                all_perms.append(perm[0:i+1] + first_letter + perm[i+1:])
            all_perms.append(perm + first_letter)
        return all_perms

if __name__ == '__main__':
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))

   example_input_2 = 'xyz'
   print('Input:', example_input_2)
   print('Expected Output:', ['xyz', 'yxz', 'yzx', 'xzy', 'zxy', 'zyx'])
   print('Actual Output:', get_permutations(example_input_2))

   example_input_3 = 'dog'
   print('Input:', example_input_3)
   print('Expected Output:', ['dog', 'odg', 'ogd', 'dgo', 'gdo', 'god'])
   print('Actual Output:', get_permutations(example_input_3))