# 유저의 입력 리스트와 제시된 문제 리스트를 입력받아
# hit와 blow 수를 딕셔너리에 담아 리턴
# 두 리스트는 모두 양의 정수를 가지고 중복된 숫자가 없음
# 두 리스트의 각 자리(같은 인덱스)를 비교하는데
# 같은 자리에 같은 숫자가 있으면 hit
# 다른 자리에 같은 숫자가 있으면 blow
# ex) [0, 1, 2, 3], [5, 3, 2, 1]    =>      {'hit': 1, 'blow': 2}
# ex) [0, 5, 1, 4], [5, 3, 2, 1]    =>      {'hit': 0, 'blow': 2}
# ex) [5, 4, 0, 1], [5, 3, 2, 1]    =>      {'hit': 2, 'blow': 0}
# ex) [5, 3, 2, 1], [5, 3, 2, 1]    =>      {'hit': 4, 'blow': 0}
def check_answer(user_data, task):
    result = {"hit":0, "blow":0}
    hit = 0
    blow = 0
    for i in range(0, len(task)):
        if task[i] == user_data[i]:
            hit += 1
        elif user_data[i] in task:
            blow += 1
    result.update({"hit":hit})
    result.update({"blow":blow})
    return result
