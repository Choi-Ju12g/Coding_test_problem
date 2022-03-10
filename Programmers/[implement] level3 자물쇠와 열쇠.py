# a = m x n matrix -> n x m
def rotate_matrix90(a):
    m = len(a)  # 행 개수
    n = len(a[0])  # 열 개수
    result = [[0] * m for _ in range(n)]  # 결과 리스트 초기화
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = a[i][j]
    return result


def make_new_lock(a, key):
    length = len(a)
    additional = key - 1
    new_lock = [[0] * (length + 2 * additional) for _ in range(length + 2 * additional)]
    for i in range(additional, length + additional):
        for j in range(additional, length + additional):
            new_lock[i][j] = a[i - additional][j - additional]
    return new_lock


def check_solve(new_lock, key):
    additional = key - 1
    for i in range(additional, len(new_lock) - additional):
        for j in range(additional, len(new_lock) - additional):
            if new_lock[i][j] != 1:
                return False
    return True

def print_mat(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end='')
        print("")

def solution(key, lock):
    new_lock = make_new_lock(lock,len(key))
    additional = len(key) -1
    length = len(lock)

    for ratate in range(4):
        key = rotate_matrix90(key)
        # 열쇠 이동
        for i in range(length+additional):
            for j in range(length+additional):

                # 위치에서 열쇠값 더하기
                for m in range(additional+1):
                    for n in range(additional+1):
                        new_lock[i+m][j+n] += key[m][n]

                if check_solve(new_lock,additional+1):
                    return True
                print(m,"X",n,"위치")
                print_mat(new_lock)
                print("")
                # 자물쇠 다시 원상태로 복구
                for m in range(additional+1):
                    for n in range(additional+1):
                        new_lock[i+m][j+n] -= key[m][n]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
a = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

test = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0]]

print(make_new_lock(a,len(key)))
print(check_solve(make_new_lock(a,len(key)),len(key)))


print(check_solve(test,len(key)))