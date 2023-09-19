# Calculator for features of proteins
# Author: Celio Dias Santos Junior
# Email: celio.diasjunior@gmail.com
# Date: 07/09/2023 - Sao Carlos, SP/Brazil

# Scales
# average frequencies of amino acids in water soluble proteins
aa_freq = {'A': 0.088, 'C': 0.0205, 'D': 0.0591, 'E': 0.0589,
           'F': 0.0376, 'G': 0.083, 'H': 0.0215, 'I': 0.054,
           'K': 0.0620, 'L': 0.0809, 'M': 0.0197, 'N': 0.0458,
           'P': 0.048, 'Q': 0.0384, 'R': 0.0422, 'S': 0.0650,
           'T': 0.0591, 'V': 0.0705, 'W': 0.0139, 'Y': 0.0352}

# effects of >2-fold variation in aa frequencies
effects = {'K': 'possible nucleoprotein', 'R': 'possible nucleoprotein',
           'C': 'stable of hard folding', 'G': 'stable structure',
           'P': 'stable structure', 'Q': 'stable structure',
           'N': 'stable structure'}
           
# residue MW in Da
aa_mw = {'A': 71.08, 'C': 103.14, 'D': 115.09, 'E': 129.12,
         'F': 147.18, 'G': 57.06, 'H': 137.15, 'I': 113.17,
         'K': 128.18, 'L': 113.17, 'M': 131.21, 'N': 114.11,
         'P': 97.12, 'Q': 128.14, 'R': 156.2, 'S': 87.08,
         'T': 101.11, 'V': 99.14, 'W': 186.21, 'Y': 163.18}

# pKa for different residues EMBOSS scale
pka = {'NT': 8.6, 'CT': 3.6, 'C': 8.5, 'D': 3.9,
       'E': 4.1, 'H': 6.5, 'K': 10.8, 'R': 12.5,
       'Y': 10.1}

# flexibility
bfactors = {'A': 0.25, 'C': 0.208, 'D': 0.875, 'E': 0.833,
            'F': 0.042, 'G': 1, 'H': 0.083, 'I': 0.667,
            'K': 0.708, 'L': 0.292, 'M': 0, 'N': 0.667,
            'P': 0.875, 'Q': 0.792, 'R': 0.958, 'S': 0.875,
            'T': 0.583, 'V': 0.375, 'W': 0.042, 'Y': 0.5}

# antigenicity
parker = {'A': 2.1, 'C': 1.4, 'D': 10, 'E': 7.8,
          'F': -9.2, 'G': 5.7, 'H': 2.1, 'I': -8,
          'K': 5.7, 'L': -9.2, 'M': -4.2, 'N': 7,
          'P': 2.1, 'Q': 6, 'R': 4.2, 'S': 6.5,
          'T': 5.2, 'V': -3.7, 'W': -10, 'Y': -1.9}

kolaskar = {'A': 1.064, 'C': 1.412, 'D': 0.866, 'E': 0.851,
            'F': 1.091, 'G': 0.874, 'H': 1.105, 'I': 1.152,
            'K': 0.93, 'L': 1.25, 'M': 0.826, 'N': 0.776,
            'P': 1.064, 'Q': 1.015, 'R': 0.873, 'S': 1.012,
            'T': 0.909, 'V': 1.383, 'W': 0.893, 'Y': 1.161}

## hydrophobicity scales
# transmembrane domains
kyte_doolitle = {'A': 1.8, 'C': 2.5, 'D': -3.5, 'E': -3.5,
                 'F': 2.8, 'G': -0.40, 'H': -3.20, 'I': 4.5,
                 'K': -3.9, 'L': 3.8, 'M': 1.9, 'N': -3.5,
                 'P': -1.6, 'Q': -3.5, 'R': -4.5, 'S': -0.8,
                 'T': -0.7, 'V': 4.20, 'W': -0.9, 'Y': -1.3}

