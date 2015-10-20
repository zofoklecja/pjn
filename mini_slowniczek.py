def freq_dic(sequence):
    return {x: sequence.count(x) for x in set(sequence)}
