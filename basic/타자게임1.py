import random,time

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
rank={}
while True:
    print("1.문제불러오기 2.문제추가 3.문제피클로저장 4.문제피클로가져오기  5.타자게임 6.등수리스트 7.종료하기")
    menu = input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open("D:/ai/pythonp/basic/word.txt", 'r',encoding='utf8')
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].replace('\n','')
        w=w+lines
        print(w)
        f.close()
    elif menu=='2':
        quiz=1
        while quiz:
            quiz=input('추가단어(종료:0)>>')
            if quiz=='0':
                print('입력을종료합니다')
                break
            w.append(quiz)
        print(w)
    elif menu=='3':
        import pickle
        with open('D:/ai/pythonp/basic/pickle.pkl','wb') as f: 
            pickle.dump(w,f)
        print(w)
    elif menu=='4':
        import pickle
        with open('D:/ai/pythonp/basic/pickle.pkl','rb') as f:
            pickle.load(f)
        print(w)     
    elif menu=='5':
        n=1
        q=random.choice(w)
        input('시작!')
        start = time.time()
        while n<=5:
            print("--{}번--".format(n))
            print(q)
            x=input()
            if q ==x:
                print("통과!")
                n=n+1
                q=random.choice(w)
            else:
                print("오타! 다시도전!")  
        end= time.time()
        print('걸린 시간 : {:.0f}초'.format(end-start))
        name=input('이름')
        rank[name]=end-start
        print(rank)
    elif menu=='6':
        import pickle
        with open('D:/ai/pythonp/basic/pickle.pkl','wb') as f:
            pickle.dump(rank,f)
        with open('D:/ai/pythonp/basic/pickle.pkl','rb') as f:  
            pickle.load(f)   
        ranklist=sorted(rank.items(),key=(lambda x: x[1]))
        print(ranklist)
        cnt=1
        for k,v in ranklist:
            print('{}등 {} 시간:{:.2}',format(cnt,k,v))
            cnt+=1
    elif menu=='7':
        break



#ㅎㅎㅎ










