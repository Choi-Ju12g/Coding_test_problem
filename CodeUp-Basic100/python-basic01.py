# basic 01
#print("Hello")

# basic 02
#print("Hello World")
#print("Hello","World")

# basic 03
#print("Hello")
#print("World")

# basic 04
#print("\'Hello\'")
#print("'Hello'")

# basic 05
#print("\"Hello World\"")

# basic 06
#print("\"!@#$%^&*()'")
# "!@#$%^&*()'

# basic 07
#print("\"C:\\Download\\'hello'.py\"")
#"C:\Download\'hello'.py"

# basic 08
#print("print(\"Hello\\nWorld\")")
#print("Hello\nWorld")

# basic 09
#c = input()
#print(c)

# basic 10
#c = int(input())
#print(c)

# basic 11
#c = float(input())
#print(c)

# basic 12
# a = input()
# b = input()
# print(a)
# print(b)

# basic 13
# a = input()
# b = input()
# print(b+"\n"+a)

# basic 14
# a = input()
# print((a+"\n")*3)

# basic 15
# a,b = input().split()
# print(a)
# print(b)

# basic 16
# a,b = input().split()
# print(b,a)

# basic 17
# c = input()
# print(c,c,c)

# basic 18
# a,b = input().split(":")
# print(a,b,sep=":")

# basic 19
# a,b,c = input().split(".")
# print(c,b,a,sep="-")
# sep은 각 변수 사이에 넣는 문자

# basic 20
# a, b = input().split('-')
# print(a+''+b)
# ''는 공백, 즉 붙여쓸때 사용가능

# basic 21
# s = input()
# for i in range(len(s)):
#     print(s[i])

# basic 22
# s = input()
# print(s[0:2] + " " + s[2:4] + " " + s[4:6])

# basic 23
# s = input().split(":")
# print(s[1])

# # basic 24
# a,b = input().split()
# print (a+b)

# basic 25
# a, b = map(int, input().split())
# print(a+b)

# basic 26
# a = float(input())
# b = float(input())
# print(a+b)

# basic 27
# a = int(input())
# print('%x'%a)

# basic 28
# a = int(input())
# print('%X'%a)

# basic 29
# a = input()
# n = int(a,16)
# print('%o'%n)

# basic 30
# print(ord(input()))
#ord(input()) 입력받은 문자 -> 유니코드 값

# basic 31
#print(chr(int(input())))
# a = int(input())
# print(chr(a))
#chr(c) c에 저장된 정수 -> 유니코드 문자 A:65

# basic 32
# a = int(input())
# print(-a)

# basic 33 *아스키 값 변환하기 위해선 ord()필수
# a = ord(input())
# b = int(a)+1
# print(chr(b))

# basic 34
# a,b = map(int, input().split())
# print(a-b)

# basic 35
# a,b = map(float, input().split())
# print(a*b)

# basic 36
# a,b = input().split()
# print(a*int(b))

# basic 37
# a = int(input())
# b = input()
# print(b*a)

# basic 38
# a, b= map(int, input().split())
# print(a**b)

# basic 39
# a, b= map(float, input().split())
# print(a**b)

# basic 40
# a, b= map(int, input().split())
# print(a//b)

# basic 41
# a, b= map(int, input().split())
# print(a%b)

# basic 42
# a = float(input())
# print(round(a,2))  #round(a,b) 실수 a를 소수점 b째 자리에서 반올림
#print(format(a, ".2f"))

# basic 43
# a,b = map(float, input().split())
# print(round(a/b,3))
# print(format(a/b,".3f"))
#round()는 반올림하고 필요없는 수는 출력 X, format()은 반올림 하고 그 자리수까지 무조건 표현

# basic 44
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b,".2f"))
#python은 int 범위 무한...

# basic 45
# a,b,c = map(int, input().split())
# print(a+b+c,format((a+b+c)/3,".2f"))

# basic 46
# print(int(input())<<1)

# basic 47
# a,b = map(int, input().split())
# print(a<<b)

# basic 48
# a,b = map(int, input().split())
# if a<b:
#     print(True)
# else:
#     print(False)
# print(123<456) 이면 True 출력

# basic 49
# a,b = map(int, input().split())
# # if a== b:
# #     print(True)
# # else:
# #     print(False)
# print(a==b)

# basic 50
# a, b = map(int, input().split())
# print(b>=a)

# basic 51
# a, b = map(int, input().split())
# print(a!=b)

# basic 52
# a = int(input())
# print(bool(a))

# basic 53
# a = int(input())
# print(not bool(a))

# basic 54
# a, b = map(int, input().split())
# print(bool(a&b))

# basic 55
# a, b = map(int, input().split())
# print(bool(a or b))

# basic 56
# a, b = map(int, input().split())
# print(bool(a) or bool(b))

# basic 57
# a, b = map(int, input().split())
# print(not(bool(a)^bool(b)))

# basic 58
# a, b = map(int, input().split())
# print(not(bool(a)|bool(b)))

# basic 59
# a = int(input())
# print(~a)

# basic 60
# a, b = map(int, input().split())
# print(a&b)

# basic 61
# a, b = map(int, input().split())
# print(a|b)

# basic 62
# a, b = map(int, input().split())
# print(a^b)

# basic 63
# a, b = map(int, input().split())
# print(a if(a>=b) else b)
# 3항연산자 참일때 값 if(조건)else 거짓일때 값

# basic 64
# a, b, c = map(int, input().split())
# print((a if (a<b) else b) if((a if (a<b) else b) <c) else c)
#
# # basic 65
# a, b, c = map(int, input().split())
# if a%2==0:
#     print(a)
# if b%2==0:
#     print(b)
# if c%2==0:
#     print(c)

# basic 66
# a, b, c = map(int, input().split())
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# if b%2==0:
#     print("even")
# else:
#     print("odd")
# if c%2==0:
#     print("even")
# else:
#     print("odd")

# basic 67
# a = int(input())
# if a > 0:
#     if a%2==0:
#         print("C")
#     else:
#         print("D")
# else:
#     if a%2==0:
#         print("A")
#     else:
#         print("B")


# basic 68
# a = int(input())
# if a>= 90:
#     print("A")
# elif a>=70:
#     print("B")
# elif a>= 40:
#     print("C")
# else:
#     print("D")

# basic 69
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else : print("what?")

# basic 70
a = int(input())
if a//3 == 1:
    print("spring")
elif a//3 == 2:
    print("summer")
elif a//3 ==3:
    print("fall")
else:
    print("winter")

# basic 71
n = 1
while n != 0:
    n = int(input())
    if n ==0:
        break
    print(n)

# basic 72
n = int(input())
# for i in range(n):
#     print(n-i)
while n!=0:
    print(n)
    n-=1

# basic 73
n = int(input())
# for i in range(n):
#     print(n-i)
while n!=0:
    print(n-1)
    n-=1

# basic 74
a = ord(input())
b =ord('a')
n = a-b
for i in range(n+1):
    print(chr(b+i),end=' ')

# basic 75
a = int(input())
for i in range(a+1):
    print(i)

# basic 76
a = int(input())
n = a
while n>=0:
    print(a-n)
    n-=1
# real basic is over

# basic 77

# basic 78

# basic 79

# basic 80

# basic 81

# basic 82

# basic 83

# basic 84

# basic 85

# basic 86

# basic 87

# basic 88

# basic 89

# basic 90

# basic 91

# basic 92

# basic 93

# basic 94

# basic 95

# basic 96

# basic 97

# basic 98

# basic 99

# basic 100


