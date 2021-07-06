def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    input_list.reverse()
    return input_list

def count_digits(n):
    """
    Return count of digits
    """
    c=0
    while(n>0):
        c+=1
        n//=10
    return c