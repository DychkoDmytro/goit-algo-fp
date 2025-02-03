class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Додає новий елемент у кінець списку"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Виводить список"""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(head):
    """Реверсує однозв’язний список"""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort_linked_list(head):
    """Сортує однозв’язний список за допомогою сортування злиттям"""
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None  

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    return merge_sorted_lists(left, right)

def get_middle(head):
    """Знаходить середину списку"""
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(left, right):
    """Об’єднує два відсортовані списки"""
    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left or right
    return dummy.next

def merge_two_sorted_linked_lists(l1, l2):
    """Об’єднує два відсортовані списки в один"""
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# Тестування всіх функцій

# 1. Тест реверсування списку
print("Тест реверсування списку:")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("Оригінальний список:")
ll.print_list()

ll.head = reverse_linked_list(ll.head)
print("Реверсований список:")
ll.print_list()

# 2. Тест сортування злиттям
print("\nТест сортування злиттям:")
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print("Несортований список:")
ll.print_list()

ll.head = merge_sort_linked_list(ll.head)
print("Відсортований список:")
ll.print_list()

# 3. Тест об’єднання двох відсортованих списків
print("\nТест об’єднання двох відсортованих списків:")
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("Перший список:")
ll1.print_list()
print("Другий список:")
ll2.print_list()

merged_head = merge_two_sorted_linked_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Об’єднаний відсортований список:")
merged_list.print_list()