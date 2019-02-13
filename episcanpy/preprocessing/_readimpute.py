import numpy as np

def readandimputematrix(file_name, min_coverage=1):
    with open(file_name) as f:
        file = f.readlines()

    # separate annotation from data    
    head_var = file[0]
    head_var = head_var.split('\t')
    # Then, extract the sample names
    sample_names = []
    data_raw = []
    for l in file[1:]:
        l = l.split('\t')
        sample_names.append(l[0])
        data_raw.append(l[1:])

    # clear memory of useless variables 
    del file
    
    ##########################################
    # now, removing empty columns
    empties = []
    partial = []
    full =  []
    for index in range(1, len(data_raw[0])):
        column = [element[index] for element in data_raw]
        if len(list(set(column))) == 1:
            empties.append(index)
        elif len(list(set(column))) <= min_coverage:
            partial.append(index)
        else:
            full.append(index)
         
    ##########################################
    intermed_matrix = []
    name_windows_covered = []
    # let's remove the compltetly uninformative columns
    for index in range(1, len(head_var[1:])):
        if index in full:
            intermed_matrix.append([element[index] for element in data_raw])
            name_windows_covered.append(head_var[index])

    ########################################
    # imputing values.
    imputed_matrix = []
    for row in intermed_matrix:
        imputed_row = []
        if "nan" in row:
            mean = np.mean([float(e)  for e in row if e != "nan"])
            for element in row:
                if element == "nan":
                    imputed_row.append(str(mean))
                else: 
                    imputed_row.append(element)
            imputed_matrix.append(imputed_row)
        else:
            imputed_matrix.append(row)

    imputed_matrix = np.matrix(imputed_matrix).transpose()
    return(imputed_matrix, sample_names, name_windows_covered)
