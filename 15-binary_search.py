# 二分查找
def binary_search(alist, item):
    n = len(alist)
    up = n - 1
    down = 0
    mid = (up + down) // 2

    while down <= up:
        mid = (up + down) // 2
        if alist[mid] < item:
            down = mid + 1
        elif alist[mid] > item:
            up = mid - 1
        elif alist[mid] == item:
            return True, mid
    return False


def binary_search2(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search2(alist[:mid], item)
        else:
            return binary_search2(alist[mid+1:], item)
    return False


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(li)
    print(binary_search(li, 31))
