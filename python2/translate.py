while(True):
    print("������ ���ܾ �ѱ����� ������ �帳�ϴ�.")
    print("���Ḧ ���Ͻ� ��� q�� �Է��ϼ���.")
    s = raw_input("�����Ͻ� �ܾ �Է��ϼ��� : ")


    tf =False;
    if(s=="q"):
        break;
    else:
        
        dictionary = {"hello":"�ȳ��ϼ���","apple":"���","banana":"�ٳ���",
                      "car":"�ڵ���","man":"����","love":"���",
                      "i love you":"���� ����� ����մϴ�"}

        for k in dictionary.keys():
            if(k==s):
                tf=True;
                print("====================")
                print(dictionary[k])
                print("====================")
                break;

        if(tf==False):
            print("���������� ������ �Ұ����մϴ�.")
