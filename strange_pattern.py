import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    boolean_array = np.zeros(shape, bool)
    start=0

    for column in range(len(boolean_array)):

        boolean_array[column, start::3] = 1

        if start==0:
            start = 2
        else:
            start -= 1
            
    return boolean_array
        

if __name__ == "__main__":
    shape = 4, 3
    pattern = strange_pattern(shape)
    print(pattern)

    pass
