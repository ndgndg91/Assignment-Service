import time  # time 모듈 import

name = input('이름을 입력하시요 : ')  # 이름 입력받아 변수저장
birth = input('안녕하세요.' + name + '씨. 생년월일 8자리를 yyyymmdd(예를 들어 1980년 2월 12일 : 19800212) 형태로 입력하시요 : ')  # 생일 입력받아 변수 저장
birth_year = int(birth[0:4])  # 태어난 년도
birth_month = int(birth[4:6])  # 태어난 월
birth_day = int(birth[6:8])  # 태어난 일
current = time.gmtime(time.time())  # 현재시간
current_year = int(current.tm_year)  # 현재년도
current_month = int(current.tm_mon)  # 현재월
current_day = int(current.tm_mday)  # 현재일
age = current_year - birth_year  # 현재년도 - 태어난 년도
if current_month > birth_month:  # 현재월이 생일월보다 지났는지 확인
    pass
elif current_month < birth_month:  # 현재월이 태어난월 안지났으면 -1살
    age -= 1
elif current_month == birth_month:  # 현재월이랑 태어난월이랑 같은경우
    if current_day >= birth_day:  # 현재일이 생일이 지난 경우
        pass
    else:  # 현재월이랑 태어난월이랑 같지만 아직 생일이 지나지 않은경우 -1살
        age -= 1

print(name + '씨는 오늘 만 ' + str(age) + '살 입니다.')  # 만 나이 출력

future_age = input('몇살이 되는 날짜를 알고 싶습니까? : ')  # 미래나이에 알고 싶은 년도를 찾기 위해서 입력받기
plus = int(future_age) - age - 1  # ex) 50 - 20 - 1 = 29  만 나이는 생일을 기준으로 먹기 때문에 년도 -1을 해줘야됨
print(name + '씨는 ' + str(current_year + plus) + '년 ' + str(birth_month) + '월 ' + str(
    birth_day) + '일에 ' + future_age + '살이 됩니다')  # 생일을 지나야되기 때문에 생일기준으로 만 나이 출력
