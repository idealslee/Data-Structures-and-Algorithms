import time


# 归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    left_p, right_p = 0, 0
    result = []

    while left_p < len(left_li) and right_p < len(right_li):
        if left_li[left_p] < right_li[right_p]:
            result.append(left_li[left_p])
            left_p += 1
        else:
            result.append(right_li[right_p])
            right_p += 1

    result += left_li[left_p:]
    result += right_li[right_p:]

    return result


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    start = time.time()
    sorted_li = merge_sort(li)
    end = time.time()
    print(sorted_li)
    print(end - start)