# antigenic sites prediction using hydrophobicity
hopp_woods = {'A': -0.5, 'C': -1, 'D': 3, 'E': 3,
              'F': -2.5, 'G': 0, 'H': -0.5, 'I': -1.8,
              'K': 3, 'L': -1.8, 'M': -1.3, 'N': 0.2,
              'P': 0, 'Q': 0.2, 'R': 3, 'S': 0.3,
              'T': -0.4, 'V': -1.5, 'W': -3.4, 'Y': -2.3}

# alpha-helixes
cornette = {'A': 0.2, 'C': 4.1, 'D': -3.10, 'E': -1.8,
            'F': 4.4, 'G': 0, 'H': 0.5, 'I': 4.8,
            'K': -3.1, 'L': 5.7, 'M': 4.2, 'N': -0.5,
            'P': -2.2, 'Q': -2.8, 'R': 1.4, 'S': -0.5,
            'T': -1.9, 'V': 4.7, 'W': 1, 'Y': 3.2}

# normalized
eisenberg = {'I': 1.38, 'F': 1.19, 'V': 1.08, 'L': 1.06,
             'W': 0.81, 'M': 0.64, 'A': 0.62, 'G': 0.48,
             'C': 0.29, 'Y': 0.26, 'P': 0.12, 'T': -0.05,
             'S': -0.18, 'H': -0.4, 'E': -0.74, 'N': -0.78,
             'Q': -0.85, 'D': -0.9, 'K': -1.5, 'R': -2.53}

# surface accessibility
rose = {'A': 0.74, 'C': 0.91, 'D': 0.62, 'E': 0.62,
        'F': 0.88, 'G': 0.72, 'H': 0.78, 'I': 0.88,
        'K': 0.52, 'L': 0.85, 'M': 0.85, 'N': 0.63,
        'P': 0.64, 'Q': 0.62, 'R': 0.64, 'S': 0.66,
        'T': 0.7, 'V': 0.86, 'W': 0.85, 'Y': 0.76}

# globular proteins
janin = {'A': 0.30, 'C': 0.90, 'D': -0.6, 'E': -0.7,
         'F': 0.5, 'G': 0.3, 'H': -0.1, 'I': 0.7,
         'K': -1.8, 'L': 0.5, 'M': 0.4, 'N': -0.5,
         'P': -0.3, 'Q': -0.7, 'R': -1.4, 'S': -0.1,
         'T': -0.2, 'V': 0.6, 'W': 0.3, 'Y': -0.4}

# transmembrane domains
engelman = {'A': 1.6, 'C': 2, 'D': -9.2, 'E': -8.2,
            'F': 3.7, 'G': 1, 'H': -3, 'I': 3.1,
            'K': -8.8, 'L': 2.8, 'M': 3.4, 'N': -4.8,
            'P': -0.2, 'Q': -4.1, 'R': -12.3, 'S': 0.6,
            'T': 1.2, 'V': 2.6, 'W': 1.9, 'Y': -0.7}

## specific volume ml/g
specific_volume = {'A': 0.748, 'C': 0.631, 'D': 0.579, 'E': 0.643,
                   'F': 0.774, 'G': 0.632, 'H': 0.67, 'I': 0.884,
                   'K': 0.789, 'L': 0.884, 'M': 0.745, 'N': 0.619,
                   'P': 0.774, 'Q': 0.674, 'R': 0.666, 'S': 0.613,
                   'T': 0.689, 'V': 0.847, 'W': 0.734, 'Y': 0.712}

## boman
boman_scale = {'L': -4.92, 'I': -4.92, 'V': -4.04, 'F': -2.98, 'M': -2.35, 'W': -2.33, 'A': -1.81, 'C': -1.28,
               'G': -0.94, 'Y': 0.14, 'T': 2.57, 'S': 3.40, 'H': 4.66, 'Q': 5.54, 'K': 5.55, 'N': 6.64, 'E': 6.81,
               'D': 8.72, 'R': 14.92, 'P': 0., 'X': 0.}


