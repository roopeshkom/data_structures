from linked_list import LinkedList

class TestLinkedList:
    def test_add_to_tail(self):
        ll = LinkedList()
        assert str(ll) == ''
        for i in range(5):
            ll.add_to_tail(i)
        assert str(ll) == '0->1->2->3->4'

    def test_add_to_head(self):
        ll = LinkedList()
        assert str(ll) == ''
        for i in range(5):
            ll.add_to_head(i)
        assert str(ll) == '4->3->2->1->0'

    def test_contains(self):
        ll = LinkedList()
        for i in range(5):
            ll.add_to_tail(i)
        assert ll.contains(4) == True
        assert ll.contains(0) == True
        assert ll.contains(2) == True
        assert ll.contains(7) == False


    def test_first_index(self):
        ll = LinkedList()
        for i in range(5):
            ll.add_to_tail(i)
        assert ll.first_index(4) == 4
        assert ll.first_index(0) == 0
        assert ll.first_index(2) == 2
        assert ll.first_index(7) == -1
