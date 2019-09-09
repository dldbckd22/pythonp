'''
def say_myself(name,old,man=True):
    print('나의이름은 {}'.format(name))
    print('나이는{}'.format(old))
    if man:
        print('남자')
    else:
        print('여자')
say_myself('홍길동',34,)
'''

'''
class Cookie:
    pass

a=Cookie()
b=Cookie()

print(id(a))
print(id(b))
print(type(a))
'''
class Fourcal:
    first=0
    second=0
    def setdata(self,first,second):
        self.first=first
        self.second=second


a=Fourcal()
a.setdata(5,7)
print(a.first)
print(a.second)
