import time


# 快速排序
def quick_sort(alist, first, last):
    n = len(alist)
    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last

    while high > low:
        while high > low and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while high > low and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    start = time.time()
    quick_sort(li, 0, len(li)-1)
    end = time.time()
    print(li)
    print(end - start)
