


# f = open("D:/ai/pythonp/basic/text2.txt", 'a')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("D:/ai/pythonp/basic/text2.txt", 'r',encoding='utf8')
# while True:
#     line = f.readline()
#     if not line: 
#         break
#     line=line.replace('\n','')
#     print(line)
# f.close()
f=open("D:/ai/pythonp/basic/word.txt", 'r',encoding='utf8')
lines = f.readlines()

for line in lines:
    line=line.replace('\n','')
    print(line)
f.close()




