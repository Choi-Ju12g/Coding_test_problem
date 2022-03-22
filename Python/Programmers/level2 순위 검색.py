def solution(info, query):
    answer = []
    info_list =[]
    query_list =[]
    key = dict()
    for i in info:
        info_list.append(i.split())
    for j in query:
        query_list.append(j.split())
        while len(query_list) > 5:
            query_list.remove('and')

    for i in range(len(info_list)):
        for j in range(len(query_list)):
            flag = 0
            for k in range(4):
                if info_list[i][k] != query_list[j][k]:
                    if query_list[j][k] != '-':
                        flag = 1
                        break
            if flag == 0:
                if int(info_list[i][4]) >= int(query_list[j][4]):
                    answer[j] += 1

    return answer