# Shopping list...
# Lorum Ipsum...
import shoplist_func
import time

datetime = time.strftime("%I:%M%p %A, %d %B %Y")
print("It is",datetime)

while True:
    v_decision = input("(add, edit, view, bought, exit)\nEnter decision: ")
    v_decision = v_decision.strip()
    
    if v_decision.startswith("add"):
        v_item = v_decision[4:] + "\n"

        shopping_list = shoplist_func.get_shopping_list()
        
        shopping_list.append(v_item)

        shoplist_func.write_shopping_list(shopping_list)
    elif v_decision.startswith("edit"):
        try:
            shopping_list = shoplist_func.get_shopping_list()

            v_itemno = int(v_decision[5:])
            v_newitem = input("Enter new item: ")
            v_itemno -= 1
            shopping_list[v_itemno] = v_newitem + "\n"

            shoplist_func.write_shopping_list(shopping_list)
        except ValueError:
            print("Command is not valid.\nEnter the no. to be edited.")
            continue
    elif v_decision.startswith("view"):
        shopping_list = shoplist_func.get_shopping_list()

        for list_no, ee in enumerate(shopping_list):
            ee = ee.strip("\n")
            list_item = f"{list_no + 1}. {ee}"
            print(list_item)
    elif v_decision.startswith("bought"):
        try:
            shopping_list = shoplist_func.get_shopping_list()

            v_bought_no = int(v_decision[7:])
            v_bought_no -= 1
            item_bought = shopping_list[v_bought_no].strip("\n")
            shopping_list.pop(v_bought_no)

            shoplist_func.write_shopping_list(shopping_list)

            message = F"The removed item from the cart is '{item_bought}'."
            print(message)
        except IndexError:
            print("Command is not valid.\nno. is out of range.")
            continue
    elif v_decision.startswith("exit"):
        break
    else:
        print('Command is not valid.')

exit("Nanri!!")
