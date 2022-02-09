from itertools import combinations_with_replacement as H
from itertools import permutations as P

# def getSubstringCount(s):
#     continous_cnt = []
#     count = 0
#     result = 0
#     pivot = s[0]
#     for i in s:
#         if i != pivot:
#             continous_cnt.append(count)
#             count = 1
#             pivot = i
#         else:
#             count += 1
#
#     if count > 1:
#         continous_cnt.append(count)
#     else:
#         continous_cnt.append(1)
#
#     print(continous_cnt)
#     for i in range(len(continous_cnt) - 1):
#         result += min(continous_cnt[i], continous_cnt[i + 1])
#
#     return result
# s = '1100010'
# print(getSubstringCount(s))

# workHours = 5
# pattern = "???1000"
#
#
# def Hwith0(dayHours, q_count, workHours):
#     A = [list(x) for x in H(range(0, dayHours + 1), q_count) if sum(x) == workHours]
#     #print(A)
#     # print(set(P(A[0], len(A[0]))), end="")
#     return A
#
#
# def findSchedules(workHours, dayHours, pattern):
#     # Write your code here
#     q_count = 0
#     case = []
#     result = []
#     for i in pattern:
#         if i != "?":
#             workHours -= int(i)
#         else:
#             q_count += 1
#
#     case = Hwith0(dayHours, q_count, workHours)
#     for i in range(len(case)):
#         list_set = list(set(P(case[i])))
#         result.append(make_schedule_pattern(list_set, pattern))
#     result = print_list(result)
#     return result
#
# def make_schedule_pattern(list_set, pattern):
#     answer = []
#     temp = ""
#     for list in list_set:
#         cnt = 0
#         for i in pattern:
#             if i == "?":
#                 temp += str(list[cnt])
#                 cnt+=1
#             else:
#                 temp += i
#         answer.append(temp)
#         temp = ""
#     return answer
#
# def print_list(list):
#     temp = []
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             temp.append(list[i][j])
#     return temp
#
# print(findSchedules(5, 2, "???1000"))







