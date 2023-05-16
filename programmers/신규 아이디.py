# 실패

def solution(new_id):
    answer = ''
    lst = []
    lst1 = ['-','_','.']

    new_id = new_id.lower()

    for i in new_id:
        if (i >='a' and i <= 'z') or (i >= '0' and i <= '9') or (i in lst1):
            continue
        else:
            new_id = new_id.replace(i, '')
    
    '''
    실패한 부분 
    처음에는 . 개수를 세서 2개가 넘어가면 바꾸려고 했다
    그러나 마지막이 . 으로 끝나는 경우를 생각하지 못해서 틀렸다
    그래서 j라는 변수를 추가로 줘서 
    .이면서 new_id의 len - 1과 같으면 제거하려고 했다
    그러나 틀렸따
    '''
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) != 0 and new_id[- 1] == '.':
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[len(new_id) - 1] == '.':
            new_id = new_id[:len(new_id)-1]

    # print(new_id)
    if len(new_id) <= 3:
        new_id += new_id[-1] * (3-len(new_id))

    print(new_id)
    answer = new_id
    return answer

'''
총평 
카카오 문제는 역시 어렵다
string의 replace 문과 
while문의 사용법에 대해 더 알게 된 것 같다
정규식을 조금 공부해봐야 할 것 같다
'''