instability = {
            'A': {'A': 1.0, 'C': 44.94, 'E': 1.0, 'D': -7.49, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': -7.49, 'K': 1.0,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 1.0, 'P': 20.26, 'S': 1.0, 'R': 1.0, 'T': 1.0, 'W': 1.0, 'V': 1.0,
                  'Y': 1.0, 'X': 0.},
            'C': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 20.26, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 33.6, 'K': 1.0,
                  'M': 33.6, 'L': 20.26, 'N': 1.0, 'Q': -6.54, 'P': 20.26, 'S': 1.0, 'R': 1.0, 'T': 33.6, 'W': 24.68,
                  'V': -6.54, 'Y': 1.0, 'X': 0.},
            'E': {'A': 1.0, 'C': 44.94, 'E': 33.6, 'D': 20.26, 'G': 1.0, 'F': 1.0, 'I': 20.26, 'H': -6.54, 'K': 1.0,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 20.26, 'P': 20.26, 'S': 20.26, 'R': 1.0, 'T': 1.0, 'W': -14.03,
                  'V': 1.0, 'Y': 1.0, 'X': 0.},
            'D': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': 1.0, 'F': -6.54, 'I': 1.0, 'H': 1.0, 'K': -7.49,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 1.0, 'P': 1.0, 'S': 20.26, 'R': -6.54, 'T': -14.03, 'W': 1.0,
                  'V': 1.0, 'Y': 1.0, 'X': 0.},
            'G': {'A': -7.49, 'C': 1.0, 'E': -6.54, 'D': 1.0, 'G': 13.34, 'F': 1.0, 'I': -7.49, 'H': 1.0, 'K': -7.49,
                  'M': 1.0, 'L': 1.0, 'N': -7.49, 'Q': 1.0, 'P': 1.0, 'S': 1.0, 'R': 1.0, 'T': -7.49, 'W': 13.34,
                  'V': 1.0, 'Y': -7.49, 'X': 0.},
            'F': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 13.34, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 1.0, 'K': -14.03,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 1.0, 'P': 20.26, 'S': 1.0, 'R': 1.0, 'T': 1.0, 'W': 1.0, 'V': 1.0,
                  'Y': 33.601, 'X': 0.},
            'I': {'A': 1.0, 'C': 1.0, 'E': 44.94, 'D': 1.0, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 13.34, 'K': -7.49,
                  'M': 1.0, 'L': 20.26, 'N': 1.0, 'Q': 1.0, 'P': -1.88, 'S': 1.0, 'R': 1.0, 'T': 1.0, 'W': 1.0,
                  'V': -7.49, 'Y': 1.0, 'X': 0.},
            'H': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': -9.37, 'F': -9.37, 'I': 44.94, 'H': 1.0, 'K': 24.68,
                  'M': 1.0, 'L': 1.0, 'N': 24.68, 'Q': 1.0, 'P': -1.88, 'S': 1.0, 'R': 1.0, 'T': -6.54, 'W': -1.88,
                  'V': 1.0, 'Y': 44.94, 'X': 0.},
            'K': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': -7.49, 'F': 1.0, 'I': -7.49, 'H': 1.0, 'K': 1.0,
                  'M': 33.6, 'L': -7.49, 'N': 1.0, 'Q': 24.64, 'P': -6.54, 'S': 1.0, 'R': 33.6, 'T': 1.0, 'W': 1.0,
                  'V': -7.49, 'Y': 1.0, 'X': 0.},
            'M': {'A': 13.34, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 58.28, 'K': 1.0,
                  'M': -1.88, 'L': 1.0, 'N': 1.0, 'Q': -6.54, 'P': 44.94, 'S': 44.94, 'R': -6.54, 'T': -1.88, 'W': 1.0,
                  'V': 1.0, 'Y': 24.68, 'X': 0.},
            'L': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 1.0, 'K': -7.49, 'M': 1.0,
                  'L': 1.0, 'N': 1.0, 'Q': 33.6, 'P': 20.26, 'S': 1.0, 'R': 20.26, 'T': 1.0, 'W': 24.68, 'V': 1.0,
                  'Y': 1.0, 'X': 0.},
            'N': {'A': 1.0, 'C': -1.88, 'E': 1.0, 'D': 1.0, 'G': -14.03, 'F': -14.03, 'I': 44.94, 'H': 1.0, 'K': 24.68,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': -6.54, 'P': -1.88, 'S': 1.0, 'R': 1.0, 'T': -7.49, 'W': -9.37,
                  'V': 1.0, 'Y': 1.0, 'X': 0.},
            'Q': {'A': 1.0, 'C': -6.54, 'E': 20.26, 'D': 20.26, 'G': 1.0, 'F': -6.54, 'I': 1.0, 'H': 1.0, 'K': 1.0,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 20.26, 'P': 20.26, 'S': 44.94, 'R': 1.0, 'T': 1.0, 'W': 1.0,
                  'V': -6.54, 'Y': -6.54, 'X': 0.},
            'P': {'A': 20.26, 'C': -6.54, 'E': 18.38, 'D': -6.54, 'G': 1.0, 'F': 20.26, 'I': 1.0, 'H': 1.0, 'K': 1.0,
                  'M': -6.54, 'L': 1.0, 'N': 1.0, 'Q': 20.26, 'P': 20.26, 'S': 20.26, 'R': -6.54, 'T': 1.0, 'W': -1.88,
                  'V': 20.26, 'Y': 1.0, 'X': 0.},
            'S': {'A': 1.0, 'C': 33.6, 'E': 20.26, 'D': 1.0, 'G': 1.0, 'F': 1.0, 'I': 1.0, 'H': 1.0, 'K': 1.0, 'M': 1.0,
                  'L': 1.0, 'N': 1.0, 'Q': 20.26, 'P': 44.94, 'S': 20.26, 'R': 20.26, 'T': 1.0, 'W': 1.0, 'V': 1.0,
                  'Y': 1.0, 'X': 0.},
            'R': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': -7.49, 'F': 1.0, 'I': 1.0, 'H': 20.26, 'K': 1.0,
                  'M': 1.0, 'L': 1.0, 'N': 13.34, 'Q': 20.26, 'P': 20.26, 'S': 44.94, 'R': 58.28, 'T': 1.0, 'W': 58.28,
                  'V': 1.0, 'Y': -6.54, 'X': 0.},
            'T': {'A': 1.0, 'C': 1.0, 'E': 20.26, 'D': 1.0, 'G': -7.49, 'F': 13.34, 'I': 1.0, 'H': 1.0, 'K': 1.0,
                  'M': 1.0, 'L': 1.0, 'N': -14.03, 'Q': -6.54, 'P': 1.0, 'S': 1.0, 'R': 1.0, 'T': 1.0, 'W': -14.03,
                  'V': 1.0, 'Y': 1.0, 'X': 0.},
            'W': {'A': -14.03, 'C': 1.0, 'E': 1.0, 'D': 1.0, 'G': -9.37, 'F': 1.0, 'I': 1.0, 'H': 24.68, 'K': 1.0,
                  'M': 24.68, 'L': 13.34, 'N': 13.34, 'Q': 1.0, 'P': 1.0, 'S': 1.0, 'R': 1.0, 'T': -14.03, 'W': 1.0,
                  'V': -7.49, 'Y': 1.0, 'X': 0.},
            'V': {'A': 1.0, 'C': 1.0, 'E': 1.0, 'D': -14.03, 'G': -7.49, 'F': 1.0, 'I': 1.0, 'H': 1.0, 'K': -1.88,
                  'M': 1.0, 'L': 1.0, 'N': 1.0, 'Q': 1.0, 'P': 20.26, 'S': 1.0, 'R': 1.0, 'T': -7.49, 'W': 1.0,
                  'V': 1.0, 'Y': -6.54, 'X': 0.},
            'Y': {'A': 24.68, 'C': 1.0, 'E': -6.54, 'D': 24.68, 'G': -7.49, 'F': 1.0, 'I': 1.0, 'H': 13.34, 'K': 1.0,
                  'M': 44.94, 'L': 1.0, 'N': 1.0, 'Q': 1.0, 'P': 13.34, 'S': 1.0, 'R': -15.91, 'T': -7.49, 'W': -9.37,
                  'V': 1.0, 'Y': 13.34, 'X': 0.},
            'X': {'A': 0., 'C': 0., 'E': 0., 'D': 0., 'G': 0., 'F': 0., 'I': 0., 'H': 0., 'K': 0.,
                  'M': 0., 'L': 0., 'N': 0., 'Q': 0., 'P': 0., 'S': 0., 'R': 0., 'T': 0., 'W': 0.,
                  'V': 0., 'Y': 0., 'X': 0.}}

