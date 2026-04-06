
data = [
    {'R': 'No',  'T': 'Yes', 'A': 'Yes'},
    {'R': 'No',  'T': 'No',  'A': 'No'},
    {'R': 'Yes', 'T': 'Yes', 'A': 'Yes'},
    {'R': 'Yes', 'T': 'No',  'A': 'No'},
    {'R': 'No',  'T': 'Yes', 'A': 'No'},
    {'R': 'Yes', 'T': 'Yes', 'A': 'Yes'},
    {'R': 'Yes', 'T': 'No',  'A': 'Yes'},
    {'R': 'No',  'T': 'No',  'A': 'No'}
]

def calculate_cpt(data, child, parents):
    cpt = {}
    for row in data:
        
        parent_state = tuple(row[p] for p in parents)
        child_state = row[child]
        
        if parent_state not in cpt:
            cpt[parent_state] = {}
        cpt[parent_state][child_state] = cpt[parent_state].get(child_state, 0) + 1
        
    
    for state in cpt:
        total = sum(cpt[state].values())
        for child_val in cpt[state]:
            cpt[state][child_val] /= total
    return cpt


cpt_t_r = calculate_cpt(data, 'T', ['R'])

cpt_a_t = calculate_cpt(data, 'A', ['T'])


evidence_rain = 'Yes'

prob_late = 0
for t_state in ['Yes', 'No']:
    
    p_t_given_r = cpt_t_r[(evidence_rain,)].get(t_state, 0)
    
   
    p_a_given_t = cpt_a_t[(t_state,)].get('Yes', 0)
    
    
    prob_late += p_a_given_t * p_t_given_r

print(f"Probability of Arriving Late given Rain: {prob_late:.2f}")
print(f"Probability of Not Arriving Late given Rain: {1 - prob_late:.2f}")
