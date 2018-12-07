
# coding: utf-8

# In[10]:

import re

sample_list = ['Xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']  # here is all given conditions

a_result = []

b_result = []

c_result = []

d_result = []

e_result = []

f_result = []

g_result = []

h_result = []


def A():

    # A condition function

    for value in sample_list:  # iterable

        result = re.search(r'\w+5+\w', value)  # include number of 5

        if result:

            a_result.append(result.group(0))  # return all matched numbers

def B():

    # B condition function

    for value in sample_list:

        result = re.search(".*(d|e).*", value)  # include letter of d or e

        if result:

            b_result.append(result.group(0)) # return all matched letters

def C():

    # C condition function

    for value in sample_list:

        result = re.search('.*d.*e.*', value) # include letters of d and e

        if result:

            c_result.append(result.group(0)) # return all matched letters

def D():

    # D condition function

    for value in sample_list:

        result = re.match(".*(d.e).*", value) # include letters of d and e with a single letter between them

        if result:

            d_result.append(result.group(0)) # return all matched letters

def E():

    # E condition func

    for value in sample_list:

        result = re.search('.*de.*', value) # include both letters of d and e in any order

        if result:

            e_result.append(result.group(0)) # return all matched letters

def F():

    # F condition function

    for value in sample_list:

        result = re.match("^(x|y|X).*", value)  # start x(X) or y

        if result:

            f_result.append(result.group(0)) # return all matched letters

def G():

    # G condition function

    for value in sample_list:

        result = re.search('^(x|y).*e$', value)  # start x or y and end e

        if result:

            g_result.append(result.group(0))  # return all matched letters

def H():

    # H condition function

    for value in sample_list:

        result = re.search('(.*\d){3}', value)  # include numbers 3 or more in a row

        if result:

            h_result.append(result.group(0))  # return all matched letters


# print output all values for each result

A()

print("A condition: ", a_result)

B()

print("B condition: ", b_result)

C()

print("C condition: ", c_result)

D()

print("D condition: ", d_result)

E()

print("E condition: ", e_result)

F()

print("F condition: ", f_result)

G()

print("G condition: ", g_result)

H()

print("H condition: ", h_result)


# In[20]:

import re

f = open("Data.txt", "r") # open the file of Data.txt

data = f.read() # read the file of Data.txt

regex = re.compile('(ANT|ATT|AGT|ACT)(AAT)') # find all given conditions with ANT in front of ATT and include ATT letters

positions = {} # input the letters from the file, this means dictionary method

for matched in regex.findall(data):#[('ATT', 'AAT'), ('ACT', 'AAT')]

    # print all given conditions that ANT in front of ATT and include ATT letters are matched  

    found = ''.join(matched) # for requiring ATT letters attached with ANT and only ANT letters are located in front of ATT

    print(found) # print all given conditions

    positions[matched[0]] = data.index(found) # count the numbers for each condition as counting from 0 to first ATT, from first ACT to second ATT, and second ATT to the end.  

print("Seq1. %s" % positions['ATT']) # cut from the number of 0 to 1139 and count total of number from 0 to 1139 by seq_1

print("Seq2. %s" % (positions['ACT'] - positions['ATT'])) # cut from the number of 1140 to 1624 and count total of number from 1140 to 1624 by seq_2

print("Seq3. %s" % (len(data) - positions['ACT'])) # cut from the number of 1625 to the end and count total of number from 1625 to the end by seq_3


# In[ ]:



