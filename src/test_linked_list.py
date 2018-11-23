from linked_list import LinkedList

class TestLinkedList:
    def test_add_to_tail(self):
        test = LinkedList()
        for i in range(5):
            test.add_to_tail(i)
        assert str(test) == '0->1->2->3->4'

    def test_add_to_head(self):
        test = LinkedList()
        for i in range(5):
            test.add_to_head(i)
        assert str(test) == '4->3->2->1->0'
