import time


# 选择排序
def choose_sort(alist):
    n = len(alist)
    for j in range(n-1):
        small = j
        for i in range(j+1, n):
            if alist[i] < alist[small]:
                small = i
        alist[j], alist[small] = alist[small], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 6, 45, 33, 789, 2]
    print(li)
    start = time.time()
    choose_sort(li)
    end = time.time()
    print(li)
    print(end - start)

