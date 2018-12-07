# -*- coding:utf-8 -*-
while (True):
    print('"""')
    print()
    day31_month = [1, 3, 5, 7, 8, 10, 12]
    day30_month = [4, 6, 9, 11]
    day28_month = [2]
    number = input("확인하고 싶은 주민번호를 입력해주세요:")
    if (number == "종료"):
        print()
        print("프로그램을 종료합니다.")
        print('"""')
        break
    else:  # input 값이 종료 이외일 경우 밑에 코드들 실행
        number_list = number.split('-')  # '-' 기준으로 나누어서 리스트로 만듬
        number1 = int(number_list[0])  # 생년월일 부분 정수형
        p_number1 = number_list[0]  # 생년월일 부분 문자형
        year = int(number_list[0][0:2])  # 생년 정수형
        p_y = number_list[0][0:2]  # 생년 문자형
        month = int(number_list[0][2:4])  # 월 정수형
        day = int(number_list[0][4:])  # 일 정수형
        number2 = int(number_list[1])  # 뒤에 7자리 정수형
        p_number2 = number_list[1]  # 뒤에 7자리 문자형
        sex = int(number_list[1][0])  # 뒤에 7자리 중 첫숫자 정수형
        if (len(p_number1) != 6):  # 생년월일이 6자리가 아니면 실행
            print()
            print("유효하지 않은 주민등록번호입니다.")
            print()
            continue
        elif (len(p_number2) != 7):  # 뒤에 7자리가 7자리가 아니면 실행
            print()
            print("유효하지 않은 주민등록번호입니다.")
            print()
            continue
        if (not (0 < month < 13)):  # 월이 1~12 사이 숫자 아니면 실행
            print()
            print("유효하지 않은 주민등록번호입니다.")
            print()
            continue
        if (month in day31_month):
            if (not (0 < day < 32)):  # 일이 1~31사이가 아닐경우
                print()
                print("유효하지 않은 주민등록번호입니다.")
                print()
                continue

        if (month in day28_month):  # 월이 2월일 경우
            if (not (0 < day < 29)):  # 일이 1~28일이 아닐경우 실행
                print()
                print("유효하지 않은 주민등록번호입니다.")
                print()
                continue

        if (month in day30_month):
            if (not (0 < day < 31)):  # 일이 1~30사이가 아닐경우
                print()
                print("유효하지 않은 주민등록번호입니다.")
                print()
                continue
        if (sex == 1 or sex == 2):  # 뒷7자리중 첫자리가 1 또는 2인 경우
            p_y = "19" + p_y
            if (sex == 1):  # 1일경우
                print()
                print(p_y + " 년 " + str(month) + " 월 " + str(day) + " 일 생 남자 입니다.")
                print()
            elif (sex == 2):  # 2일 경우
                print()
                print(p_y + " 년 " + str(month) + " 월 " + str(day) + " 일 생 여자 입니다.")
                print()
        if (sex == 3 or sex == 4):  ##뒷7자리중 첫자리가 3 또는 4인 경우
            if (year > 17):  # 현재 년도 보다 더 미래일수가 없다.
                print("유효하지 않은 주민등록번호입니다.")
                continue
            else:
                p_y = "20" + p_y
                if (sex == 3):  # 3인경우
                    print()
                    print(p_y + " 년 " + str(month) + " 월 " + str(day) + " 일 생 남자 입니다.")
                    print()
                elif (sex == 4):  # 4일경우
                    print()
                    print(p_y + " 년" + str(month) + " 월" + str(day) + " 일 생 여자 입니다.")
                    print()
