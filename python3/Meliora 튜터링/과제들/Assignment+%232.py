
# coding: utf-8

# In[41]:

# Number 1
seq="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# seq is my variable
seq_1=seq[0:62] # DNA is cut from 0 to 62
print(seq_1)
file=open("file#1.txt","w+")
# open file#1 for writing and create 
file.write("ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCG")
file.close()


# In[49]:

intron=seq[63:90] # the number of DNA from 63 to 90 is selected
print(intron)
file=open("file#2.txt","w+") 
# open file#2 for writing and create 
file.write("TCGATCGATCGATCGATCGATCATGCT")
file.close()
# Write and Close for all works


# In[50]:

# Number 2(a)
seq_1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2="actgatcgacgatcgatcgatcacgact"
seq_3="ACTGAC-ACTGT-ACTGTA---CATGTG"
# all sequences are my variable
file=open("file#3.fa","w+")
# open file#2 for writing and create 
List=["seq_1","seq_2","seq_3"] 
seq_List=["ATCGTACGATCGATCGATCGCTAGACGTATCG",str(seq_2.upper()),"ACTGAC-ACTGT-ACTGTA---CATGTG"]
# The List is made by divided for each sequence and seq_2 is changed by upper letter.
for i in range (3):
    file.write(">"+str(List[i])+"\n"+str(seq_List[i])+"\n")
file.close()
# Create files, write, and close for all works 



# In[51]:

# Number 2(b)
# making separate files for all given sequence 
seq_1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2="actgatcgacgatcgatcgatcacgact"
seq_3="ACTGAC-ACTGT-ACTGTA---CATGTG"
# all sequences are my variable
file=open("seq_1.fa","w+")

List=["seq_1","seq_2","seq_3"]
seq_List=["ATCGTACGATCGATCGATCGCTAGACGTATCG",str(seq_2.upper()),"ACTGAC-ACTGT-ACTGTA---CATGTG"]
file.write(">"+seq_1[0]+"\n"+seq_2[0])
file.close()


# In[52]:

# here is the same producere as above first cell but the other sequnce to follow
seq_1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2="actgatcgacgatcgatcgatcacgact"
seq_3="ACTGAC-ACTGT-ACTGTA---CATGTG"
# all sequences are my variable
file=open("seq_2.fa","w+")

List=["seq_1","seq_2","seq_3"]
seq_List=["ATCGTACGATCGATCGATCGCTAGACGTATCG",str(seq_2.upper()),"ACTGAC-ACTGT-ACTGTA---CATGTG"]
file.write(">"+seq_2[1]+"\n"+seq_3[1])
file.close()


# In[55]:

# here is the same producere to follow but the other sequence without first and second cell
seq_1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2="actgatcgacgatcgatcgatcacgact"
seq_3="ACTGAC-ACTGT-ACTGTA---CATGTG"
# all sequences are my variable
file=open("seq_3.fa","w+")

List=["seq_1","seq_2","seq_3"]
seq_List=["ATCGTACGATCGATCGATCGCTAGACGTATCG",str(seq_2.upper()),"ACTGAC-ACTGT-ACTGTA---CATGTG"]
file.write(">"+seq_3[2]+"\n"+seq_1[2])
file.close()


# In[38]:

# Number 3 (1)
# trim and write all the sequnce

fileq=open("fileq.txt","r")
file_5=open("file_5.txt","w+")
for line in fileq:
    file_5.write(str(line[14:]))
fileq.close()
file_5.close()


# In[54]:

# Number 3 (2)
# print the length of the trimmed sequnce

file_5=open("file_5.txt","r")
for line in file_5:
    print("The length of the sequence" + str(line) + "is" + str(len(line)+".")

file_5.close()

* I did correctly following the method but I didn't know why syntaxError was shown on the bottle after this box

