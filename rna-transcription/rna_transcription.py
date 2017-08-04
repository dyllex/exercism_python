"""
I had a lot of trouble with this exercise.
Would really appreciate any advice/tips. 
Thanks!
"""

def to_rna(dna):

    rna = []
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    for base in dna:
        if base in 'GCAT':
            rna += dna_to_rna[base]
        else:
            return ''

    return ''.join(rna)