# Transform the above into a simpler-to-use form, a single dictionary that maps dimers
instability2 = {}
for k,vs in instability.items():
    for k2,v in vs.items():
        if v:
            instability2[k+k2] = v

def calc_aafreq(seq):
    seq = seq.upper()
    aas = list(aa_freq)
    aafreqs = [seq.count(x) / len(seq) for x in aas]
    aaprop = [aafreqs[idx] / aa_freq.get(x) for idx, x in enumerate(aas)]
    print('Amino acid\tfold-change from average water sol. proteins\teffect')
    for idx, x in enumerate(aaprop):
        if x > 2:
            print(f'{aas[idx]}\t{x:.2f}\t{effects.get(aas[idx], "")}')

def mw(seq, verbose=True):
    seq = seq.upper()
    total = sum(aa_mw.get(x, 0) for x in seq)
    total /= 1000
    if verbose:
        print(f'The molecular weight = {total:.2f} kDa')
    else:
        return total

def prot_charge(seq, pH=7.0, verbose=True):
    def form(pKa, pH, ch='+'):
        if ch == '+': return 1/1+(10**(pH - pKa))
        else: return -1/1+(10**(pKa - pH)) 
    
    seq = seq.upper()
    neg = ['D', 'E']
    pos = ['C', 'H', 'R', 'K', 'Y']
    charge = sum(form(pka.get(x, 0), pH, '+') for x in seq if x in pos)
    charge += sum(form(pka.get(x, 0), pH, '-') for x in seq if x in neg)
    charge += form(pka.get('NT', 0), pH, '+')
    charge += form(pka.get('CT', 0), pH, '-')
    if verbose:
        print(f'at pH = {pH}, charge = {charge:.2f}')
    else:
        return charge


