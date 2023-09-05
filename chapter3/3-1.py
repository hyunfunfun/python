#if문
money=True
if money :
    print('taxi')
else:
    print('walk')

a=3
if a==1:
    print(1)
elif a==3:
    print(3)
else:
    print('not')

#while문
treehit=0
while treehit<10:
    treehit+=1
    print('나무 %d번 찍음'% treehit)
    if treehit==10:
        print('나무 쓰러짐')
