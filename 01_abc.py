# 如果a+b+c=1000, a^2 + b^2 = c^3, 求a, b, c

import time

start_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a+b+c ==1000 and a**2 + b**2 == c**2:
#                 print("a:%d b:%d c:%d"%(a, b, c))

for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a:%d b:%d c:%d"%(a, b, c))

end_time = time.time()
print('time:%s'%(end_time - start_time))
print('finished')
