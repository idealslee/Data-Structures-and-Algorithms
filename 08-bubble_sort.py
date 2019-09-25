import time

# 冒泡排序
def bubble_sort(alist):
    n = len(alist)
    for j in range(0, n-1):
        # 一个元素从头到未排序序列的尾，比较
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            break
    """
    for j in range(n-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
            alist[i], alist[i+1] = alist[i+1], alist[i]
    """


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    start = time.time()
    bubble_sort(li)
    end = time.time()
    print(li)
    print(end-start)
