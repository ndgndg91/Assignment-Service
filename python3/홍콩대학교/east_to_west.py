def main():
    """양배추, 염소, 늑대를 옮기기 동쪽에서 서쪽으로 옮기기 (염소,양배추) (늑대,염소) 같은 위치에 있으면 안됨
    1. 사람과 염소 e->w

    2. 사람혼자 w->e

    3. 사람과 늑대 e->w

    4. 사람과 염소 w->e

    5. 사람과 양배추 e->w

    6. 사람혼자 w->e

    7. 사람과 염소 e->w"""
    man_directions = ['W', 'E', 'W', 'E', 'W', 'E', 'W']  # 사람이 움직이는 방향을 리스트로
    for i in range(7):  # 총 7번의 움직임을 for문을 사용
        if i == 0:  # 사람이 염소를 데리고 서쪽으로 이동
            takes_something_to_move(i, man_directions[i], 'goat')
        elif i == 2:  # 사람이 늑대를 데리고 서쪽으로 이동
            takes_something_to_move(i, man_directions[i], 'wolf')
        elif i == 3:  # 사람이 염소를 데리고 동쪽으로 이동
            takes_something_to_move(i, man_directions[i], 'goat')
        elif i == 4:  # 사람이 양배추를 가지고 서쪽으로 이동
            takes_something_to_move(i, man_directions[i], 'cabbage')
        elif i == 6:  # 사람이 염소를 데리고 서쪽으로 이동
            takes_something_to_move(i, man_directions[i], 'goat')
        else:  # 사람이 혼자서 동쪽으로 이동하는 경우
            takes_something_to_move(i, man_directions[i], None)


def make_full_string(string):
    """W, E 문자열을 West, East 로 만들어주는 함수 """
    if string == 'W':  # 사람의 이동방향이 서쪽일 경우 완벽한 문자열을 만들어주기 위함
        string += 'est'
    elif string == 'E':  # 사람의 이동방향이 동쪽일 경우 완벽한 문자열을 만들어주기 위함
        string += 'ast'
    return string


def takes_something_to_move(index, man_direction, something=None):
    """순서와 사람의 이동방향과 데리고갈 무언가를 입력받아서 출력해주는 함수"""
    man_direction = make_full_string(man_direction)
    if something is None:  # 데리고 갈 무언가가 없이 사람 혼자 이동할 경우
        print(str(index + 1) + '. The man takes the himself to the ' + man_direction)
    else:  # 데리고 갈 무언가가 있는 경우
        print(str(index + 1) + '. The man takes the ' + something + ' to the ' + man_direction)


if __name__ == '__main__':  # 프로그램 실행시 맨처음에 동작
    main()  # main()메소드 실행
