import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    
    #make sure that every parameter is an integer or float
    if not isinstance(loc, (float, int)): 
        raise TypeError("One parameter is not an integer or float!")
    if not isinstance(scale, (float, int)): 
        raise TypeError("One parameter is not an integer or float!")
    if not isinstance(lower_bound, (float, int)): 
        raise TypeError("One parameter is not an integer or float!")
    if not isinstance(upper_bound, (float, int)): 
        raise TypeError("One parameter is not an integer or float!")
    
    #check if the lower bound is smaller than the upper bound
    if lower_bound >= upper_bound:
        raise ValueError("The lower bound is bigger than the upper bound!")
    
    #In the function 100 samples of a gaussian distribution 
    #should be drawn in respect to the given loc 
    #and scale parameters
    samples = np.random.normal(loc, scale, 100)

    #Values below the lower bound an dabove the upper bound should be filtered out
    filtered_samples = [x for x in samples if lower_bound <= x <= upper_bound]

    #calculate mean and standard deviation
    mean = np.mean(filtered_samples)
    std = np.std(filtered_samples)
    
    return (mean, std)


if __name__ == "__main__":
    gaussian_analysis(3, 4, 1, 2)

