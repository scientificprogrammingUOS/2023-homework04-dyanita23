import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis = 0):
    #remove unnecessary dimensions
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)

    #check if they can be combined & then stack them
    #first get the shapes of both arrays
    shape1 = arr1.shape
    shape2 = arr2.shape


    #if axis is 0, cmbine vertically
    if axis == 0:
        if shape1[1:] != shape2[1:]:
            raise ValueError("The arrays cannot be combined along axis 0")
        return np.concatenate([arr1, arr2], axis = 0)
    
    #if the axis is 1, combine horizontally
    elif axis == 1:
        if shape1[0] != shape2[0]:
            raise ValueError("The arrays cannot be combined along axis 1")
        return np.concatenate([arr1, arr2], axis = 1)
    
    #if the axis is not 1 or 0
    else:
        raise ValueError("The two arrays cannot be combined!")
        


if __name__ == "__main__":

    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    combined = combination(arr1, arr2, axis=1)
    print(combined)