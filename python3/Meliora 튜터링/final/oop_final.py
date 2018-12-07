import re  # 정규식 모듈 임포트


class Digest:  # 클래스 정의
    f = 'Data.txt'  # 클래스 변수정의

    def __init__(self, file=None):  # 생성자 정의
        if file is None:  # 객체 생성시 file매개변수값을 받지 않으면 객체file변수에는 클래스변수를 넣음
            self.file = Digest.f
        else:  # 객체 생성시 file 매개변수를 받는다면 받은 매개변수를 객체변수로 지정
            self.file = file

    def abc1(self):  # abc1메소드 정의
        dna = open(self.file).read().rstrip("\n")  # 자신의 객체변수로 지정한 파일을 읽어서 문자열변수에 담음
        all_possible_cut_sites = [0]  # 리스트 생성

        for match in re.finditer(r"A[ATGC]TAAT", dna):  # 정규식 패턴을 이용하여 문자열을 찾음
            all_possible_cut_sites.append(match.start() + 3)  # 찾은 문자열의 3번째 자리의 인덱스를 리스트에 넣음

            print(all_possible_cut_sites)
            print("_______")

        all_possible_cut_sites.append(len(dna))  # 문자열의 총길이를 리스트에 넣음
        print("***********")
        print(all_possible_cut_sites)

        for i in range(1, len(all_possible_cut_sites)):  # 리스트 멤버에 2번째 멤버부터 각각 접근해서 길이를 구해줌
            this_cut_position = all_possible_cut_sites[i]
            previous_cut_position = all_possible_cut_sites[i - 1]
            fragment_size = this_cut_position - previous_cut_position
            print("one fragment size is " + str(fragment_size))

    def abc2(self):
        dna = open(self.file).read().rstrip("\n")
        all_possible_cut_sites_2 = [0]

        for match in re.finditer(r"GC[AG][AT]TG", dna):
            all_possible_cut_sites_2.append(match.start() + 4)
            print(all_possible_cut_sites_2)
            print("_______")

        all_possible_cut_sites_2.append(len(dna))
        print("***********")
        print(all_possible_cut_sites_2)

        for i in range(1, len(all_possible_cut_sites_2)):
            this_cut_position = all_possible_cut_sites_2[i]
            previous_cut_position = all_possible_cut_sites_2[i - 1]
            fragment_size = this_cut_position - previous_cut_position
            print("one fragment size is " + str(fragment_size))

    def AvrII(self):
        dna = open(self.file).read().rstrip("\n")
        all_possible_cut_sites_2 = [0]

        for match in re.finditer(r"CCTAGG", dna):
            all_possible_cut_sites_2.append(match.start() + 1)
            print(all_possible_cut_sites_2)
            print("_______")

        all_possible_cut_sites_2.append(len(dna))
        print("***********")
        print(all_possible_cut_sites_2)

        for i in range(1, len(all_possible_cut_sites_2)):
            this_cut_position = all_possible_cut_sites_2[i]
            previous_cut_position = all_possible_cut_sites_2[i - 1]
            fragment_size = this_cut_position - previous_cut_position
            print("one fragment size is " + str(fragment_size))
    def AcvI(self):
        dna = open(self.file).read().rstrip("\n")
        all_possible_cut_sites_2 = [0]

        for match in re.finditer(r"GG[ATGC]CC", dna):
            all_possible_cut_sites_2.append(match.start() + 1)
            print(all_possible_cut_sites_2)
            print("_______")

        all_possible_cut_sites_2.append(len(dna))
        print("***********")
        print(all_possible_cut_sites_2)

        for i in range(1, len(all_possible_cut_sites_2)):
            this_cut_position = all_possible_cut_sites_2[i]
            previous_cut_position = all_possible_cut_sites_2[i - 1]
            fragment_size = this_cut_position - previous_cut_position
            print("one fragment size is " + str(fragment_size))




a = Digest()  # a라는 객체를 생성함
a.abc1()  # abc1메소드를 호출
a.abc2()  # abc2메소드를 호출
a.AcvI()  # avcl3메소드를 호출
a.AvrII()


