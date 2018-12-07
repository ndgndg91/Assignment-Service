import re


class Assignment7:
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    gencode = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    def __init__(self, sequence=None, species=None, gene_name=None):
        if sequence is None and species is None and gene_name is None:
            self.sequence = "ACTGATCGTTACGTACGAGTCAT"
            self.species = "Drosphila melanogaster"
            self.gene_name = "ABC1"
        else:
            self.sequence = sequence
            self.species = species
            self.gene_name = gene_name

    def len_of_sequence(self):
        return len(self.sequence)

    def translate_to_amino(self):

        last_codon_start = len(self.sequence) - 2
        protein = ""
        # =======================================================================================
        for start in [num for num in range(0, last_codon_start, 3)]:  # using list comprehension ==
            # =======================================================================================
            codon = self.sequence[start:start + 3]
            aa = Assignment7.gencode.get(codon, 'X')
            protein = protein + aa
        return protein

    def get_complement(self):
        return_val = ""
        for c in self.sequence:
            return_val += Assignment7.complement[c]
        return return_val

    def get_cg_gc(self):
        searched = re.findall(r"GC|CG", self.sequence)
        count = len(searched)
        return str((count / self.len_of_sequence()) * 100)

    def restriction_enzyme(self):
        searched = re.findall(r"A[ATGC]TAAT", self.sequence)
        return len(searched)


a = Assignment7();
print(a.species)
print(a.sequence)
print(a.gene_name)
print("translate : " + a.translate_to_amino())
print("complement : " + a.get_complement())
print(a.get_cg_gc() + "%")
print(a.restriction_enzyme())
# b = Assignment7("asdsdf", "dfkweri sdf", "DD2")
# print(b.sequence)
# print(b.species)
# print(b.gene_name)




import re  # 정규식 모듈 임포드


class Assignment7:  # 클래스 정의
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}  # 클래스 변수 사전 complement 정의
    gencode = {  # 클래스 변수 사전 genecode 정의
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    def __init__(self, sequence=None, species=None, gene_name=None):  # constructor 정의
        if sequence is None and species is None and gene_name is None:  # 객체 생성시 매개변수를 받지 않으면 디폴트값으로 객체 변수를  가짐
            self.sequence = "ACTGATCGTTACGTACGAGTCAT"
            self.species = "Drosphila melanogaster"
            self.gene_name = "ABC1"
        else:  # 객체 생성시 매개변수를 받는 다면 받은 매개변수로 객체변수를 가짐
            self.sequence = sequence
            self.species = species
            self.gene_name = gene_name

    def len_of_sequence(self):  # 시퀀스의 길이를 구하는 메소드
        return len(self.sequence)

    def translate_to_amino(self):

        last_codon_start = len(self.sequence) - 2
        protein = ""
        # =======================================================================================
        for start in [num for num in range(0, last_codon_start, 3)]:  # using list comprehension == 시퀀스를 3글자 단위로 자르는 리스트
            # =======================================================================================
            codon = self.sequence[start:start + 3]  # 세글자 단위로 잘라서 codon에 저장
            aa = Assignment7.gencode.get(codon, 'X')  # 클래스 변수 genecode에서  codon을 키값으로 value값을 찾아서 가져옴 , 없을 경우 'X'를 반환
            protein = protein + aa  # protein 변수에 누적
        return protein

    def get_complement(self):
        return_val = ""
        for c in self.sequence:  # 시퀀스를 문자 하나씩 접근해서 클래스 변수 complement에 키값으로 접근해서 value값을 차례대로 가져오면서 return_val에 누적
            return_val += Assignment7.complement[c]
        return return_val

    def get_cg_gc(self):
        searched = re.findall(r"GC|CG", self.sequence)  # 시퀀스에서 GC 또는 CG가 포함 되어있다면 count list에 넣음
        count = len(searched)  # CG 또는 GC 가 들어있는 리스트의 길이 즉 ㄴ개수를 구함
        return str((count / self.len_of_sequence()) * 100)  # 퍼센트를 구함

    def restriction_enzyme(self):
        searched = self.sequence.split(re.search(r"A[ATGC]TAAT", self.sequence))  # 시퀀스를 해당 정규식에 맞게 잘라서 리스트로 반환
        # print(searched)
        for x in searched:  # for문을 이용해 리스트에 각각 접근하여 길이를 반환
            return (len(x))


a = Assignment7()  # 객체 a를 생성
print(a.species)  # a의 객체 변수는 디폴트값
print(a.sequence)  # a의 객체 변수 디폴트값
print(a.gene_name)  # a의 객체 변수 디폴트값
print("translate : " + a.translate_to_amino())  # 메소드 호출
print("complement : " + a.get_complement())  # 메소드 호출
print(a.get_cg_gc() + "%")  # 메소드 호출
print(a.restriction_enzyme())  # 메소드 호출

import re  # regular express begins


class Assignment7:  # class definition
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    gencode = {  # class variable dictionary definition
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    def __init__(self, sequence=None, species=None, gene_name=None):  # constructor definition
        if sequence is None and species is None and gene_name is None:  # when object is created and it isn't received by parameter, a value of default would be received by object
            self.sequence = "ACTGATCGTTACGTACGAGTCAT"
            self.species = "Drosphila melanogaster"
            self.gene_name = "ABC1"
        else:  # if parameter is received when it is made by an object, an object variable as an unrecognized variable would be received
            self.sequence = sequence
            self.species = species
            self.gene_name = gene_name

    def len_of_sequence(self):  # the length of sequence should be found
        return len(self.sequence)

    def translate_to_amino(self):

        last_codon_start = len(self.sequence) - 2
        protein = ""
        # =======================================================================================
        for start in [num for num in range(0, last_codon_start,
                                           3)]:  # using list comprehension == # the three letters should be cut from the given sequence
            # =======================================================================================
            codon = self.sequence[start:start + 3]  # the three cut letters moves to the codon and then they are saved
            aa = Assignment7.gencode.get(codon, 'X')  # class variable numbering
            protein = protein + aa  # protein variable numbering and accumulate multiples
        return protein

    def get_complement(self):
        return_val = ""
        for c in self.sequence:  # each letter should approach into sequence in order to gain the value of the class variable's complement; each value, in order, moves to return_val
            return_val += Assignment7.complement[c]
        return return_val

    def get_cg_gc(self):
        searched = re.findall(r"GC|CG",
                              self.sequence)  # both letters of CG or GC should be found in the list; the length in between should be counted.
        count = len(searched)
        return str((
                   count / self.len_of_sequence()) * 100)  # the value of % is found; percentage of length over entire sequence

    def restriction_enzyme(self):
        searched = self.sequence.split(
            re.search(r"A[ATGC]TAAT", self.sequence))  # the sequence of interest should be matched with regular express
        # print(searched)
        for x in searched:  # the length in the list should be converted using "for loop"
            return (len(x))


a = Assignment7();  # an object of "a" would be created
print(a.species)  # an object of "a" is variable
print(a.sequence)  # an object of "a" is variable
print(a.gene_name)  # an object of "a" is variable
print("translate : " + a.translate_to_amino())  # a method is called
print("complement : " + a.get_complement())  # a method is called
print(a.get_cg_gc() + "%")  # a method is called
print(a.restriction_enzyme())  # a method is called
