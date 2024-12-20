class ListNode: #определяет структуру узла односвязного списка
    def __init__(self, x):
        self.val = x #каждый узел имеет значение val
        self.next = None #и ссылку на следующий узел next

class Solution(object):
    def get_intersection_node(self, headA, headB): #принимает на вход головы двух списков headA и headB
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB #два указателя pA и pB, которые будут проходить по спискам headA и headB
        while pA != pB: #цикл продолжается, пока указатели pA и pB указывают на разные узлы
            pA = headB if pA is None else pA.next #если pA указывает на None, то переустанавливается на голову второго списка
            pB = headA if pB is None else pB.next #то же самое, только уже с pB

        return pA #когда pA и pB совпадают, возвращатся узел, на который они указывают
                    #если они оба равны None, это означает, что пересечение отсутствует

node1a = ListNode(1) #создание узлов
node2a = ListNode(2)
node3a = ListNode(3)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node1b = ListNode(4)
node2b = ListNode(5)
node3b = ListNode(6)

node1a.next = node2a #соединение узлов в списки
node2a.next = node3a
node3a.next = node7
node7.next = node8
node8.next = node9

node1b.next = node2b
node2b.next = node3b
node3b.next = node7

solution = Solution()
intersection_node = solution.get_intersection_node(node1a, node1b)

if intersection_node:
    print(f'пересекающиеся узлы: {intersection_node.val}')
else:
    print('нет пересечения')