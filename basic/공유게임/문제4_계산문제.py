import random,time
count=0
oper=['+','-','*','/']
input("엔터를 누르면 문제가 나옵니다.")
start = time.time()
for x in range(0,5):
    a=random.randint(1,5)
    b=random.randint(1,5)
    op=random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz,'=')
    c=int(input())
    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답!")
end=time.time()
print("{:.0f}초동안 {}개 맞음".format(end-start,count))