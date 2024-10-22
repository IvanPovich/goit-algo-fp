from linked_list.linked_list import LinkedList
from fanc_link_list.reverse_list import reverse_list
from fanc_link_list.merge_sort import merge_sort, merge_sorted_list


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
   # Створимо два відсортовані списки
    print("Перший список:")
    first_list = LinkedList()
    first_list.insert_at_end(1)
    first_list.insert_at_end(3)
    first_list.insert_at_end(5)
    first_list.print_list()
    print("\nДругий список:")
    second_list = LinkedList()
    second_list.insert_at_end(2)
    second_list.insert_at_end(4)
    second_list.insert_at_end(6)
    second_list.print_list()
    merged_list = merge_sorted_list(first_list, second_list)

    print("\nНовий злитий в один, відсортований список:")
    merged_list.print_list()
