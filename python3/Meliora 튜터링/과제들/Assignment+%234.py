
# coding: utf-8

# In[ ]:

def gene_code():
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    return gencode

def translate_dna(dna_seq):
    """
    This function will take dna_sequence string type parameter
    @dna_seq: (string) combination of dna characters
    @return: (string) the answer of the desired question
    """
    result = ""
    dic = gene_code()             # Variable dic equals a dictionary table 

    # now split input dna sequence into 3 word for each
    while len(dna_seq) >= 3:      # here is iteration until dna_seq to become empty string
        seq = dna_seq[0:3]        # here is codons from nucleotide sequence
        #print("desired: " +seq)  # check if it prints out correctly
        
        if seq not in dic.keys(): # check if sequence exist in the dictionary
            result += "X"         # after above line, checck instead of result from a dictionary table, then put X for indicating not found
            continue              # go back to while loop
        
        dna_seq = dna_seq[3:]     # after all works, update the remaing nucleotide
        
        #print("rest: " + dna_seq)# check if it prints out correctly
        result += dic[seq]        # add the amino acids into the result
    return result

assert translate_dna("ATGTTCGGT") == "MFG"
assert translate_dna("ATCGATCGAT") == "IDR"
assert translate_dna("ACGANCGAT") == "TXD"


# In[ ]:



