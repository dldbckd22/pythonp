import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()
input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()
et = end - start
print("실제 시간 : {:.0f}초".format(et))
print("차이 : {:.0f}초".format(abs(et - 20)))
