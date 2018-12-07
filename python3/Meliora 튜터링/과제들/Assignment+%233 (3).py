
# coding: utf-8

# In[20]:

def my_function(seq, amino_acid):
    seq_1 = seq.upper() # seq makes all letters to be upper letter
    aa = amino_acid.upper() # aa is converted by amino acid and upper letter
    length = len(seq_1) # string number
    
    aa_count=seq_1.count(aa) # total of amino acid 
    aa_content = aa_count/length # amino acid is divided by length
    aa_perc = aa_content*100 # percent is obtained 
    return aa_perc # return means calculation from the result used by all function
    print(aa_perc)

assert my_function("MSRSLLLRFLLFLLLLPPLP","M")==5
assert my_function("MSRSLLLRFLLFLLLLPPLP","r")==10  
assert my_function("msrslllrfllfllllpplp","L")==50 
assert my_function("MSRSLLLRFLLFLLLLPPLP","Y")==0 


# In[22]:

def my_function(seq, amino_acid=["M","L","F","S","Y"]):
    seq_1 = seq.upper() # seq_1 makes all letters to be upper letter
    length = len(seq_1) # string number
    total = 0 # it means starting first number
    for x in amino_acid:
        aa_count=seq_1.count(x) # x in amino_acid is involved within seq_1 count 
        total = aa_count+total # orignal total of aa_count is involved with toral of next(or new) one 
    
    aa_content=total/length # aa equals total of aa is devided by length
    aa_perc = aa_content*100 # percent is obtained 
    return aa_perc # end of function if it is right to work through function
    print(aa_perc)


assert my_function("MSRSLLLRFLLFLLLLPPLP",["M"])==5
assert my_function("MSRSLLLRFLLFLLLLPPLP",["M","L"])==55  
assert my_function("msrslllrfllfllllpplp",["F","S","L"])==70 
assert my_function("MSRSLLLRFLLFLLLLPPLP",["Y"])==65 


# In[23]:

def get_gene(): # get_gene is named
    fl = open("data.csv","r") # fl is maded by file and opens(or read) data.csv 
    for x in fl: # x in fl is selected
        temp = x.rstrip("\n").split(",") # rstrip is removed space(enter) and split is made by the list
        species = temp[0] # colum of first line
        gene = temp[2] # colum of third line
        if species == "Drosophila meLanogaster" or "Drosophila simulans": # only using in Drosophila meLanogaster" or "Drosophila simulans
            print(gene)

get_gene()


# In[29]:

def get_gene_range():  # get_gene_range is named
    fl = open("data.csv","r") # fl is maded by file and opens(or read) data.csv 
    for x in fl: # x in fl is selected
        temp = x.rstrip("\n").split(",") # rstrip is removed space(enter) and split is made by the list
        gene = temp[2] # colum of third line
        seq = temp[1] # colum of second line
        seq_len = len(seq) # length of sequence is gained
        if (seq_len >= 90) or (seq_len < 110) : # seq_len needs to get the range for less than or equal to 90 and grater than 110 
            print(gene)

get_gene_range()


# In[35]:

def get_at(seq): # get_at is named
    """
    This function will count total number of "A" and "T" characters in given string called Seqeunce (seq)
    """
    a_count = seq.upper().count("A") # a letter in seq become upper letter and A is counted
    t_count = seq.upper().count("T") # t letter in seq become upper letter and T is counted
    at_content = (a_count+t_count)/len(seq) # All A and T letters is divided by length
    return at_content  # end of function if it is right to work through function (this should be percentage of a and t apperance)

def get_c(): # get_c is named
    fl = open("data.csv","r") # fl is maded by file and opens(or read) data.csv 
    for x in fl: # x in fl is selected
        temp = x.rstrip("\n").split(",") # rstrip is removed space(enter) and split is made by the list
        seq = temp[1] # colum of second line
        exp = int(temp[3]) # int means possible to read for computer language
        # print(exp) # this is shown by second condition in problem question 
        gene = temp[2] # colum of third line
        # print(get_at(seq)) # this is shown by first condition in problem question 
        if (get_at(seq) < 0.5) and (exp > 200) : # get_at needs to get the range for less than 0.5 and grater than 200
            print(gene)
get_c()


# In[36]:

def get_gene_begin_k_h(): # get_gene_begin_k_h is named
    fl = open("data.csv","r") # fl is maded by file and opens(or read) data.csv 
    for x in fl:
        temp = x.rstrip("\n").split(",") # rstrip is removed space(enter) and split is made by the list
        gene = temp[2] # colum of third line
        gname = temp[0] # colum of first line
        if gene[0] == "h" or gene[0] == "k" : # h or k letter picked in begining gene name on the list
            if not gname == "Drosophila melanogaster": # except Drosophila melanogaster
                print(gene)

get_gene_begin_k_h()


# In[41]:

def get_at2(seq): # get_at2 is named
    """
    This function will count total number of "A" and "T" characters in given string called Seqeunce (seq)
    """
    a_count = seq.upper().count("A") # a letter in seq become upper letter and A is counted
    t_count = seq.upper().count("T") # t letter in seq become upper letter and T is counted
    at_content = (a_count+t_count)/len(seq) # All A and T letters is divided by length
    return at_content # end of function if it is right to work through function (this should be percentage of a and t apperance)

def get_e(): # get_e is named
    fl = open("data.csv","r") # fl is maded by file and opens(or read) data.csv 
    for x in fl:
        temp = x.rstrip("\n").split(",") # rstrip is removed space(enter) and split is made by the list
        seq = temp[1] # colum of second line
        exp = int(temp[3]) # int means possible to read for computer language
        # print(exp) 
        gene = temp[2] # colum of third line
        # print(get_at2(seq)) 
        if (get_at2(seq) > 0.65) : # a and t apperance is greater than 65%
            print(gene + " is High")
        elif (get_at2(seq) < 0.65 and get_at2(seq) > 0.45): # a and t apperance is greater than 45% and less than 65%
            print(gene + " is medium")
        else: # otherwise
            print(gene + " is low")

get_e()

