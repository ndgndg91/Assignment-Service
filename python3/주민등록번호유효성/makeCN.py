def make_input():
    print("+++++++++++++++++++++++++")
    print("++++주민등록번호 생성기++++")
    print("+++++++++++++++++++++++++")
    print()
    print("개인 정보를 입력해 주세요.")
    list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # index 0,2,4,6,7,9,11 31일까지
    day31_month = [1, 3, 5, 7, 8, 10, 12]
    day30_month = [4, 6, 9, 11]
    day28_month = [2]
    year = input("년도 : ")
    if (int(year) < 1900 or int(year) > 2099):
        print()
        print("**************** 1900~2099년생만 취급합니다. ****************")
        print("**************** 년도를 위에 맞게 입력해주세요 ****************")
        print()
        return make_input()
    month = input("달 : ")
    if (int(month) not in list_month):
        print()
        print("************ 외계에서 오셨나요? 01~12만 취급합니다. *************")
        print("**************** 월을 위에 맞게 입력해주세요 ****************")
        print(" ************** 처음부터 다시 입력합니다. ****************")
        print()
        return make_input()
    day = input("일 : ")
    if (int(month) in day31_month):
        if (int(day) < 1 or int(day) > 31):
            print()
            print("******** 1,3,5,7,8,10,12월은 1~31일 까지 입니다. *****")
            print("******** 처음부터 다시 입력합니다. *****")
            print()
            return make_input()
    elif (int(month) in day28_month):
        if (int(day) < 1 or int(day) > 28):
            print()
            print("******** 2월은 1~28일 까지 입니다. *****")
            print("******** 처음부터 다시 입력합니다. *****")
            print()
            return make_input()
    elif (int(month) in day30_month):
        if (int(day) < 1 or int(day) > 30):
            print()
            print("******** 4,6,9,11월은 1~30일 까지 입니다. *****")
            print("******** 처음부터 다시 입력합니다. *****")
            print()
            return make_input()
    sex = input("성별 : ")
    if(sex != "남자" and sex != "여자"):
        print()
        print("************ 주민등록번호는 성소수자들을 배려하지 않습니다. ************")
        print("****************** 남자 또는 여자를 입력해주세요. ********************")
        print("******************** 처음부터 다시 입력합니다. **********************")
        print()
        return make_input()
    cn_dictionary = {"Year": year, "Month": month, "Day": day, "Sex": sex}
    return cn_dictionary


information = make_input()


def CN_maker(dictionary):
    year = dictionary["Year"]
    month = dictionary["Month"]
    day = dictionary["Day"]
    number = 0
    if (int(day) < 10):
        day = "0" + day
    sex = dictionary["Sex"]
    if (year[0] == "1"):
        if (sex == "남자"):
            number = 1
        elif (sex == "여자"):
            number = 2
    elif (year[0] == "2"):
        if (sex == "남자"):
            number = 3
        elif (sex == "여자"):
            number = 4

    year = year[2:]
    first = year + month + day
    second = str(number) + "******"
    return print("당신의 주민등록번호는\t" + first + '-' + second + "\t입니다.")


CN_maker(information)
