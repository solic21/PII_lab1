import numpy as np


def fuzzification(crisp_values, input_lvs):
    """
    Returns dict of terms, which were activated (P > 0)
    """

    result = {}

    for index, crisp_value in enumerate(crisp_values):
        # Get most close value to the given in Universe
        x_curr = np.argmax(input_lvs[index]['U'] >= crisp_value)
        result[index] = {}
        for term, mfs in input_lvs[index]['terms'].items():
            # Checking if P > 0
            if mfs[x_curr] > 0:
                result[index][term] = mfs[x_curr]

    return result

