# 节点类
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
    pass


# 链表类
class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        if not self.__head:
            return True
        else:
            return False

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("\n")

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
        cur = self.__head
        pre = None
        flag = 0
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    print("element removed!")
                    self.travel()
                else:
                    pre.next = cur.next
                    print("element removed!")
                    self.travel()
                flag = 1
                break
            else:
                pre = cur
                cur = cur.next
        if flag == 0:
            print("element not exist!")


    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    single_obj = SingleLinkList()
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

    print(single_obj.search(256))

    single_obj.remove(102)
