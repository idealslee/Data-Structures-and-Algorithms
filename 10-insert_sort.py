import time


# 插入排序
def insert_sort(alist):
    n = len(alist)
    for j in range(n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 6, 45, 33, 789, 2]
    print(li)
    start = time.time()
    insert_sort(li)
    end = time.time()
    print(li)
    print(end - start)
