import numpy as np

def calculate(list):
  if len(list) == 9:
    # Define to array 3x3
    array = np.array(list)
    array3x3 = array.reshape((3,3))
    
    # Result
    calculations = {
        'mean':[[array3x3[:, i].mean() for i in range(3)],
                [array3x3[i, :].mean() for i in range(3)],
                array3x3.mean()],
        'variance':[[array3x3[:, i].var() for i in range(3)],
                    [array3x3[i, :].var() for i in range(3)],
                    array3x3.var()],
        'standard deviation':[[array3x3[:, i].std() for i in range(3)],
                              [array3x3[i, :].std() for i in range(3)],
                              array3x3.std()],
        'max':[[array3x3[:, i].max() for i in range(3)], 
              [array3x3[i, :].max() for i in range(3)], 
              array3x3.max()],
        'min':[[array3x3[:, i].min() for i in range(3)], 
              [array3x3[i, :].min() for i in range(3)], 
              array3x3.min()],
        'sum':[[array3x3[:, i].sum() for i in range(3)], 
              [array3x3[i, :].sum() for i in range(3)], 
              array3x3.sum()]
    }
    
    # Return the result
    return calculations
  else:
    raise ValueError("List must contain nine numbers.")