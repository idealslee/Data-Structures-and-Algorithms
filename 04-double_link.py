from single_link import SingleLinkList


# 节点类
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


# 链表类
class DoubleLinkList(SingleLinkList):

    def __init__(self, node=None):
        self.__head = node

    # def is_empty(self):
    #     if not self.__head:
    #         return True
    #     else:
    #         return False
    #
    # def length(self):
    #     cur = self.__head
    #     count = 0
    #     while cur != None:
    #         count += 1
    #         cur = cur.next
    #     return count
    #
    # def travel(self):
    #     cur = self.__head
    #     while cur != None:
    #         print(cur.elem, end=" ")
    #         cur = cur.next
    #     print("\n")

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        :param pos: 位置
        :param item: 节点数值
        :return:
        """
        node = Node(item)
        if pos < 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.__head
        flag = 0
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表是否只有一个节点
                    if cur.next is not None:
                        cur.next.prev = None
                    print("element removed!")
                    self.travel()
                else:
                    cur.prev.next = cur.next
                    if cur.next is not None:
                        cur.next.prev = cur.prev
                    print("element removed!")
                    self.travel()
                flag = 1
                break
            else:
                cur = cur.next
        if flag == 0:
            print("element not exist!")

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    double_obj = DoubleLinkList()
    print(double_obj.is_empty())
    print(double_obj.length())

    double_obj.add(8)
    double_obj.travel()
    double_obj.append(1)
    print(double_obj.is_empty())
    print(double_obj.length())

    double_obj.append(2)
    double_obj.append(3)
    double_obj.append(4)
    double_obj.append(5)

    print(double_obj.length())
    double_obj.travel()

    double_obj.add(100)
    double_obj.travel()

    double_obj.insert(4, 256)
    double_obj.travel()

    double_obj.insert(-4, 1024)
    double_obj.travel()

    print(double_obj.search(256))

    double_obj.remove(102)
