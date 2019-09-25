# 节点类
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
    pass


# 链表类
class SingleCycleLinkList(object):

    def __init__(self, node=None):
        self.__head = node
        if node is not None:
            node.next = node

    def is_empty(self):
        if not self.__head:
            return True
        else:
            return False

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur没有打印尾结点
        print(cur.elem)

    def add(self, item):
        node = Node(item)
        cur = self.__head
        if cur is None:
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

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
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        flag = 0
        while cur.next is not self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                    print("element removed!")
                    #self.travel()
                else:
                    pre.next = cur.next
                    print("element removed!")
                    #self.travel()
                flag = 1
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向为节点
        if cur.elem == item:
            if cur is self.__head:
                self.__head = None
            else:
                pre.next = self.__head
                flag = 1
        if flag == 0:
            print("element not exist!")

    def search(self, item):
        cur = self.__head
        if self.is_empty():
            return False
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == "__main__":
    single_obj = SingleCycleLinkList()
    print(single_obj.is_empty())
    print(single_obj.length())

    single_obj.add(8)
    single_obj.travel()
    single_obj.append(1)
    print(single_obj.is_empty())
    print(single_obj.length())

    single_obj.append(2)
    single_obj.append(3)
    single_obj.append(4)
    single_obj.append(5)

    print(single_obj.length())
    single_obj.travel()

    single_obj.add(100)
    single_obj.travel()

    single_obj.insert(4, 256)
    single_obj.travel()

    single_obj.insert(-4, 1024)
    single_obj.travel()

    single_obj.remove(1024)
    single_obj.travel()

    print(single_obj.search(256))

    single_obj.remove(102)
