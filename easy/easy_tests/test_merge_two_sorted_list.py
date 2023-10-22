import pytest
from easy.easy_solutions.merge_two_sorted_lists import Solution, ListNode


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def compare_linked_lists(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next
    return list1 is None and list2 is None


data = [
    (None, None, None),
    (create_linked_list([1, 3, 5]), None, create_linked_list([1, 3, 5])),
    (create_linked_list([1, 3, 5]), create_linked_list([2, 4, 6]), create_linked_list([1, 2, 3, 4, 5, 6])),
    (create_linked_list([1, 3, 5, 7, 9]), create_linked_list([2, 4, 6]), create_linked_list([1, 2, 3, 4, 5, 6, 7, 9]))
]


@pytest.mark.parametrize("list1, list2, expected_result", data)
def test_mergeTwoLists(list1, list2, expected_result):
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    assert compare_linked_lists(result, expected_result)
