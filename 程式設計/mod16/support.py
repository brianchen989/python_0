# Module defintion
def print_func(arg):
    """Print Hello message to arg argument"""
    # print (__name__)
    print ('Hello :',arg)
print("Support module name : ",__name__)
print("the__file__ in support.py :",__file__)
if __name__ == '__main__':
# execute only if run as a script
    print("Support module is being run directly")