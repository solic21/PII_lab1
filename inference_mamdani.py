import itertools
import numpy as np
import fuzzy_operators
import membership_functions
import fuzzifier
import defuzzifier


def preprocessing(input_lvs, output_lv):
    '''
    Creates the Universe (U) and MFs (input and output)
    '''

    # Creation of the Universe
    for item in input_lvs:
        item['U'] = np.arange(*item['X'])
    output_lv['U'] = np.arange(*output_lv['X'])

    # Creation of the input MFs
    for lv in input_lvs:
        for key, value in lv['terms'].items():
            mf, *params = value
            lv['terms'][key] = getattr(membership_functions, mf)(lv['U'], *params)

    # Creation of the output MFs
    for key, value in output_lv['terms'].items():
        mf, *params = value
        output_lv['terms'][key] = getattr(membership_functions, mf)(output_lv['U'], *params)


def activated_rules(fuzzy_values, rule_base):
    '''
    Returns ativated rules
    '''
    terms = (item.keys() for item in fuzzy_values.values())
    antecedents = tuple(itertools.product(*terms))
    return [rule for rule in rule_base if rule[0] in antecedents]


def implication(fuzzy_values, activated_rules, output_lv):
    '''
    Returns final MFs
    '''
    result = []
    for rule in activated_rules:
        antecedent, consequent = rule
        mfs = (fuzzy_values[index][term] for index, term in enumerate(antecedent))
        tmp = fuzzy_operators.fuzzy_min(output_lv['terms'][consequent], min(mfs))
        result.append(tmp)
    return result


def aggregation(*fuzzy_sets):
    '''
    Aggregate final MFs
    '''
    return fuzzy_operators.fuzzy_union(*fuzzy_sets)


def process(input_lvs, output_lv, rule_base, crisp_values):
    '''
    Returns overall output: ((defuzzified value, term), final MF)
    '''

    # Get probabilities of terms
    fuzzy_values = fuzzifier.fuzzification(crisp_values, input_lvs)
    # Get corresponding rules
    rules = activated_rules(fuzzy_values, rule_base)
    # Apply fuzzy implization
    implication_fuzzy_sets = implication(fuzzy_values, rules, output_lv)
    # Apply fuzzy aggregation
    result_fuzzy_set = aggregation(*implication_fuzzy_sets)
    # Get resulting defuzzified value
    crisp_result = defuzzifier.defuzzification(output_lv['U'], result_fuzzy_set, 'mom')
    
    crisp_i = np.argmax(output_lv['U'] >= crisp_result)
    max_p, max_word = -1, None
    
    for term, u in output_lv['terms'].items():
        if u[crisp_i] > max_p:
            max_p = u[crisp_i]
            max_word = term

    return (crisp_result, max_word), result_fuzzy_set

