import re

file = open('Data.txt', 'r')
dna_txt = file.read()
r_enzyme = re.compile(r'(A[AGCT]T).*(AAT)')
r_enzyme2 = re.compile(r'(GC[AG][AT]).*(TG)')
matched_iter = r_enzyme.finditer(dna_txt)
print(matched_iter)
for matched in matched_iter:
    print(matched.start(), dna_txt[matched.start()], dna_txt[matched.start() + 1], dna_txt[matched.start() + 2])
    print(matched.end(), dna_txt[matched.end() - 3], dna_txt[matched.end() - 2], dna_txt[matched.end() - 1])
    print(matched.group(1))
    print(matched.group(2))
    print(matched.groups())
    print("중간에 들어가는 문자열길이 : ", (matched.end() - 4) - (matched.start() + 2))

matched_iter2 = r_enzyme2.finditer(dna_txt)
print(matched_iter)
for matched in matched_iter2:
    print(matched.start(), dna_txt[matched.start()], dna_txt[matched.start() + 1], dna_txt[matched.start() + 2],
          dna_txt[matched.start() + 3])
    print(matched.end(), dna_txt[matched.end() - 2], dna_txt[matched.end() - 1])
    print(matched.group(1))
    print(matched.group(2))
    print(matched.groups())
    print("중간에 들어가는 문자열길이 : ", (matched.end() - 3) - (matched.start() + 3))

test = 'AATCCCCCCCCCCAAT'
r_test = re.compile(r'(AAT).*(AAT)')
t_matched = r_test.finditer(test)
for matched in t_matched:
    print(matched.start())
    print(matched.end(), test[15])
    print(matched.group(1))
    print(matched.group(2))
    print(matched.groups())
    print("중간에 들어가는 문자열길이 : ", (matched.end() - 4) - (matched.start() + 2))  # 12 - 2 = 10
    print(test[matched.start() + 3:matched.end() - 3])  # 3:13
    print(len(test[matched.start() + 3:matched.end() - 3]))  # 3:13



# import re
#
# file = open('Data.txt', 'r')
# dna_txt = file.read()
# a = re.compile(r'(ACGT)')
# matched = a.findall(dna_txt)
# print(len(matched))