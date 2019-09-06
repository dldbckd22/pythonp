import random,time
com=random.sample(range(1,10),3)    
print(com) 
strike = 0
check=0
input("시작!")
start = time.time()
while strike != 3:
    strike = 0
    ball = 0
    guess = list(input("3자리 숫자를 입력하세요 : "))
    print(guess)
    for a in guess:
        for b in com:
            if int(a)==b and guess.index(a)==com.index(b) :
                strike+=1
            elif int(a)==b:
                ball+=1
    check+=1
    print("스트라이크:%d, 볼:%d, 시도횟수:%d" %(strike,ball,check)) 
end=time.time()
print("정답!! 걸린시간은 {:.0f}초입니다.".format(end-start))                  