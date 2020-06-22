def avg(a,b):
    """This is doc type of a function in
     which we write for what we have made the function"""
    average=(a+b)/2
    #print(average)
    return average #return is must to get value,not to get none
    """ this is not doc type ,this is comment
    for multi line """
    ''' this is also a multi line comment to check that 
    single cote also works'''
v=avg(6,8)
print(v)
print(avg.__doc__)