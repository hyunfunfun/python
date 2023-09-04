#리스트 자료형
a=[1,2,3]
print(a)
print(a[0]+a[2])
b=[1,2,3,['a','b','c']]
print(b[3])
print(b[3][0])

#리스트 연산
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)
print(len(a))#길이

#리스트 수정
a[2]=4
print(a)
#리스트 삭제
del a[2]
print(a)
#리스트 추가
a.append(4)
print(a)
#리스트 정렬
b=[1,4,3,2]
b.sort()
print(b)
#리스트 뒤집기
b.reverse()
print(b)
#리스트 반환(찾기)
print(b.index(3))
#리스트 요소 삽입
b.insert(1,5)#1번째에 5삽입
print(b)
#리스트 요소 제거
b.remove(2)#첫번째로 나오는 2제거
print(b)
#리스트 마지막요소 끄집어내기
print(b.pop())
print(b)#마지막에 있던 숫자는 삭제됨
#리스트에 있는 요소 카운트
a=[1,2,3,1]
print(a.count(1))
#리스트 확장 (리스트만 확장가능)
a.extend([4,5])
print(a)
b=[7,8,9]
a.extend(b)
print(a)