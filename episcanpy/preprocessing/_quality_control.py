import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.axes as pltax

def coverage_cells(adata, bins=50, key_added=None):
    if key_added == None:
        key_added='sum_peaks'
    # make sum peaks
    sum_peaks = []
    matrix = np.matrix(adata.X)
    matrix = matrix.tolist()
    for var in matrix:
        sum_peaks.append(sum(var))
    adata.obs[key_added] = sum_peaks
    
    # number of peaks in a cell
    np.histogram(adata.obs[key_added])
    plt.hist(adata.obs[key_added], bins)
    plt.show
    
def commoness_features(adata, threshold=None, bw=0.5, key_added=None):
    if key_added == None:
        key_added='commonness'
    common = []
    matrix = np.matrix(adata.X)
    matrix = matrix.transpose()
    matrix = matrix.tolist()
    for var in matrix:
        common.append(sum(var))
    adata.var[key_added] = common

    if threshold != None:
        plt.axvline(x=threshold, color='r')
        
    sns.set_style('whitegrid')
    sns.kdeplot(np.array(adata.var[key_added]), bw)
