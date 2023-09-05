#딕셔너리 자료형
a={'name':'pey', 'phone':'010-1234-5678', 'birth':1118}
print(a)

#딕셔너리 추가
a={1:'pey'}
a[2]='b'
print(a)

#딕셔너리 삭제
del a[1]
print(a)

grade={'pey':10, 'juliet':12}
print(grade['pey'])

#딕셔너리 관련 함수
#key리스트 만들기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
#value리스트 만들기
print(a.values())
#key,value 쌍 얻기
print(a.items())
#key로 value얻기
print(a.get('name'))
#해당key가 딕셔너리에 있는지 조사하기
print('name' in a)
print('animal' in a)
#key,value 쌍 모두지우기
print(a.clear())