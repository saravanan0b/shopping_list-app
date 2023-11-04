# Custom functions for the shopping list program.
def get_shopping_list():
    with open("shoppinglist.txt", "r") as file_local:
        shopping_list_local = file_local.readlines()
    return shopping_list_local


def write_shopping_list(shopping_list_arg):
    with open("shoppinglist.txt", "w") as file_local:
        file_local.writelines(shopping_list_arg)
