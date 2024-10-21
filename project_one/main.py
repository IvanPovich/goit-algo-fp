from linked_list.linked_list import LinkedList
from fanc_link_list.reverse_list import reverse_list
from fanc_link_list.merge_sort import merge_sort, merge


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.insert_at_end(4)
    llist.insert_at_end(5)

    print("\nЗАВДАННЯ ПЕРШЕ: ")
    print("Оригінальний список:")
    llist.print_list()

    llist = reverse_list(llist)
    print("\nРеверсований список:")
    llist.print_list()

    print("\nЗАВДАННЯ ДРУГЕ: ")
    print("Оригінальний список:")
    llist.print_list()

    llist = merge_sort(llist)
    print("\nВідсортований список злиттям (merge):")
    llist.print_list()

    print("\nЗАВДАННЯ ТРЕТЄ: ")
    print("Оригінальні списки:")
    list_first = LinkedList()
    list_first.insert_at_end(1)
    list_first.insert_at_end(2)
    list_first.insert_at_end(3)
    list_first.insert_at_end(4)
    list_first.insert_at_end(5)
    list_second = LinkedList()
    list_second.insert_at_end(6)
    list_second.insert_at_end(7)
    list_second.insert_at_end(8)
    list_second.insert_at_end(9)

    new_list = merge(list_first, list_second)
    print("\nДва відсортовані списки злиті в один відсортований:")
    new_list.print_list()
