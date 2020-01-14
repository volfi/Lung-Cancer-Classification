import numpy as np

def normalize_data(data_unnormed, normalization = "None"):
    
    data_normed = np.zeros((23444,594))
    for i,line in enumerate(data_unnormed[1:]):
        splitted_line = np.asarray(line.split()[2:], dtype=float)
        if normalization == "Z":
            data_normed[i,:] = (splitted_line - np.mean(splitted_line))/np.std(splitted_line)
        elif normalization == "MinMax":
            data_normed[i,:] = (splitted_line - np.min(splitted_line))/(np.max(splitted_line)-np.min(splitted_line))
        else:
            data_normed[i,:] = splitted_line
    return data_normed