def pI(seq, verbose=True):
    seq = seq.upper()
    pHs = [x/100 for x in range(0, 1401)]
    chs = [prot_charge(seq, x, False) for x in pHs]
    isolectric = pHs[chs.index(min(chs))]
    if verbose:
        print(f'pI = {isolectric:.2f}')
    else:
        return isolectric


def mol_extinc(seq, verbose=True):
    seq = seq.upper()
    tyr = seq.count('Y')
    trp = seq.count('W')
    cys = seq.count('C')
    cystine = cys // 2
    e1 = (tyr * 1490) + (trp * 5500) + (cystine * 125)
    e2 = (tyr * 1490) + (trp * 5500)
    if verbose:
        print(f'Not considering cystines, E = {e2:.2f} L/mol.cm')
        print(f'Considering cystines, E = {e1:.2f} L/mol.cm')
    else:
        return (e1, e2)


def profile(seq, scale, output=False, window=5):
    def avg(mlist):
        return sum(mlist) / len(mlist)
    convseq = [scale.get(x, 0) for x in seq.upper()] 
    ws = [convseq[idx: idx+window] for idx in range(len(convseq))]
    ws = [avg(x) for x in ws]
    ws = [(idx, x) for idx, x in enumerate(ws)]
    threshold = avg(convseq)
    if output:
        with open(output, 'w') as ofile:
            ofile.write(f'# Average threshold: {threshold:.2f}\n')
            ofile.write('Residue\tWindow Avg.\n')
            for idx, x in ws:
                ofile.write(f'{idx}\t{x}\n')
    else:
        return ws, threshold
    
 
