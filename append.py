def list_operation(lst, add_item, remove_item):
    print("Original list: ", lst)

    lst.append(add_item)
    print(f"After appending {add_item} : ", lst)

    if remove_item in lst:
        lst.remove(remove_item)
        print(f"After removing {remove_item}: ", lst)

    else:
        print(f"{remove_item} not found in the list", lst)

    lst.sort()
    print("After sorting: ", lst)

my_list = [10, 20, 5, 15]
list_operation(my_list, add_item = 25, remove_item = 20)