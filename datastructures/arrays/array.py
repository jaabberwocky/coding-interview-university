import numpy as numpy

class resizingArray:

    def __init__(self, data=None):
        ''' 
        Expects a list of data.
        '''
        if data is None:
            self.length = 0
        else:
            self.length = len(data)

        