def antigenicity(seq, window_size=8, verbose=True):
    antigenic_segments = [] 
    threshold = sum(kolaskar.get(x) for x in seq)/len(seq) 
    if threshold > 1.05: threshold = 1.05
    for i in range(len(seq) - window_size + 1):
        window = seq[i:i + window_size]
        antigenic_score = 0.0
        # Calculate antigenic propensity score for the window
        for j in range(window_size):
            amino_acid = window[j]
            if amino_acid in kolaskar:
                antigenic_score += kolaskar[amino_acid]
        antigenic_score /= window_size
        if antigenic_score >= threshold:
            start = i
            end = i + window_size - 1
            fragment = seq[start:end+1]
            antigenic_segments.append((start+1, end+1, fragment, antigenic_score))
    if verbose:
         print(f'Antigenicity by Kolaskar')
         print(f'Threshold: {threshold}, Window_size: {window_size}')
         print('START\tSTOP\tFRAGMENT\tANTIGENIC SCORE')
         for a, b, c, d in antigenic_segments:
             print(f'{a}\t{b}\t{c}\t{d:.2f}')
    else:
         return antigenic_segments


def hydrophobicity(seq, scale='KD', verbose=True):
     # defining scales
     scales = {'KD': kyte_doolitle,
               'HW': hopp_woods,
               'COR': cornette,
               'EIN': eisenberg,
               'ROS': rose,
               'JAN': janin,
               'ENG': engelman}
     scale = scales[scale]
     _, threshold = profile(seq, scale)
     if verbose:
         print(f'Avg. hydrophobicity = {threshold:.2f}')
     else:
         return threshold


def solubility(seq, verbose=True):
    AH = hydrophobicity(seq, 'KD', verbose=False)
    RH = sum(1 for x in seq if x not in ['K', 'R', 'D', 'E', 'H'])
    RH /= sum(1 for x in seq if x in ['K', 'R', 'D', 'E', 'H'])
    LIND = (sum(1 for x in seq if x in ['K', 'R', 'D', 'E', 'H']) + 2) / len(seq)
    sol = RH + LIND - (0.05*AH)   
    if verbose:
        if sol < 1.1: print(f'Solubility = {sol:.2f}\tInsoluble')
        elif sol > 2.5: print(f'Solubility = {sol:.2f}\tUnstructured')
        else: print(f'Solubility = {sol:.2f}\tSoluble')
    else:
        return (AH, RH, LIND, sol)         


def radius(seq, verbose=True):
    weight = mw(seq, verbose=False)*1000
    length = len(seq)
    dg = 0.41*(weight**0.5)
    d = 3.875*(length**0.333)
    if verbose:
        print(f'Gyration radius = {dg:.2f}°, Radius = {d:.2f}°')
    else:
        return (g, dg)
        

def sp_vol(seq, verbose=True):
    seq = seq.upper()
    freqs = [seq.count(x) / len(seq) for x in specific_volume]
    sps = list(specific_volume.values())
    freqs = [k*v for k, v in zip(freqs, sps)]
    psv = sum(freqs)
    if verbose:
        print(f'Specific volume = {psv:.3f} mL/g')
    else:
        return psv
    

def pckg_vol(seq, verbose=True):
    # approx.
    weight = mw(seq, verbose=False) * 1000
    VP = 1.245 * weight
    if verbose:
        print(f'Packed volume = {VP:.2f} A^3')
    else:
        return VP


def instability_index(seq, verbose=True):
    seq = seq.upper()
    II = 0
    idx = 0
    while (idx+2) < len(seq):
        kmer = seq[idx : idx+2]
        II += instability2[kmer]
        idx += 1
    II *= 10
    II /= len(seq)
    if verbose:
        print(f'Instability index = {II:.2f}')
    else:
        return II


def aliphatic_index(seq, verbose=True):
    AAAs = {'A': 1, 'V': 2.9, 'I': 3.9, 'L': 3.9}
    seq = seq.upper()
    AI = 0
    for k, v in AAAs.items():        
        AI += seq.count(k) * v
    if verbose:
        print(f'Aliphatic index = {AI:.2f}')
    else:
        return AI
        
        
def boman_index(seq, verbose=True):
    seq = seq.upper()
    boman = [boman_scale.get(x, 0) for x in seq]
    boman = sum(boman) / len(seq)
    if verbose:
        print(f'Boman index = {boman:.2f}')
    else:
        return boman
        

