import random,time,pickle,os

class GameClass:
    w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
    rank={}

    def __init__(self):
        pass

    def rankLoad(self):
        if os.path.exists('D:\ai\pythonp\basic\rank.pik'):
            f=open('D:\ai\pythonp\basic\rank.pik','rb')
            self.rank=pickle.load(f)
       

    def wordLoadTxt(self):
        with open('D:\ai\pythonp\basic\word.txt','r',encoding='utf8') as f:
            lines=f.readlines()
            for i in range(len(lines)):
                lines[i]=lines[i].replace('\n','')
                self.w=self.w+lines 
        print(self.w)
        
        '''
        f=open(D:\ai\pythonp\basic\word.txt','r',encoding='utf8')
        line = 1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
            w.append(line)
        print(w)
        f.close()
        '''

    def wordSaveTxt(self):
        
        with open('D:\ai\pythonp\basic\word.txt','w',encoding='utf8') as f:
            data=''
            for i in self.w:
                data+=i+'\n'
        f.write(data)
         

    def wordAppend(self):
  
        quiz=1
        while quiz:
            quiz=input('추가할 단어 입력(종료:0) >> ')
            if quiz=='0':
                print('입력을 종료합니다.')
                break
            self.w.append(quiz)
        print(self.w)    

    def wordSavePik(self):
       
        with open('D:\ai\pythonp\basic\word.pik','wb') as f:
            pickle.dump(self.w,f)
       
        print(self.w)    

    def wordLoadPik(self):
       
        with open('D:\ai\pythonp\basic\word.pik','rb') as f:
            self.w=pickle.load(f)
        
        print(self.w)

    def game(self):
        
        n=1
        q=random.choice(self.w)
        input('시작!')
        start = time.time()
        while n<=5:
            print("--{}번--".format(n))
            print(q)
            x=input()
            if q ==x:
                print("통과!")
                n=n+1
                q=random.choice(self.w)
            else:
                print("오타! 다시도전!")  
        end= time.time()
        print('걸린 시간 : {:.0f}초'.format(end-start))
        name = input('이름을 입력하세요')
        self.rank[name]=end-start
        f=open('D:\ai\pythonp\basic\rank.pik','wb')
        pickle.dump(self.rank,f)
        f.close()
        print(self.rank)

    def rankList(self):
    
        ranklist=sorted(self.rank.items(),key=(lambda x: x[1]))
        print(ranklist)
        cnt=1
        for k,v in ranklist:
            print('{}등 {} 시간:{:.2f}'.format(cnt,k,v)) 
            cnt+=1  