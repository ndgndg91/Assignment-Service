while(True):
    print("간단한 영단어를 한국말로 번역해 드립니다.")
    print("종료를 원하실 경우 q를 입력하세요.")
    s = raw_input("번역하실 단어를 입력하세요 : ")


    tf =False;
    if(s=="q"):
        break;
    else:
        
        dictionary = {"hello":"안녕하세요","apple":"사과","banana":"바나나",
                      "car":"자동차","man":"남자","love":"사랑",
                      "i love you":"나는 당신을 사랑합니다"}

        for k in dictionary.keys():
            if(k==s):
                tf=True;
                print("====================")
                print(dictionary[k])
                print("====================")
                break;

        if(tf==False):
            print("무슨말인지 번역이 불가능합니다.")