def motif_finder(motif, seq, output=False, verbose=True):
    import re
    results = re.finditer(motif, seq)
    test = []
    for x in results:
        coords = x.span()
        test.append((coords[0], coords[1], x.group()))
    if output:
        with open(output, 'w') as ofile:
            ofile.write('START\tSTOP\tMATCH\n')
            for sta, sto, mat in test:
                ofile.write(f'{sta}\t{sto}\t{mat}\n')
    if verbose:
        print(f'START\tSTOP\tMATCH')
        for sta, sto, mat in test:
            print(f'{sta}\t{sto}\t{mat}')
    else:
        return test


def hmoment(seq, angle = 100, window = 11, verbose = True):
    '''
    # http://emboss.bioinformatics.nl/cgi-bin/emboss/hmoment
    # SEQUENCE: FLPVLAGLTPSIVPKLVCLLTKKC
    # ALPHA-HELIX ANGLE=100 : 0.52
    # BETA-SHEET  ANGLE=160 : 0.271
    # 
    # ALPHA HELIX VALUE
    # hmoment(seq = "FLPVLAGLTPSIVPKLVCLLTKKC", angle = 100, window = 11)
    # 0.5199226
    # 
    # BETA SHEET VALUE
    # hmoment(seq = "FLPVLAGLTPSIVPKLVCLLTKKC", angle = 160, window = 11)
    # 0.2705906
    '''
    import numpy as np
    wdw = min(window, len(seq))  # if sequence is shorter than window, take the whole sequence instead
    mtrx = np.array([eisenberg[aa] for aa in seq], dtype=np.float64)  #[::-1]
    mwdw = np.array([mtrx[i:i + wdw] for i in range(len(mtrx) - wdw + 1)])
    rads = angle * (np.pi / 180) * np.arange(wdw)  # calculate actual moment (radial)
    vcos = np.dot(mwdw, np.cos(rads))
    vsin = np.dot(mwdw, np.sin(rads))
    # The code below is optimized to avoid copies
    vcos **= 2.
    vsin **= 2.
    moms = vsin
    moms += vcos
    moment = np.sqrt(moms.max()) / wdw
    if verbose:
         print(f'at {angle}° and window of {window} residues, H-moment = {moment:.2f}')
    else:
        return moment


def main(seq):
    calc_aafreq(seq)
    print('\n')
    mw(seq, verbose=True)
    print('\n')
    prot_charge(seq, pH=7.0, verbose=True)
    print('\n')
    pI(seq, verbose=True)
    print('\n')
    mol_extinc(seq, verbose=True)
    print('\n')
    for scale_name, scale in [('flexibility_bfactors', bfactors),
                              ('antigenicity_parker', parker),
                              ('antigenicity_kolaskar', kolaskar),
                              ('hydrophobicity_KD', kyte_doolitle),
                              ('hydrophobicity_hopp_woods', hopp_woods),
                              ('hydrophobicity_cornette', cornette),
                              ('hydrophobicity_eisenberg', eisenberg),
                              ('hydrophobicity_rose', rose),
                              ('hydrophobicity_janin', janin),
                              ('hydrophobicity_engelman', engelman)]:
        print(f'Calculating profile for the scale {scale_name}')    
        profile(seq, scale, output=f'profile_{scale_name}.tsv', window=5)
    print('\n')
    antigenicity(seq, 8, True)
    print('\n')
    hydrophobicity(seq, scale='KD', verbose=True)
    print('\n')
    solubility(seq, verbose=True)
    print('\n')
    radius(seq, verbose=True)
    print('\n')
    sp_vol(seq, verbose=True)
    print('\n')
    pckg_vol(seq, verbose=True)
    print('\n')
    instability_index(seq, verbose=True)
    print('\n')
    aliphatic_index(seq, verbose=True)
    print('\n')
    boman_index(seq, verbose=True)
    print('\n')
    hmoment(seq, angle=100, window=11, verbose=True)
    print('\nSearching for patterns, in this case V[AKL]')
    motif_finder(r'V[AKL]', seq, output=False, verbose=True)


if __name__ == '__main__':
    seq = 'VLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRFKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAGGAMNKALELFRKDIAAKYKELGYQG'
    main(seq)
        
