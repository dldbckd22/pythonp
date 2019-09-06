prompt='''
 1. 커피메뉴입력
 2. 커피가격
 3. 종료
 Enter menu >>
'''
coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
order=0
while order!= '3':
    print(prompt)
    order=input()
    if order=='1':
        menuname=input('메뉴이름>>')
        menuprice=input('메뉴가격>>')
        coffee[menuname]=int(menuprice)
        print("메뉴 {} 가격 {}원을 등록합니다.".format(menuname,menuprice))
    elif order=='2':
        for c in coffee:
            print(c,end=' ')
        print()
        menu = input("선택 : ")
        for k,v in coffee.items(): # 튜플로 리턴 (키,값)
            if k==menu:
                print(v)
    elif order=='3':        
        pass
    else:
        print("메뉴를 다시 입력하세요")