import numpy as np
def read_csv(csv_file_path):
    

    matrix = np.array(list(loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)))
    
    return matrix
