#슬라이싱
a="Pithon"
b=a[0:4]
print(b)

#중간 문자열 바꾸기
a[:1]#P
a[2:]#thon
print(a[:1]+'y'+a[2:])

#문자열 포매팅
print("I eat %d apple"% 1 )
print("I eat 2 %s"% "banana")
number=3
arr="mango"
print("I eat %d %s"% (number , arr))
print("I eat {num} {food}".format(food="bread", num=10))

#문자열 관련 함수
a="hobby"
print(a.count('b'))#b의 갯수
print(a.find('h'))#h의 위치
print(",".join("abcd"))#문자열 각각 사이에 삽입
print("end")